import telebot
from random import randint
from time import sleep
from string import ascii_lowercase
from gtts import gTTS
from qrcode import make
from khayyam import JalaliDatetime

def create_MainMenu():
    markup = telebot.types.ReplyKeyboardMarkup()
    itembtn_One = telebot.types.KeyboardButton('/game')
    itembtn_Two = telebot.types.KeyboardButton('/age')
    itembtn_Three = telebot.types.KeyboardButton('/voice')
    itembtn_Four = telebot.types.KeyboardButton('/max')
    itembtn_Five = telebot.types.KeyboardButton('/argmax')
    itembtn_Six = telebot.types.KeyboardButton('/qrcode')
    itembtn_Seven= telebot.types.KeyboardButton('/help')
    markup.row(itembtn_One, itembtn_Five)
    markup.row(itembtn_Four, itembtn_Two)
    markup.row(itembtn_Six, itembtn_Three)
    markup.row(itembtn_Seven)
    return markup

def create_GameMenu():
    markup_game = telebot.types.ReplyKeyboardMarkup()
    itembtn_game_one = telebot.types.KeyboardButton('New Game')
    itembtn_game_Two = telebot.types.KeyboardButton('Exit')
    markup_game.row(itembtn_game_one)
    markup_game.row(itembtn_game_Two)
    return markup_game

bot = telebot.TeleBot("5008203854:AAFQjdI3YTisXJklf0ZLWbANLGYzzAOERgE")

markup= create_MainMenu()

markup_Game= create_GameMenu()

#%%
# /start

@bot.message_handler(commands=['start'])
def send_Wolcome(message):
    bot.reply_to(message, 'Dear {}, welcome to my bot 🙋🏻‍♂️💙'.format(message.from_user.first_name))
    msg = bot.send_message(message.chat.id, 'Please choose one item 👇', reply_markup=markup)

#%%
# /game

randomNumber=randint(0, 1001)

@bot.message_handler(commands=['game'])
def define_Game(message):
    bot.send_message(message.chat.id, 'In this section, you have to guess a number and the bot guides you (go up, go down, you win)')
    msg = bot.send_message(message.chat.id, 'Please guess a number (0 to 1000)', reply_markup=markup_Game)
    bot.register_next_step_handler(msg, play_Game)

def play_Game(message):
    if message.text == 'Exit':
        bot.send_message(message.chat.id, 'you are out of the game')
        bot.send_message(message.chat.id, 'Please choose one item 👇', reply_markup=markup)
    else:
        try:
            if message.text == 'New Game':
                global randomNumber
                randomNumber=randint(0, 1001)
                bot.send_message(message.chat.id, 'The game restarted')
                msg =  bot.send_message(message.chat.id, 'Please guess a number (0 to 1000)', reply_markup=markup_Game)
                bot.register_next_step_handler(msg, play_Game)
            elif float(message.text) > randomNumber:
                msg = bot.send_message(message.chat.id, 'Enter a smaller number',reply_markup=markup_Game)
                bot.register_next_step_handler(msg, play_Game)
            elif float(message.text) < randomNumber:
                msg = bot.send_message(message.chat.id, 'Enter a larger number',reply_markup=markup_Game)
                bot.register_next_step_handler(msg, play_Game)
            else:
                bot.send_message(message.chat.id, 'you win 🏆')
                msg = bot.send_message(message.chat.id, 'please choose one item 👇', reply_markup=markup)
        except:
            bot.send_message(message.chat.id, 'your input must be an intrger number 🤦🏻‍♂️')
            msg = bot.send_message(message.chat.id, 'Please guess a number (0 to 1000)', reply_markup=markup_Game)
            bot.register_next_step_handler(msg, play_Game)

#%%
# /argmax

@bot.message_handler(commands=['argmax'])
def send_argmax(message):
    bot.send_message(message.chat.id, 'in this section, an array like the following example will be taken from you, then the index of the largest number in the array is viewed 👇')
    bot.send_message(message.chat.id, '1,2,3,4,5,6,7')
    msg = bot.send_message(message.chat.id, 'Please enter your desired array', reply_markup=markup)
    bot.register_next_step_handler(msg, find_argmax)

def find_argmax(message):
    try:
       myArray= list(map(int, message.text.split(',')))
       indexOfLargestNumber=myArray.index(max(myArray))
       bot.send_message(message.chat.id, 'The index of the largest number in the desired array is equal to {}'.format(indexOfLargestNumber))
       bot.send_message(message.chat.id, 'please choose one item 👇', reply_markup=markup)
    except:
        bot.send_message(message.chat.id, 'Please enter the desired array according to the given pattern 🤦🏻‍♂️')
        bot.send_message(message.chat.id, 'in this section, an array like the following example will be taken from you, then the index of the largest number in the array is viewed 👇')
        bot.send_message(message.chat.id, '1,2,3,4,5,6,7')
        msg = bot.send_message(message.chat.id, 'Please enter your desired array', reply_markup=markup)
        bot.register_next_step_handler(msg, find_argmax)

#%%
# /max

@bot.message_handler(commands=['max'])
def send_max(message):
    bot.send_message(message.chat.id, 'in this section, an array like the following example will be taken from you, then the largest number in the array is viewed 👇')
    bot.send_message(message.chat.id, '1,2,3,4,5,6,7')
    msg = bot.send_message(message.chat.id, 'Please enter your desired array', reply_markup=markup)
    bot.register_next_step_handler(msg, find_max)

def find_max(message):
    try:
       myArray= list(map(int, message.text.split(',')))
       LargestNumber=max(myArray)
       bot.send_message(message.chat.id, 'The largest number in the desired array is equal to {}'.format(LargestNumber))
       bot.send_message(message.chat.id, 'please choose one item 👇', reply_markup=markup)
    except:
        bot.send_message(message.chat.id, 'Please enter the desired array according to the given pattern 🤦🏻‍♂️')
        bot.send_message(message.chat.id, 'in this section, an array like the following example will be taken from you, then the largest number in the array is viewed 👇')
        bot.send_message(message.chat.id, '1,2,3,4,5,6,7')
        msg = bot.send_message(message.chat.id, 'Please enter your desired array', reply_markup=markup)
        bot.register_next_step_handler(msg, find_max)

#%%
# /voice
    
@bot.message_handler(commands=['voice'])
def send_voice(message):
    bot.send_message(message.chat.id, 'In this section, an English text will be taken from you and its voice will be sent to you')
    msg = bot.send_message(message.chat.id, 'Please enter your desired text', reply_markup=markup)
    bot.register_next_step_handler(msg, create_voice)

def isEnglishText(message):
    alph = ascii_lowercase

    for char in (message.text).lower():
        if char not in alph:
            return False
    return True

def create_voice(message):
    if isEnglishText(message)==False:
        bot.send_message(message.chat.id, 'Entered text must be in English 🤦🏻‍♂️')
        msg = bot.send_message(message.chat.id, 'Please enter your desired text', reply_markup=markup)
        bot.register_next_step_handler(msg, create_voice)
    else:
        content = gTTS(text=message.text, slow=False)
        content.save('voice.ogg')
        content = open('voice.ogg', 'rb')
        bot.send_voice(message.chat.id, content)
        bot.send_message(message.chat.id, 'please choose one item 👇', reply_markup=markup)

#%%
#/age

@bot.message_handler(commands=['age'])
def send_age(message):
    bot.send_message(message.chat.id, 'in this section, your date of birth is taken in solar Hijri like the following pattern and your age is calculated 👇')
    bot.send_message(message.chat.id, 'year/month/day')
    msg =bot.send_message(message.chat.id, 'Please enter the desired date of birth', reply_markup=markup)
    bot.register_next_step_handler(msg, calculate_age)

def calculate_age(message):
    try:
        if len((message.text).split('/')) == 3:
            date = JalaliDatetime.now() - JalaliDatetime(message.text.split('/')[0], message.text.split('/')[1], message.text.split('/')[2])
            bot.send_message(message.chat.id, 'You are {} years old'.format(date.days // 365))
            bot.send_message(message.chat.id, 'please choose one item 👇', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'The date of birth entered must be the same as the pattern 🤦🏻‍♂️')
            bot.send_message(message.chat.id, 'in this section, your date of birth is taken in solar Hijri like the following pattern and your age is calculated ')
            bot.send_message(message.chat.id, 'year/month/day')
            msg =bot.send_message(message.chat.id, 'Please enter the desired date of birth', reply_markup=markup)
            bot.register_next_step_handler(msg, calculate_age)
    except:
        bot.send_message(message.chat.id, 'The date of birth entered must be the same as the pattern 🤦🏻‍♂️')
        bot.send_message(message.chat.id, 'in this section, your date of birth is taken in solar Hijri like the following pattern and your age is calculated ')
        bot.send_message(message.chat.id, 'year/month/day')
        msg =bot.send_message(message.chat.id, 'Please enter the desired date of birth', reply_markup=markup)
        bot.register_next_step_handler(msg, calculate_age)

#%%
#/qrcode

@bot.message_handler(commands=['qrcode'])
def send_qrcode(message):
    bot.send_message(message.chat.id, 'In this section, a string is taken and its qrcode is sent to you')
    msg = bot.send_message(message.chat.id, 'Please enter your desired string', reply_markup=markup)
    bot.register_next_step_handler(msg, create_qrcode)

def create_qrcode(message):
    image = make(message.text)
    image.save('QR-Code.png')
    photo = open('QR-Code.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, 'please choose one item 👇', reply_markup=markup)

#%%
#/help

gameCommand_Guide='In this section, you have to guess a number and the bot guides you (go up, go down, you win)'
argmaxCommand_Guide='in this section, an array like the following example will be taken from you, then the index of the largest number in the array is viewed\n👉 1,2,3,4,5,6,7'
maxCommand_Guide='in this section, an array like the following example will be taken from you, then the largest number in the array is viewed\n👉 1,2,3,4,5,6,7'
voiceCommand_Guide='In this section, an English text will be taken from you and its voice will be sent to you'
ageCommand_Guide='in this section, your date of birth is taken in solar Hijri like the following pattern and your age is calculated\n👉 year/month/day'
qrcodeCommand_Guide='In this section, a string is taken and its qrcode is sent to you'
helpCommand_Guide='This section is the bot guide'

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, '/game \n{}\n\n/argmax \n{}\n\n/max \n{}\n\n/voice \n{}\n\n/age \n{}\n\n/qrcode \n{}\n\n/help \n{}'.format(gameCommand_Guide, argmaxCommand_Guide, maxCommand_Guide, voiceCommand_Guide, ageCommand_Guide, qrcodeCommand_Guide, helpCommand_Guide), reply_markup=markup)

#%%
bot.infinity_polling()