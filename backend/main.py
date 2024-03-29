# uvicorn main:app
# uvicorn main:app --reload

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custom Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

# Initiate App
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
    "http://localhost:8000",
    "https://teacher-leonor.onrender.com",
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check health
@app.get("/health")
async def check_health():
    return {"message": "healthy"}


# Check health
@app.get("/")
def root():
    return {"message": "Hello, access page '/docs' to see endpoints"}


# Reset Messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation reset"}


# Get audio
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    print(f"Incoming request headers: {file.headers}")
    
    # # Get saved audio
    # audio_input = open("voice.mp3", "rb")
    
    # Save file from frontend
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
        
    audio_input = open(file.filename, "rb")
    
    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)
    
    # Guard: Ensure message decoded
    if not message_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode audio.")
    
    # Get ChatGPT Response
    chat_response = get_chat_response(message_decoded)
    
    # Guard: Ensure message decoded
    if not chat_response:
        raise HTTPException(status_code=400, detail="Failed to get chat response.")
    
    # Store messages
    store_messages(message_decoded, chat_response)
    
    # Convert chat response to audio
    print("\nChat Response: ", chat_response)
    audio_output = convert_text_to_speech(chat_response)
    
    # Guard: Ensure message decoded
    if not audio_output:
        raise HTTPException(status_code=400, detail="Failed to get Eleven Labs audio response.")
    
    # Create a generator that yields chunks of data
    # def iterfile():
    #     yield audio_input
        
    # Return audio file
    return StreamingResponse(iter([audio_output]), media_type="application/octet-stream")
