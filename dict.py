import time
import random
import copy



def get_dict():
    words_dict = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]}

    with open("words.txt") as words_file:
        for line in words_file:
            word = line.lower().replace("\n","")
            if len(word):
                l = word[0]
                if words_dict.get(l,False) is not False:
                    words_dict[l].append(word)


    return words_dict

def get_shuffled_dict(dict,key=0):
    dict = copy.deepcopy(dict)
    random.seed(key)
    for l in dict:
        random.shuffle(dict[l])
    return dict

# start_time = time.time()
# words_dict = get_dict()
# shuffled_dict = get_shuffled_dict(words_dict,22)
# print(words_dict==shuffled_dict)
# print("--- %s seconds ---" % (time.time() - start_time))
