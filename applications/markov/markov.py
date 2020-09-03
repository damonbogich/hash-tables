import random


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    word_list = words.split()
    # print(word_list)
    word_dict = {}
    start_words = []
    end_words = []

    #keep track of end and beginning words
    end_word_punctuation = ['.', '?', '!']

    #create dictionary:
    #loop through word_list
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = []
        if word[0].isupper():
            start_words.append(word)
        if word[-1] in end_word_punctuation:
            end_words.append(word)
        if len(word) > 1:
            if word[-2] in end_word_punctuation and word[-1] == ' " ':  #need a loook at why this isn't working -- the words that end with punctuation then " aren't in the list
                end_words.append(word)

    
    #loop through words list and add the word after each word to that words list in dict
    for word in range(len(word_list) - 1):
        word_dict[word_list[word]].append(word_list[word + 1])
    # print(word_dict)

    for i in range(5):
        #create 5 random sentences:
        
        #1. choose random start word
        random_start_word = random.choice(start_words)
        print(random_start_word, end=" ")
        #2. pick a random word from it's list of words
        current = random_start_word
        #while loop
        running = True
        while running is True:
            random_follow_word = random.choice(word_dict[current])
            print(random_follow_word, end= " ")
                #if that word is a stop word, end the sentence
            if random_follow_word in end_words:
                running = False
            else:
                current = random_follow_word

            #else pick a word from that words list and repeat till there's a stop word printed

    



