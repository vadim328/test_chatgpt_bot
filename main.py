import telebot
import requests
import json

bot = telebot.TeleBot('')


def use_api_chatgpt(mes):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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',
    }

    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': mes,
            },
        ],
        'temperature': 0.7,
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)
    resp_dickt = response.json()
    return resp_dickt['choices'][0]['message']['content']


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, малышка, задай мне свой вопрос ;)")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, use_api_chatgpt(message.text))


bot.polling(none_stop=True, interval=0)

