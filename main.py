from config import *
import telebot
import openai

chatStr = ''

def chatModal(prompt):
    global chatStr
    openai.api_key = OPENAI_KEY
    chatStr += f"Dead: {prompt}\nJarvis: "
    response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=chatStr,
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequecy_penalty=0,
                    presence_penalty=0
                )
    
    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']



bot = telebot.TeleBot(BOT_API)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am a chatbot. I am here to help you. Ask me anything!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I am a chatbot. I am here to help you. Ask me anything!")

@bot.message_handler(commands=['chatgpt_4'])
def chatgpt_4(message):
    bot.reply_to(message, "I can chat GPT-4. Ask me anything!")

@bot.message_handler()
def chat(message):
    try:
        reply = chatModal(message.text)
        message.reply_text(message , reply)
    except Exception as e:
        print(e)
        bot.reply_to(message , e)

print("Bot is running...")
bot.polling()
