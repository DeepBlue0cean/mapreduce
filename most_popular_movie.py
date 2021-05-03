from mrjob.job import MRJob
from mrjob.step import MRStep


class MRMostPopularMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_find_max)
        ]

    def mapper_get_ratings(self, _, line):
        (user_id, movie_id, rating, timestamp) = line.split("\t")
        yield movie_id, 1

    def reducer_count_ratings(self, movie_id, view):
        yield None, (sum(view), movie_id)

    def reducer_find_max(self, key, views):
        yield max(views)


if __name__ == '__main__':
    MRMostPopularMovie.run()
