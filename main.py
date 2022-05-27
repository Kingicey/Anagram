# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    # Check if the length of each word is the same
    if (len(word1) == len(word2)):

        # sort each word
        sortedWord1 = sorted(word1)
        sortedWord2 = sorted(word2)
        # check if the two words have the same letters
        if (sortedWord1 == sortedWord2):
            return True
        else:
            return False
    else:
        return False

    # return True

check = find_anagrams("live", "vile")
print(check)