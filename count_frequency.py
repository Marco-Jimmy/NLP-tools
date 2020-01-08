# coding: utf-8

import jieba.posseg
from collections import Counter

ENCODE = 'utf-8'


def load_stop_words(path):
    """
    Input:    The path to stopwords file (txt)
    Return:   A list of stopwords
    Function: Read the stopwords from a txt file and convert them into a list.
    """
    with open(path, 'r', encoding=ENCODE) as f:
        stop_words = f.readlines()
        stop_words = [word.strip() for word in stop_words]  # strip the line break
    stop_words.append('\n')
    return stop_words


def sentences2words(sents):
    """
    Input:    A string (sentences)
    Return:   A list of pairs of (word, tag)
    Function: Cut the sents into words and assign tags accordingly by jieba.posseg.
    """
    pair_list = jieba.posseg.cut(sents)
    return pair_list


def rm_stop_words(pair_list, stopwords):
    """
    Input:    A list of pairs of (word, tag), a list of stopwords
    Return:   A list of strings (word)
    Function: Remove the unnecessary word according to stopwords.
    """
    exclude_tags = {'m', 'f', 'x', 'd'}
    final_word_list = []
    for word, tag in pair_list:
        if tag not in exclude_tags:
            if word not in stopwords:
                final_word_list.append(word)
    return final_word_list


def word_freq_stat(sentences, limit):
    """
    Input:      A string (sentences), An int (limit)
    Return:     A dictionary (freq_rank)
    Function:   Count the frequently used words of given text and print the rank of the first <limit> of them.
    """
    # Load the stop words from local path.
    # the 'stopwords.txt' is provided by ltp.
    stopwords = load_stop_words('stopwords.txt')
    # Convert the sentences to words.
    words_tags = sentences2words(sentences)
    # Remove the stop words.
    word_list = rm_stop_words(words_tags, stopwords)
    # Count the frequency of each word.
    words_freq = Counter(word_list)
    # Sort the frequency and list <limit> most frequent words
    freq_rank = words_freq.most_common(limit)
    for i in range(limit):
        print("{}\t{}".format(freq_rank[i][1], freq_rank[i][0]))
    return freq_rank


if __name__ == '__main__':
    with open('example_text.txt', 'r', encoding=ENCODE) as f:
        example = f.read()
    word_freq_stat(example, 20)
