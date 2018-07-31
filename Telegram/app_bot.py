"""
@bot.message_handler(commands=COMMANDS_LIST)
def handle_c1(message):
    bot.send_message(message.chat.id, 'COMMANDS OK')

@bot.message_handler
    content_types=['text']
    content_types=['commands']
    content_types=['document']
    content_types=['audio']
    content_types=['photo']
    content_types=['sticker']
"""
import telebot
import datetime
import os.path

LOG_FILE = 'log.txt'

# telegram bot initialization
TOKEN = '============================'
COMMANDS_LIST = ['/com1', '/com2', '/com3', '/log']
bot = telebot.TeleBot(TOKEN)


def bot_log(username, chat, request, message, answer):
    current_date = datetime.datetime.now()
    if not os.path.isfile(LOG_FILE):
        mode = 'w'
    else:
        mode = 'a'
    with open(LOG_FILE, mode) as file:
        file.write('time: {}, username:{}, chat_ID:{}, request:{}, message_received: {}, message_send: {}\n'.format(
            str(current_date.strftime("%Y-%m-%d %H:%M:%S")), username, chat, request, message, answer)
        )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text in COMMANDS_LIST:
        request_type = 'commands'
        if message.text == '/log':
            doc = open(LOG_FILE, 'r')
            answer = doc.name
            bot_log(message.chat.username, message.chat.id, request_type, message.text, answer)
            bot.send_document(message.chat.id, doc)
        else:
            answer = 'COMMANDS OK'
            bot_log(message.chat.username, message.chat.id, request_type, message.text, answer)
            bot.send_message(message.chat.id, answer)
    else:
        request_type = 'text'
        answer = 'TEXT OK'
        bot_log(message.chat.username, message.chat.id, request_type, message.text, answer)
        bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['document'])
def handle_files(message):
    request_type = 'documents'
    answer = 'DOCS OK'
    bot_log(message.chat.username, message.chat.id, request_type, message.text, answer)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['photo'])
def handle_files(message):
    request_type = 'photos'
    answer = 'PHOTO OK'
    bot_log(message.chat.username, message.chat.id, request_type, message.text, answer)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['sticker'])
def handle_files(message):
    request_type = 'stickers'
    answer = 'STICKER OK'
    bot_log(message.chat.username, message.chat.id, request_type, message.text, answer)
    bot.send_message(message.chat.id, answer)


if __name__ == '__main__':
    updates = bot.get_updates()
    bot.polling(none_stop=True, interval=0)

