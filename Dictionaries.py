# phonebookD = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
#   }
#
# print phonebookD['Alice']
# phonebookD ['Adam'] = '777-777-7777'
# print phonebookD


# phonebookD = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
#   }
#
# print phonebookD['Alice']
# phonebookD ['Adam'] = '777-777-7777'
# del phonebookD ['Bob']
# items = phonebookD.items()
# print items

#
#
# ramit = {
#   'name': 'Adam',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
#
#
# print  ramit ['email']
#
# print ramit ['friends'] [1] ['interests'] [1]

##DO NOT USE -------
# words_dict = {}
# word = raw_input('Please enter a word')
# for word in word.split():
#     word = word.replace('a', '3').replace('b', '1').replace('n', '2')
# words_dict[word] = words_dict.get(word, 0) +1
# print word
#------


### letter Summary

# word = raw_input('Please enter in a word! ').lower()
# emptyDictionary = {}
# def wordCount(word):
#     for char in word:
#         if char in emptyDictionary:
#             emptyDictionary[char] += 1
#         else:
#             emptyDictionary[char] = 1
#     print emptyDictionary
#
# wordCount(word)

### Word Summary


# word = raw_input('Please enter in a word! ').lower()
# emptyDictionary = {}
# def wordCount(sentence):
#     for word in word:
#         if char in emptyDictionary:
#             emptyDictionary[char] += 1
#         else:
#             emptyDictionary[char] = 1
#     print emptyDictionary
#
# wordCount(word)
#

word = raw_input('enter a word')
emptyDictionary = {}
def letterCount(word):
    for char in word:
        if char in emptyDictionary:
            emptyDictionary[char] += 1
        else:
            emptyDictionary[char] = 1
    print emptyDictionary
