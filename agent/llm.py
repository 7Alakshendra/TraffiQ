import requests

PROVIDER="ollama"

def chat(prompt):
    if PROVIDER == "ollama":
        URL = "http://localhost:11434/api/chat"
        payload = {
            "model": "llama3.2:3b",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        response = requests.post(URL, json=payload)
        return response.json()['message']['content']
    
    elif PROVIDER == "anthropic":
        pass  # implement later

if __name__=="__main__":
    response=chat("Explain traffic congestion in one sentence.")
    print(response)
    
