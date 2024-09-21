# ANAGRAMS

def python_anagrams(anagrams):
    anagram_dict = {}
    for word in anagrams:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
        else:
            anagram_dict[sorted_word] = 1
    return max(anagram_dict.values())
anagrams = ['listen', 'enlist', 'silent', 'inlets', 'banana']
print(python_anagrams(anagrams))