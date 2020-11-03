def check_vowel(c):
    c = c.lower()
    vowels = 'aoeiu'
    if c in vowels:
        return True
    else:
        return False

# def disemvowel(string):
#     i = 0
#     while i < len(string):
#         if check_vowel(string[i]):
#             string = string[:i] + string[i+1:]
#         else:
#             i += 1
#     return string


def disemvowel(string):
    vowels = 'aoeiuAOEIU'
    for c in vowels:
        string = string.replace(c, '')
    return string


print(disemvowel('This website is for losers LOL!'))
