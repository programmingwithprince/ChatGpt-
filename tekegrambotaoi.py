from flask import Flask
import telebot
import requests

TOKEN = '6399514429:AAGYGeqGVqXnoqXP0C-7m8s_tQNRbq_kdb8'

bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	try:
	    bot.reply_to(message,'Preparing your answer. please wait!')
	    print(message.text)
	    req = requests.post('https://langchain-app--codewithharry.repl.co/generate', json= {"prompt":message.text})
	    bot.reply_to(message, req.text)           
	except Exception as e:
	    print(e)
	    bot.reply_to(message,'Unable to process your request currently!')
bot.infinity_polling()        




app = Flask(__name__)
 @app.route('/')
def hello_world():
    return 'Hello World'
 

app.run()
