import viz
from collections import defaultdict
import matplotlib.pyplot as plt
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import *
import wordcloud
from tqdm import tqdm

STOPWORDS = set(stopwords.words('english'))
WORD_COUNT = 20
BOOK_PATH = 'Karamazov.txt'
# MINI_BOOK_PATH = 'mini_karamazov.txt'


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
        words = list(filter(lambda word: word not in STOPWORDS, words))
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
        tokens = e(f.read())
        tokens_count = count_tokens(tokens)
        viz.dict_to_bar_graph(tokens_count, WORD_COUNT,
                              "count of adj+noun phrases")


def get_proper_nouns(book_file):
    text = book_file.read()
    tokenized = nltk.pos_tag(nltk.tokenize.word_tokenize(text))
    proper_nouns = ''
    for word, tag in tokenized:
        if tag.startswith("NNP") or tag.startswith("NNPS"):
            proper_nouns += word + " "
    return proper_nouns


def h(book_file):
    proper_nouns_text = get_proper_nouns(book_file)
    cloud = wordcloud.WordCloud(collocations=False).generate(proper_nouns_text)
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    # b()
    # c()
    # d()
    count_adj_noun_phrases()
    # with open(BOOK_PATH) as f:
    #     h(f)
