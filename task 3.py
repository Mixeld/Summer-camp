
"""
импорты всех библиотек
"""
import random
import telebot


"""
зарание известные параметры и функции
"""


# жизни
lives =  10

# варианты слов ( надо 10 штук )
word_variants = ["dog","cat","cola","home","flat","bus","school","garden","cofe","tree"]

word_variants[0]

# слово которое выбранно для игры
word_right=random.choise(word_variants)

# слово из "_" с угадыванием символами
word_in_game = "_" *len(world_right)
print ("lives memory",lives)

"""
команды для активаци игры-бота
"""
bot = telebot.Telebot(' token ')
@bot.message_header(commands=['start']
def send_welcome(message)
    bot.replay_to(message, 'я бот, приятно познакомиться',{message.from_user.first_name}'
@bot.messsage_headler(content_types=['text']
def get_txt_messages(messages)
    if message.text.lower()=='сыграем':
            bot.send_message(message.from_user.id 'Hi! Lets play! ')

            """
            игра
            """
            while ("_" in word_in_game) and (lives > 0):
                bot.send_message("lives memory", lives)
                bot.send_message(word_in_game)
                letter = input("input character")

                # есть ли буква в стллове
                if letter in word_right:
                    print(" you are right !! ")
                    index - 1
                    while word_in_game.count(letter) != word_right.count(letter):
                        index = word_right.find(letter, index + 1)
                        word_in_game = word_in_game[:index] + letter + word_in_game[index + 1:]
                    else:
                        lives - 1
                        print("Bad letter :(")
                    bot.send_message("*" * 10)
                if lives > 0:
                    bot.send_message(word_right)
                    bot.send_message("you are awesome")
                else:
                    bot.send_message("you lose !")
                    bot.send_message("word right", word_right)
# на тот случай если напишут что-то не то
    else:
        bot.send_message(message.from_user.id 'I cant undestand you')