import requests
import json
from config.config import API_KEY
def send_chat_to_npc(content):
    f = open("input.txt")
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": API_KEY,
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>",
        "X-Title": "<YOUR_SITE_NAME>",
    },
    data=json.dumps({
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
        {
            "role": "user",
            "content": f.read() + content
        }
        ],
        
    })
    )
    if response.status_code == 200:
        try:
            response_data = response.json()
            ai_response = response_data['choices'][0]['message']['content']
            print("AI Response:", ai_response)
            
        except KeyError:
            print("Error: Unexpected response format")
    else:
        print(f"Error: {response.status_code} - {response.text}")



def main():
    send_chat_to_npc("chop down some tree")

if __name__ == "__main__":
    main()