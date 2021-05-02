import re

from mrjob.job import MRJob
from mrjob.step import MRStep

WORD_REGEXP = re.compile(r"[\w']+")


class MRWordFrequencyCounter(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_word,
                   reducer=self.reducer_count_word),
            MRStep(mapper=self.mapper_make_counts_key,
                   reducer=self.reducer_output_word)
        ]

    def mapper_get_word(self, _, line):
        words = WORD_REGEXP.findall(line)
        for word in words:
            yield word, 1

    def reducer_count_word(self, word, frequency):
        yield word, sum(frequency)

    def mapper_make_counts_key(self, word, count):
        yield '%04d' % int(count), word

    def reducer_output_word(self, count, words):
        for word in words:
            yield word, count


if __name__ == '__main__':
    MRWordFrequencyCounter.run()
