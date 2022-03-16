import random

def get_word(wordfile="/usr/share/dict/words"):
    good_words = []
    with open(wordfile) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) >=5:
                good_words.append(i)
    return random.choice(good_words)

def mask_word(secret_word,guesses):
    op=[]
    for i in secret_word:
        if i in guesses:
            op.append(i)
        else:
            op.append("-")
    return "".join(op)