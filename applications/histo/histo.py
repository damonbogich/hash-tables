# Your code here

def histogram(file):
    pass

with open("robin.txt") as f:
    words = f.read()

    ignore = ['"', ":", ";", ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    word_count_dict = {}
    
    word_list = words.split()
    # print(word_list)
    for word in word_list:
        word = word.lower()
        if word[-1] in ignore:
            word = word[:-1]
        if word not in word_count_dict:
            word_count_dict[word] = 1
        if word in word_count_dict:
            word_count_dict[word] += 1
    # print(word_count_dict)

    #now we need find the length of longest word in word_list
    
    current = 0
    
    for word in word_list:
        if len(word) > current:
            current = len(word)

    longest_word_length = current
    print(longest_word_length)  #16

    #neeed to create a dictionary where the count of each word is translated to hash_marks
    #order of dictionary should be most to least hashmarks, then alphabetically
    for key in word_count_dict:
        word_count_dict[key] = word_count_dict[key] * "#"
    

    word_count_dict = {k: v for k, v in sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)}
    # word_count_dict = [v[0] for v in sorted(word_count_dict.items(), key=lambda kv: (kv[1], kv[0]))]
    print(word_count_dict)


