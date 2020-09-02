
ignore = ['"', ":", ";", ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def word_count(s):
    #counter to make sure ignored character is in string
    count = 0

    word_count_dictionary = {}

    #loop through all ignore characters, replace them with blank space, and count how many there are
    for character in ignore:
        if character in s:
            s = s.replace(character, "")
            count += 1
    # if count == 0:
    #     return {}   I think that the readme had the directions wrong for this one
    
    
    #make list containing each word in string, make them all lowercase
    string_word_list = s.lower().split()

    #loop through string word list to make every word dictionary key
    for word in string_word_list:
        word_count_dictionary[word] = 0
    print(word_count_dictionary)
    
    for word in string_word_list:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
    
    return word_count_dictionary
    


    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))