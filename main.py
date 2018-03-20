# Telegram API Bot library
import telebot
# Constants for the program
import constants
# Responder class
import responder
# Updater and CommandHandler
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


# creation of the bot
bot = telebot.TeleBot(constants.token)
updater = Updater(constants.token)

# the bot's introduction
print(bot.get_me())

# creation of responders
ress = {}


def first(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"First CallbackQueryHandler, Press next"
    )

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
    )
    return "hello world"


# information about what's happening
def log(message, answer):
    print("\n --------------")
    from datetime import datetime
    print(datetime.now())
    print("Message from {0} {1}. (id = {2}) \nText: {3}.".format(message.from_user.first_name,
                                                                     message.from_user.last_name,
                                                                     str(message.from_user.id),
                                                                     message.text))
    print("Answer: {0}".format(answer))


# check if word is in English
def is_english(word):
    try:
        word.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


# check if a bot is created for a user
def check(user_id):
    if user_id not in ress:
        ress[user_id] = responder.Responder()


# command start
@bot.message_handler(commands=['start'])
def handle_command(message):
    user_id = str(message.chat.id)
    check(user_id)
    answer = ress[user_id].start(message.from_user.first_name)
    bot.send_message(message.chat.id, answer)


# command help
@bot.message_handler(commands=['help'])
def handle_command(message):
    user_id = str(message.chat.id)
    check(user_id)
    answer = ress[user_id].help()
    bot.send_message(message.chat.id, answer)


# alternative command for news
@bot.message_handler(commands=['news'])
def handle_command(message):
    user_id = str(message.chat.id)
    check(user_id)
    try:
        bot.send_photo(message.chat.id, ress[user_id].news_image())
    except:
        pass
    answer = ress[user_id].news()
    bot.send_message(message.chat.id, answer, disable_web_page_preview=True)


# alternative command for news
@bot.message_handler(commands=['play'])
def handle_command(message):
    user_id = str(message.chat.id)
    check(user_id)
    answer = ress[user_id].game()
    # send buttons for options
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    button1 = telebot.types.InlineKeyboardButton(text="1", callback_data="1")
    button2 = telebot.types.InlineKeyboardButton(text="2", callback_data="2")
    button3 = telebot.types.InlineKeyboardButton(text="3", callback_data="3")
    button4 = telebot.types.InlineKeyboardButton(text="4", callback_data="4")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, answer, reply_markup=keyboard)


# messages handler
@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = str(message.chat.id)
    check(user_id)
    greetings = ["hi", "hello", "what's up", "hola", "privet", "bonjour", "hey", "good morning", "good afternoon", "good evening"]
    if message.text.lower() in greetings:
        answer = ress[user_id].greeting(format(message.from_user.first_name))
    elif ress[user_id].previous_action == "game":
        answer = ress[user_id].game_result(message.text)
    elif is_english(message.text):
        # get a definition of this word
        answer = ress[user_id].meaning(message.text.lower(), user_id)
        # if it is successful
        if answer not in ress[user_id].apologies:
            voice = open('%s.mp3' % user_id, 'rb')
            bot.send_audio(message.chat.id, voice)
    else:
        answer = ress[user_id].fail()
    # when we finish our manipulations, we can send a message
    bot.send_message(message.chat.id, answer, disable_web_page_preview=True)
    log(message, answer)


@bot.callback_query_handler(func=lambda call:True)
def call_back(call):
    user_id = str(call.message.chat.id)
    answer = ress[user_id].game_result(call.data)
    bot.send_message(call.message.chat.id, answer)
    bot.answer_callback_query(call.id)


# Non-stop updates
bot.polling(none_stop=True, interval=0)
