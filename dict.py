import time
import json
import random
import copy



def get_dict():
    words_dict = {}

    with open("words.json") as words_file:
        words_dict = json.load(words_file)

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
