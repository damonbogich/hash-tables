def no_dups(s):
    word_dict = {}

    string_list = s.split()

    for i in string_list:
        word_dict[i] = None
    
    removed_dups = "".join(f"{key} " for key, value in word_dict.items())

    removed_dups = removed_dups[:-1]

    return removed_dups



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))