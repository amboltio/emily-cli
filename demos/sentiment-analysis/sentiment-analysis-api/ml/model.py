from collections import defaultdict
import pickle
from tqdm import tqdm
import numpy as np

class Model():

    def __init__(self):
        super().__init__()
        self.word_idx_map = {}

        # Probability of a word given a class
        self.p_w = {
            'positive': np.zeros(0),
            'negative': np.zeros(0)
        }

        # Probability of a class
        self.p = {
            'positive': 0,
            'negative': 0
        }

        # Score of the empty review given a class
        self.s_e = {
            'positive': 0,
            'negative': 0
        }

    def fit(self, review_sentiment_pairs):
        review_counts, word_counts = self._count_occurrences(review_sentiment_pairs)
        for c in ['positive', 'negative']:
            self.p[c] = review_counts[c] + sum(review_counts.values())
            self.p_w[c] = self._compute_conditional_probabilities(
                review_counts, word_counts, c
            )

        self.s_e['positive'] = self._empty_score('positive')
        self.s_e['negative'] = self._empty_score('negative')

    def forward(self, words):
        words = self._filter_words(words)
        positive_score = self._score(words, 'positive')
        negative_score = self._score(words, 'negative')
        return positive_score, negative_score

    def save_model(self, save_path):
        with open(save_path, 'wb') as fp:
            pickle.dump(self, fp)

    def load_model(self, model_path):
        with open(model_path, 'rb') as fp:
            model = pickle.load(fp)
            self.__dict__.update(model.__dict__)


    def _idx_vector(self, words):
        return [self.word_idx_map[word] for word in words]

    def _empty_score(self, c):
        return np.log(self.p[c]) + np.sum(np.log(1 - self.p_w[c]))

    def _score(self, words, c):
        i = self._idx_vector(words)

        return np.exp(self.s_e[c]) + np.exp(np.sum(np.log(
            self.p_w[c][i] / (1 - self.p_w[c][i]))
        ))

    def _filter_words(self, words):
        return set(words).intersection(set(self.word_idx_map.keys()))

    def _count_occurrences(self, review_sentiment_pairs):
        i = 0
        review_counts = {
            'positive': 0,
            'negative': 0
        }
        word_counts = {
            'positive': defaultdict(int),
            'negative': defaultdict(int)
        }
        for words, sentiment in tqdm(review_sentiment_pairs, '[Counting...]'):
            review_counts[sentiment] += 1
            for word in set(words):
                word_counts[sentiment][word] += 1
                if word not in self.word_idx_map:
                    self.word_idx_map[word] = i
                    i += 1

        return review_counts, word_counts

    def _compute_conditional_probabilities(self, review_counts, word_counts, c):
        vocab_size = len(self.word_idx_map)
        p_w = np.zeros(vocab_size)
        for word, n in tqdm(word_counts[c].items(), f'[Calculating {c} probabilities...]'):
            i = self.word_idx_map[word]
            p_w[i] = n / review_counts[c]

        return p_w

    def __call__(self, sample):
        return self.forward(sample)
