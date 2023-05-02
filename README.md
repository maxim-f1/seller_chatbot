# seller_chatbot
The bot is connected to GPT3.5 waiting for a message from the user. The GPT is programmed to sell a trial subscription. It is not distracted by other conversations, its only purpose is to sell!

It uses a cached index.json file to compose the response, which stores the context for the response. This saves tokens.

To change the Prompt parameters, delete prompt/index.json and add/modify the contents of prompt/data/ 
