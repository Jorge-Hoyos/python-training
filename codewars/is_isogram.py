def my_solution (word):
    flag = True
    word = word.lower()
    for index,letter in enumerate(word):
        for next_letter in word[index+1:]:
            print ("is {0} equals {1}".format(letter, next_letter))
            if letter == next_letter:
                flag = False
                break
    return flag

def is_isogram(string):
  # Set creates a array with non duplicates
    return len(string) == len(set(string.lower()))