import matplotlib.pyplot as plt
from collections import defaultdict


def trim_dict(my_dict, threshold):
    new_dict = defaultdict(int)
    for v in my_dict:
        if my_dict[v] > threshold:
            new_dict[v] = my_dict[v]
    return new_dict


def dict_to_bar_graph(my_dict, num_of_words_to_show, head=0):
    if head > 0:
        my_dict = trim_dict(my_dict, head)
    if num_of_words_to_show > len(my_dict):
        num_of_words_to_show = len(my_dict)

    my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
    plt.bar(range(num_of_words_to_show), list(my_dict.values())[:num_of_words_to_show], align='center')
    plt.xticks(range(num_of_words_to_show), list(my_dict.keys())[:num_of_words_to_show], rotation=70)
    plt.show()

