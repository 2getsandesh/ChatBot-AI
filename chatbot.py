from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)

    # Get the input data from the user
    input_text = input("> ")
    if input_text == "exit":
        break

    # Tokenize the input text and history
    inputs = tokenizer(history_string, input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate the response from the model using max_new_tokens
    max_tokens = 60  # Example value, adjust as needed
    outputs = model.generate(**inputs, max_new_tokens=max_tokens)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    print(response)

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
    
conversation_history.clear()