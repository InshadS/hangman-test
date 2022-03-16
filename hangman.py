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

def create_status(secret_word, guesses, remaining_turns):
    masked_word = mask_word(secret_word, guesses)
    guesses = " ".join(guesses)
    return f"""Word: {masked_word}
    Guesses: {guesses}
    Remaining turns : {remaining_turns}
    """

def play(secret_word, guesses, guess, remaining_turns):
    if "-" not in mask_word(secret_word, guesses+[guess]):
        return remaining_turns, False, True
    if guess in guesses:
        return remaining_turns, True, False
    if guess in secret_word:
        guesses.append(guess)
        return remaining_turns, False, False
    if guess not in secret_word:
        guesses.append(guess)
        return remaining_turns-1, False, False

def main():
    secret_word = get_word()
    print(secret_word)
    remaining_turns = 8
    guesses = []
    while True:
        status = create_status(secret_word, guesses, remaining_turns)
        print(status)
        guess = input("Enter a letter ").strip()
        remaining_turns, repeat, finished = play(
            secret_word, guesses, guess, remaining_turns)
        if finished:
            print(f"You found the secret word '{secret_word}'")
            break
        if remaining_turns == 0:
            print(f"You failed. The secret word was {secret_word}")
            break
        elif repeat:
            print(f"You already guessed '{guess}'")


if __name__ == "__main__":
    main()