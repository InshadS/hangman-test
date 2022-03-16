import os

import hangman

def test_get_word_no_punctuation():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_no_proper_nouns():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("Noufal\n")
        f.write("John\n")
        f.write("Simon\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_mask_word_single_letter():
    secret_word = "elephant"
    guesses= ["l"]
    ret =hangman.mask_word(secret_word,guesses)
    assert ret == "-l------"

def test_mask_word_mulitple_letter():
    secret_word = "elephant"
    guesses= ["e"]
    ret =hangman.mask_word(secret_word,guesses)
    assert ret == "e-e-----"

def test_mask_word_mix_letter():
    secret_word = "elephant"
    guesses= ["e","l","y"]
    ret =hangman.mask_word(secret_word,guesses)
    assert ret == "ele-----"

def test_create_status_not_guessed():
    secret_word = "elephant"
    guesses = []
    remaining_turns = 8
    status = hangman.create_status(secret_word, guesses, remaining_turns)
    assert status == """Word: --------
    Guesses: 
    Remaining turns : 8
    """
def test_create_status_normal():
    secret_word = "elephant"
    guesses = ["a", "x", "h"]
    remaining_turns = 7
    ret = hangman.create_status(secret_word, guesses, remaining_turns)
    assert ret == """Word: ----ha--
    Guesses: a x h
    Remaining turns : 7
    """