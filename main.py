import dict


words_dict = dict.get_dict()
key = int(input("Enter Key: "))
shuffled_dict = dict.get_shuffled_dict(words_dict,key)

def encode():
    sentence = input("Encode sentence: ").lower().split(" ")
    output = []
    for word in sentence:
        if words_dict.get(word[0],False) is not False:
            i = words_dict[word[0]].index(word)
            output.append(shuffled_dict[word[0]][i])
    print(" ".join(output))

def decode():
    sentence = input("Decode sentence: ").lower().split(" ")
    output = []
    for word in sentence:
        if words_dict.get(word[0],False) is not False:
            i = shuffled_dict[word[0]].index(word)
            output.append(words_dict[word[0]][i])
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


