def translation(given_word):
    if given_word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return given_word + "way"
    else:
        return given_word[1:] + given_word[0] + "ay"


word = raw_input("enter a english word: ")
print word
print translation(word)
