import random

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

while ("_" in word_in_game) and (lives > 0 ):
    print("lives memory", lives)
    print (word_in_game)
    letter = input("input character")

    #есть ли буква в стллове
    if letter in word_right:
        print (" you are right !! ")
        index - 1
        while word_in_game.count(letter) !=word_right.count(letter):
            index = word_right.find(letter, index + 1 )
            word_in_game = word_in_game[:index] + letter + word_in_game[index + 1 :]
        else:
            lives - 1
            print ("Bad letter :(")
        print("*"* 10)

    if lives > 0:
        print (word_right)
        print ("you are awesome")
    else:
        print ("you lose !")
        print("word right",word_right)