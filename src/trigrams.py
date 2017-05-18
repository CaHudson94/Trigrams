"""."""
import io
import random
import sys
import os


def main(text='temp.txt', n='21'):
    """."""
    if os.path.isfile(text):
        if os.stat(text).st_size >= 1:
            dictionary = build_dict(text)
            if dictionary:
                n = int(n)
                return build_words(n, dictionary)
            return'\nThe file should have three or more words.\n'
        elif os.stat(text).st_size == 0:
            return '\nThis text file is empty.\n'
    else:
        return 'Please enter a valid file name'


def build_dict(text='temp.txt'):
    """."""
    dictionary = {}
    word1 = ''
    word2 = ''
    temp = ''
    fi = io.open(text, encoding='utf-8')
    for line in fi:
        words_from_file = line.split()
        if len(words_from_file) >= 3:
            for word in words_from_file:
                if word1 == '':
                    word1 = word
                elif word2 == '':
                    word2 = word
                else:
                    temp = word1 + ' ' + word2
                    if temp in dictionary:
                        ltemp = dictionary[temp]
                        ltemp.append(word)
                        dictionary[temp] = ltemp
                    else:
                        dictionary[temp] = [word]
                    word1 = word2
                    word2 = word
        elif len(words_from_file) < 3:
            return
    return dictionary


def get_random(x):
    """."""
    from random import randint
    return randint(0, x - 1)


def build_words(n, dictionary):
    """."""
    lent = random.choice(list(dictionary.keys()))
    leng = lent.split()
    word1 = leng[0]
    word2 = leng[1]
    result = leng[0].capitalize()
    result = result + ' ' + leng[1]
    for x in range(0, n - 2):
        temp = word1 + ' ' + word2
        tlist = list(dictionary[temp])
        o = get_random(len(tlist))
        new_word = tlist[o]
        result = result + ' ' + new_word
        word1 = word2
        word2 = new_word
        testword = word1 + ' ' + word2
        if testword not in dictionary:
            lent = random.choice(list(dictionary.keys()))
            leng = lent.split()
            word1 = leng[0]
            word2 = leng[1]
    return result


if __name__ == '__main__':
    if (len(sys.argv) == 3):
        print(main(sys.argv[1], sys.argv[2]))
    else:
        print(main())
