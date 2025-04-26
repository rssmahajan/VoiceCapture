from word2number import w2n

def normalize_numbers(text):
    words = text.split()
    new_words = []
    for word in words:
        try:
            number = w2n.word_to_num(word)
            new_words.append(str(number))
        except:
            new_words.append(word)
    return ' '.join(new_words)
