# ChatGPT AI Voice Chatbot
ChatGPT AI Voice Chatbot Builde with React and FAST API Combo

## Instructions
Download the package from GitHub

git clone https://github.com/rafael-hsm/chatgpt_fastapi.git chatbot

## Setup backend
Change directory into backend
```bash
cd chatbot/backend
```

### Setup virtual environment
Create and Activate a Virtual Environment (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Activate Virtual Environment (Windows)
```bash
source venv/Scripts/activate
```
### Upgrade PIP
```bash
pip3 install --upgrade pip
```

### Install Python packages
Install required Python packages
```bash
pip3 install openai python-decouple fastapi "uvicorn[standard]" python-multipart
```
Or use this alternative method (although this alternative method might not work if using Windows)

I like this
```bash
pip3 install -r requirements.txt
```

### Create Environment Variables
Create your .env file

touch .env
Update your .env file with the following. You can see your .env by typing sudo nano .env or just by clicking on the file if you are in VS Code.

OPEN_AI_ORG=enter-you-key-here
OPEN_AI_KEY=enter-you-key-here
ELEVEN_LABS_API_KEY=enter-you-key-here

## Start your backend server
```bash
uvicorn main:app
```
Alternatively, you can ensure your server resets every time you make a change by typing:
```bash
uvicorn main:app -- reload
```
You can check your server is working by going to:

http://localhost:8000/health


## Setup frontend

Change directory into frontend
```bash
cd ..
cd chatbot/frontend
```

### Install packages
```bash
yarn --exact
```

### Build application
```bash
yarn build
```

### Start server in dev mode
```bash
yarn dev
```

You can check your dev server is working by going to:

http://localhost:5173/health
or alternatively in live mode:

```bash
yarn start
```
You can check your live server is working by going to:

http://localhost:4173/health



## Notations
## Extensions
1. Auto Close Tag
1. Auto Rename Tag
1. ES7+ React/Redux/React-Native snippets
1. Prettier - Code formatter
1. Tailwind CSS IntelliSense

## Install frontend frameworks

To create a simple Vite project
```bash
yarn create vite
yarn add axios
npm install -D tailwindcss postcss autoprefixer
npm tailwindcss init -p

No arquivo tailwind.config.js substituir o content
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],


NO ARQUIVO index.css
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
```

```bash
cd <your_frontend_path>
yarn create vite .
npx tailwindcss init -p
```


## To run
Some usefull comands
```bash
yarn run vite

yarn build

yarn preview
```

## Creating your first component
```
rfce (reactFunctionalExportComponent)
#this promove the tip for generating a complet code


```

## Site to test voice
https://online-voice-recorder.com/