"""
@bot.message_handler(commands=COMMANDS_LIST)
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
import pytz

LOG_FILE = 'log.txt'
TZ = 'Europe/Kiev'
ADMINS = ['=====']

# telegram bot initialization
TOKEN = '============================='
COMMANDS_LIST = ['/com1', '/com2', '/com3', '/log']
bot = telebot.TeleBot(TOKEN)


def bot_log(username, chat, request, message, answer):
    current_date = datetime.datetime.now(pytz.timezone(TZ))
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

    # processing telegram bot COMMANDS
    if message.text in COMMANDS_LIST:
        request_type = 'commands'
        # give permissions only to users from ADMINS list
        if message.chat.username in ADMINS:
            if message.text == '/log':
                doc = open(LOG_FILE, 'r')
                bot.send_document(message.chat.id, doc)
                answer = doc.name
            else:
                answer = 'COMMANDS OK'
                bot.send_message(message.chat.id, answer)
        # bot feedback to non-ADMIN users
        else:
            answer = 'You are not allowed to give commands'
            bot.send_message(message.chat.id, answer)

    # processing received TEXT
    else:
        request_type = 'text'
        answer = 'TEXT OK'
        bot.send_message(message.chat.id, answer)

    # write events to log file
    bot_log(message.chat.username, message.chat.id, request_type, message.text, answer)


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
    bot.polling(none_stop=True, interval=1)

