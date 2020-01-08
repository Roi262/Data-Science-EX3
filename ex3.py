import viz
from collections import defaultdict
import matplotlib.pyplot as plt
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import *
# import tqdm
from tqdm import tqdm

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


# def common_words(use_stopwords=False):
#     with open("Karamazov.txt") as f:
#         words_counter = defaultdict(int)
#         for line in f:
#             line = line.replace("{", " ").replace(", ", " ").replace(". ", " ")
#             for word in line.split():
#                 if word.isspace():
#                     continue
#                 if use_stopwords:
#                     if word not in STOPWORDS:
#                         words_counter[word] += 1
#                 if not use_stopwords:
#                     words_counter[word] += 1
#         viz.dict_to_bar_graph(words_counter, WORD_COUNT)


def count_tokens(tokens: list) -> dict:
    token_count = defaultdict(int)
    for word in tokens:
        token_count[word] += 1
    return token_count
    

def b():
    with open("Karamazov.txt") as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = line.replace("{", " ").replace(", ", " ").replace(". ", " ")
            line_words = line.split()
            words += line_words
        words_count = count_tokens(words)
        viz.dict_to_bar_graph(words_count, WORD_COUNT, "4.b")


def c():
    with open("Karamazov.txt") as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = line.replace("{", " ").replace(", ", " ").replace(". ", " ")
            line_words = line.split()
            words += line_words
        words = list(filter(lambda word: word not in STOPWORDS, words))
        words_count = count_tokens(words)
        viz.dict_to_bar_graph(words_count, WORD_COUNT, "4.c")


def d() -> None:
    stemmer = PorterStemmer()
    with open("Karamazov.txt") as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = line.replace("{", " ").replace(", ", " ").replace(". ", " ")
            line_words = line.split()
            words += line_words
        words = list(map(lambda word: stemmer.stem(word), words))
        stemmed = [stemmer.stem(word) for word in words]
        words_count = count_tokens(stemmed)
        viz.dict_to_bar_graph(words_count, WORD_COUNT, "4.d")

def is_noun(tag):
    return tag.startswith("NN")


def is_adj(tag):
    return tag.startswith("JJ")


def e(text):
    '''Call e with the full txt'''
    tokenized = nltk.pos_tag(nltk.tokenize.word_tokenize(text))
    out = []
    i = 0
    while i < len(tokenized):
        # print('in while')
        word, tag = tokenized[i]
        if is_adj(tag):
            new = word
            i += 1
            if i == len(tokenized):
                break
            word, tag = tokenized[i]
            while is_adj(tag):
                new = new + " " + word
                i += 1
                if i == len(tokenized):
                    break
                word, tag = tokenized[i]
            if is_noun(tag):
                new = new + " " + word
                i += 1
                if i == len(tokenized):
                    break
                word, tag = tokenized[i]
                while is_noun(tag):
                    new = new + " " + word
                    i += 1
                    if i == len(tokenized):
                        break
                    word, tag = tokenized[i]
                out.append(new)
        else:
            i += 1
    return out

def count_adj_noun_phrases():
    with open("Karamazov.txt") as f:
    # with open("mini_karamazov.txt") as f:
        tokens = e(f.read())
        tokens_count = count_tokens(tokens)
        viz.dict_to_bar_graph(tokens_count, WORD_COUNT, "count of adj+noun phrases")

if __name__ == "__main__":
    # b()
    # c()
    # d()
    count_adj_noun_phrases()

