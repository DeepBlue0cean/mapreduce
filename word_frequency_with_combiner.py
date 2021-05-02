import re

from mrjob.job import MRJob

WORD_REGEXP = re.compile(r"[\w']+")


class MRWordFrequencyWithCombiner(MRJob):
    def mapper(self, _, line):
        words = WORD_REGEXP.findall(line)
        for word in words:
            yield word.lower(), 1

    def combiner(self, word, frequency):
        yield word, sum(frequency)

    def reducer(self, word, frequency):
        yield word, sum(frequency)


if __name__ == '__main__':
    MRWordFrequencyWithCombiner.run()
