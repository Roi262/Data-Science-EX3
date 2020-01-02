import viz
from collections import defaultdict
import matplotlib.pyplot as plt
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords


STOPWORDS = set(stopwords.words('english'))
WORD_COUNT = 20

# def common_characters():
#     with open("data\\HPMovies\\HP1.csv") as f:
#         speaker_counter = defaultdict(int)
#         major_speakers_counter = defaultdict(int)
#         for line in f:
#             speaker = line.split(",")[0]
#             speaker_counter[speaker] += 1
#         viz.dict_to_bar_graph(dict, MAJOR_CHAR_COUNT)



def common_words(use_stopwords=False):
    with open("Karamazov.txt") as f:
        words_counter = defaultdict(int)
        for line in f:
            line = line.replace("{", " ").replace(", ", " ").replace(". ", " ")
            for word in line.split(" "):
                if word.isspace(): 
                    continue
                if use_stopwords:
                    if word not in STOPWORDS:
                        words_counter[word] += 1
                if not use_stopwords:
                    words_counter[word] += 1
        viz.dict_to_bar_graph(words_counter, WORD_COUNT)

# a
common_words()
# b
common_words(True)