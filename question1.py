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

n = get_number() # number of words, from the standard input, you see that you have to start with a number

def python_anagrams(anagrams):
    anagram_dict = {} # TODO: why dictionary?
    for word in anagrams:
        sorted_word = ''.join(sorted(word)) # TODO: why join? and why sorted?
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
        else:
            anagram_dict[sorted_word] = 1
    return max(anagram_dict.values()) # TODO: why max? and why .values()?
print(python_anagrams([get_word() for _ in range(n)])) # TODO: why [get_word() for _ in range(n)]?

# WE END OUR CODE HERE