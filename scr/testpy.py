import io
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
                    print(dictionary[temp])
                    ltemp = dictionary[temp]
                    ltemp.appened(word)
                    print(ltemp)
                    dictionary[temp] = dictionary[temp].append(word)
                else:
                    dictionary[temp] = [word]
                word1 = word2
                word2 = word
    print(dictionary.items())
trigrams()
                
