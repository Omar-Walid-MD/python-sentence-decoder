import dict

def main():
    words_dict = dict.get_dict()
    key = int(input("Enter Key: "))
    shuffled_dict = dict.get_shuffled_dict(words_dict,key)

    def trim_word(word):
        while not word[-1].isalpha():
            word = word[:-1]
        while not word[0].isalpha():
            word = word[1:]
        return word

    def encode():
        sentence = input("Encode sentence: ").lower().split(" ")
        output = []
        for word in sentence:
            word = trim_word(word)
            if words_dict.get(word[0],False) is not False:
                try:
                    i = words_dict[word[0]].index(word)
                    output.append(shuffled_dict[word[0]][i])
                except ValueError:
                    for letter in word:
                        if letter.isalpha():
                            i = words_dict[letter].index(letter)
                            output.append(shuffled_dict[letter][i])
        print(" ".join(output))

    def decode():
        sentence = input("Decode sentence: ").lower().split(" ")
        output = []
        for word in sentence:
            word = trim_word(word)
            if words_dict.get(word[0],False) is not False:
                try:
                    i = shuffled_dict[word[0]].index(word)
                    output.append(words_dict[word[0]][i])
                except ValueError:
                    continue
        print(" ".join(output))

    while True:

        m = ""
        while m!="e" and m!="d" and m!="c":
            m = input("Encode (e), Decode (d), Close (c): ").lower()

        if m=="c":
            break
        elif m=="e":
            encode()
        elif m=="d":
            decode()


if __name__=="__main__":
    main()