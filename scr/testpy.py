import io
import random
dictionary = {}
def trigrams(text = 'temp.txt'):
    word1 = ''
    word2 = ''
    temp = ''
    fi = io.open(text, encoding ='utf-8')
    for line in fi:
        for word in line.split():
            if word1 == '':
                word1 = word
            elif word2 == '':
                word2 = word
            else:
                temp = word1 +' '+ word2
                if  temp in dictionary:
                    ltemp = dictionary[temp]
                    ltemp.append(word)
                    dictionary[temp] = ltemp
                else:
                    dictionary[temp] = [word]
                word1 = word2
                word2 = word
    print(dictionary.items())
def getRandom(x):
    from random import randint
    return randint(0,x -1)
def build_words(n):
    lent = random.choice(list(dictionary.keys()))
    leng = lent.split()
    word1 = leng[0]
    word2 = leng[1]
    result = leng[0].capitalize()
    result = result + ' ' +leng[1]
    for x in range(0,n- 2):
        temp = word1 +  ' ' +word2
        tlist =list( dictionary[temp])
        o = getRandom(len(tlist))
        new_word = tlist[o]
        result = result + ' '+ new_word
        word1 = word2
        word2 = new_word
        testWord = word1 + ' '+ word2
        if testWord not in dictionary:
            lent = random.choice(list(dictionary.keys()))
            leng = lent.split()
            word1 = leng[0]
            word2 = leng[1]
    print(result)

                
