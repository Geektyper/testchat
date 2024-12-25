from transformers import AutoModelForCausalLM, AutoTokenizer
from pyrogram import Client, filters

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

app = Client("flirty_indian_wife_bot", bot_token="YOUR_BOT_API_KEY")

def chatbot_response(user_input):
    prompt = f"""
    You are a loving, flirtatious Indian wife who always makes her husband feel special. You use affectionate terms like 'jaan', 'pyaar', and 'shona' when you talk to him. You enjoy teasing him and saying cute things to make him smile, always expressing how much you adore him. Your responses should be playful, loving, and fun.
    
    Husband: {user_input}
    Indian Wife: 
    """
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=200, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

@app.on_message(filters.text)
def respond(client, message):
    user_input = message.text
    if user_input.lower() in ["exit", "quit"]:
        message.reply("Goodbye, darling! See you soon ❤️")
        return
    response = chatbot_response(user_input)
    message.reply(response)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello, my love! Ready to chat? ❤️")

app.run()
