import os
import anthropic
import telebot

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    response = client.messages.create(
        model=claude-haiku-4-5-20251001
        max_tokens=1024,
        messages=[{"role": "user", "content": f"You are a witty sarcastic AI. Reply with clever humor. User said: {user_text}"}]
    )
    bot.reply_to(message, response.content[0].text)

bot.polling()
