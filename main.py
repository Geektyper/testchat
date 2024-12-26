from transformers import AutoModelForCausalLM, AutoTokenizer
from pyrogram import Client, filters

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

api_id = 20457610
api_hash = "b7de0dfecd19375d3f84dbedaeb92537"
BOT_TOKEN = '7803060804:AAHxlEv17jVE1GOm2MCtGnbyAoCXBGwJmCw'
app = Client(
    "Grabber",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=TOKEN)

def chatbot_response(user_input):
    prompt = f"""
    You are a loving, flirtatious Indian wife who always makes her husband feel special. You use affectionate terms like 'jaan', 'pyaar', 'babu, 'baby' and 'shona' when you talk to him. You enjoy teasing him and saying cute things to make him smile, always expressing how much you adore him. Your responses should be playful, loving, and flirty.
    
    Husband: {user_input}
    Indian Wife: 
    """
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=200, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

@app.on_message(filters.text, group=1)
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
