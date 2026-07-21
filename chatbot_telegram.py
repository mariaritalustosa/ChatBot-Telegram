import telebot
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

key_token_telegram = os.getenv("token_telegram")
key_open_router = os.getenv("key_open_router")


bot = telebot.TeleBot(key_token_telegram)

@bot.message_handler(commands= ["start"])
def welcome_message(mensagem):
    bot.reply_to(mensagem, "Bem-vindo")

@bot.message_handler(func = lambda m: True)
def reply_my_messages(mensagem):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + key_open_router,
        },
        data=json.dumps({
            "model": "openai/gpt-oss-20b:free",
            "messages": [
                {
                    "role": "user",
                    "content": mensagem.text
                }
            ]
        })
    )
    dados = response.json()
    if "choices" in dados:
        texto_ia = dados["choices"][0]["message"]["content"]
        bot.reply_to(mensagem, texto_ia)
    else:
        print("Erro na resposta", dados)   

print("Bot iniciado")

bot.polling()

