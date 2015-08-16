#       Name:  Jesus Ivan Gonzalez
#       Date:  Aug 16th 2015
#       Description:  Given a list of scramble words, return the possible word
#           in a given word list
#--------------------------------------------------------------------------

#Returns wordCompare if all letters in descramble are in wordCompare, else None
def stripWordList(descramble, wordCompare):
    counter = 0
    for i in range(len(descramble)):
        if descramble[i] in wordCompare:
            counter += 1
        else:
            return None
    if counter == len(descramble):
        return wordCompare
    return None



#Accepts 'wordlist.txt', looks at each line, and calls stripWordList, returns shorter Word List
def possibleChoices(descramble, fWordList):
    newWordList = []
    for line in fWordList:
        line = line[:len(line)-1]
        newWordItem = stripWordList(descramble, line)
        if newWordItem != None:
            newWordList.append(newWordItem)
            newWordItem = []
    return newWordList

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

#List of scramble words
descramble = ['mkeart', 'sleewa', 'edculds', 'iragoge', 'usrlsle', 'nalraoci', 'nsdeuto',
              'amrhat', 'inknsy', 'iferkna']

#Main portion of code.  Calls possibleChoices(), returns new possible answers.  Words with
#a single answer is returned as is.  Words with multiple answers will compare its letters in the
#to the letters of the scrambled word.  Only returns when all letters match.
for i in range(len(descramble)):
    fhandle = open('wordlist.txt','r')
    possibleWords = possibleChoices(descramble[i], fhandle)
    fhandle.close()

    if len(possibleWords) == 1:
        print(descramble[i], possibleWords)
    else:
        for word in possibleWords:
            counter = 0
            for j in range(len(word)):
                if word[j] in descramble[i]:
                    counter += 1
                else:
                    break
            if(counter == len(descramble[i])):
                print(descramble[i], [word])
