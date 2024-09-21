# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# WE START OUR CODE HERE

number_of_words = get_number() # number of words, from the standard input, you see that you have to start with a number
def get_letters(words):
    letters = []
    for word in words:
        get_letter = sorted(word)[0] # TODO: you remember sorted() we talked about in question1.py? why are we adding [0]? alt for this? 
        letters.append(get_letter)
    letters = ''.join(sorted(letters)) # TODO: sort again? why?
    return letters
print(get_letters([get_word() for _ in range(number_of_words)]))  # we talked about this in the first question

# WE END OUR CODE HERE