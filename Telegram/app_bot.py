"""
TEMP_FILE = 'temp.json'
bot.send_message(73102344, 'Hello, bro')

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


LOG_FILE = 'tmp.log'

# telegram bot initialization
TOKEN = '679780471:AAGle4zlZCDpOrBCLPK0lf9QaJBzB04m-Hs'
COMMANDS_LIST = ['/c1', '/c2', '/c3', '/help']
bot = telebot.TeleBot(TOKEN)


def bot_log(chat, request, message, answer):
    current_date = datetime.datetime.now()
    if not os.path.isfile(LOG_FILE):
        with open(LOG_FILE, 'w') as file:
            file.write('time: {}, chat_ID:{}, request:{}, message_received: {}, message_send: {}\n'.format(
                str(current_date.strftime("%Y-%m-%d -- %H:%M:%S")), chat, request, message, answer)
            )
    else:
        with open(LOG_FILE, 'a') as file:
            file.write('time: {}, chat_ID:{}, request:{}, message_received: {}, message_send: {}\n'.format(
                str(current_date.strftime("%Y-%m-%d -- %H:%M:%S")), chat, request, message, answer)
            )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text in COMMANDS_LIST:
        request_type = 'commands'
        answer = 'COMMANDS OK'
        bot.send_message(message.chat.id, answer)
        bot_log(message.chat.id, request_type, message.text, answer)
    else:
        request_type = 'text'
        answer = 'TEXT OK'
        bot.send_message(message.chat.id, answer)
        bot_log(message.chat.id, request_type, message.text, answer)


@bot.message_handler(content_types=['document'])
def handle_files(message):
    request_type = 'documents'
    answer = 'DOCS OK'
    bot.send_message(message.chat.id, answer)
    bot_log(message.chat.id, request_type, message.text, answer)


@bot.message_handler(content_types=['photo'])
def handle_files(message):
    request_type = 'photos'
    answer = 'PHOTO OK'
    bot.send_message(message.chat.id, answer)
    bot_log(message.chat.id, request_type, message.text, answer)


@bot.message_handler(content_types=['sticker'])
def handle_files(message):
    request_type = 'stickers'
    answer = 'STICKER OK'
    bot.send_message(message.chat.id, answer)
    bot_log(message.chat.id, request_type, message.text, answer)


if __name__ == '__main__':
    updates = bot.get_updates()

    bot.polling(none_stop=True, interval=0)

