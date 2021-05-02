import re

from mrjob.job import MRJob

WORD_REGEXP = re.compile(r"[\w']+")


class MRWordFrequency(MRJob):
    def mapper(self, _, line):
        words = WORD_REGEXP.findall(line)
        # words = line.split()
        # my_word = ["I", "love", "you"]
        for word in words:
            # if word.lower() in (test.lower() for test in my_word):
                yield word.lower(), 1

    def reducer(self, word, frequency):
        yield word, sum(frequency)


if __name__ == '__main__':
    MRWordFrequency.run()
