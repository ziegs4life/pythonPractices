# ## Uppercase a String
# Sting = hello
# string.upper
#
# ## Capitalize a String
# sting = adam
# sting.capitalize()
#
# ## Reverse a String
# Adam [::-1]
#
#
## Leetspeak
# def adam(string):
#
#
#     for char in string:
#     	if char == 'a':
#     		string = string.replace('a','4')
#     	elif char == 'e':
#     		string = string.replace('e','3')
#     	elif char == 'g':
#     		string = string.replace('g','6')
#     	elif char == 'l':
#     		string = string.replace('l','1')
#     	elif char == 'o':
#     		string = string.replace('o','0')
#     	elif char == 's':
#     		string = string.replace('s','5')
#     	elif char == 't':
#     		string = string.replace('t','7')
#     	else:
#     		pass
#
#     print(string)
# string = raw_input(' I am translating this message')
# adam(string)
#
#
# ## Long-long Vowels
# string = input('This is expanding vowels')
#
# for char in sting:
#     if car == 'oo':
#         string = string.replace('i','iii')
#     elif car == 'ee':
#         string = string.replace('e','eee')
#     else:
#         pass
#
# print(string)
#
#
# ## Caesar Cipher
# secret = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
# # secret = "hello"
# offset = 13
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# result = ''
#
# for char in secret:
#     ascii_code = ord(char)
#     is_uppercase = ascii_code >= 65 and ascii_code <= 90
#     char = char.lower()
#     if char not in alphabet:
#         new_char = char
#     else:
#         idx = alphabet.find(char)
#         new_idx = idx + offset
#         if new_idx > 25:
#             new_idx = new_idx - 26
#         new_char = alphabet[new_idx]
#         if is_uppercase:
#             new_char = new_char.upper()
#     result += new_char
#
# print result
