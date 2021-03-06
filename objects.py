# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
#     def greet(self, other_person):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
#
#
# class

def isWhiteSpace(character):
    return character == ' ' or character == '\n'

def slice(sentence):
    words = []
    beginningOfWord = 0
    currentCharacter = 0
    for character in sentence:
        if isWhiteSpace(character):
            word = (sentence[beginningOfWord:currentCharacter])
            words.append(word.lower())
            beginningOfWord = currentCharacter + 1
        currentCharacter += 1
    return words

def countWords(sentence):
    wordCount = {}
    words = slice(sentence)
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    print wordCount

countWords("hello this is my Sentence sentence is my word hello")
