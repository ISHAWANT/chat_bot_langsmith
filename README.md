# chat_bot with lang-smith integration 

#### 1. Create a env 

```bash 
conda create -p venv python=3.12 -y 
``` 

#### 2. Activate the env 

```bash
conda activate venv/
``` 

#### 3. Install the packages from requirements.txt 
```bash 
pip install -r requirements.txt 
``` 

#### 4. Create a .evn file 

```bash 
GROQ_API_KEY = "groq api key here" 

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="langsmith api key here"
LANGSMITH_PROJECT="Chatbot_Project"