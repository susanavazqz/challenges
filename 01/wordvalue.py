from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    dictionary_object = open(DICTIONARY, 'r')
    list = [w.strip() for w in dictionary_object.readlines()]

    return list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)

def max_word_value(list_words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    ret = {'word': '', 'sum': 0}
    if not list_words:
        list_words = load_words()

    for word in list_words:
        sum = calc_word_value(word)
        if sum > ret['sum']:
            ret['word'] = word
            ret['sum'] = sum

    return ret['word']

if __name__ == "__main__":
    pass # run unittests to validate
