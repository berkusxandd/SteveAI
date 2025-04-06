# About the project
This project will allow us to create better AI system for Unreal Engine 5 with AIController and Smart Object integrations. Type what you want from NPC to do, it will do it for you!

# API
I used DeepSeek V3 0324 for all of my tests and demo video. This worked the fastest and reasonable with the backstory.

# Backstory for API calls
With the input file that I put in the repo, you can request from the AI model to behave like an NPC. Only thing that you should do just add your chat input afterwards. 

# BP_AIAPI
This is basically brain of the NPC. This object will parse all the inputs/outputs and finally sends a meaningful behaviour to the NPC. This object also keeps the inventory of the NPC which can be changed in the future.

# BP_NPC
This is our actor blueprint for the NPC character. Animation can be replaced, or if you wish, new behaviours can be added.

# Output
Output struct is:
input-type: [command, info (basic chatting, whats up, how are you etc.)]  
action: [cutting,attack,equip,calling, position]  
target: [the target that it understands (tree, enemy, red enemy, biggest enemy, strongest zombie)]  
response: [null,if NPC has something to say]  

Watch the Demo Video:
https://drive.google.com/file/d/16WMetxTO5P7IBERTv5ukSaQVosGMoyD9/view?usp=sharing

![image](https://github.com/user-attachments/assets/67278eb9-2bc9-4764-8888-c81bf47b30fd)

