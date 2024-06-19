# ChatBot-AI
 
This code creates a simple conversational AI using the Transformers library and the Facebook Blenderbot-400M-distill model. It allows you to have an interactive chat with the model, and it will respond based on the conversation history.

Features:
Leverages Transformers for powerful natural language processing capabilities.
Uses the Blenderbot-400M-distill model, known for its ability to hold open-ended conversations.
Offers a user-friendly interface for interaction.

Requirements:
Python (https://www.python.org/downloads/)
Transformers library (pip install transformers)
A GPU is recommended for optimal performance (but can run on CPU as well)

Usage:
Save the code as a Python script (e.g., chatbot.py).
Run the script using python chatbot.py.
The model will be downloaded on the first run (might take some time).
Type your message and press Enter. The AI will respond, continuing the conversation.
Type "exit" and press Enter to stop the chat.

Explanation:

Imports:
Imports necessary classes from the Transformers library (AutoTokenizer, AutoModelForSeq2SeqLM) for working with pre-trained models and tokenization.

Model and Tokenizer:
Loads the pre-trained model (facebook/blenderbot-400M-distill) using AutoModelForSeq2SeqLM.from_pretrained.
Loads the corresponding tokenizer using AutoTokenizer.from_pretrained.

Conversation History:
conversation_history is a list that stores the conversation between you and the AI.

Main Loop:
The loop continues until the user types "exit".
The conversation history is formatted into a string with each message on a new line.
User input is received.
Both the history string and user input are tokenized using the tokenizer.
The model generates a response with a maximum number of tokens specified by max_tokens.
The generated response is decoded back into text and printed.
Both the user input and response are added to the conversation history.

Conversation History Cleanup:
After exiting the loop, the conversation history is cleared.

Customization:
You can adjust the max_tokens parameter to control the length of the model's response.
Experiment with different pre-trained models from the Transformers library for varied conversation styles.

Disclaimer:
Large language models like Blenderbot are still under development and may generate responses that are not entirely factual or relevant. Use this code for educational or entertainment purposes only.