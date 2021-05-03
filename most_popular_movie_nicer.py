from mrjob.job import MRJob
from mrjob.step import MRStep


class MRMostPopularMovie(MRJob):

    def configure_args(self):
        super(MRMostPopularMovie, self).configure_args()
        self.add_file_arg('--items', help='Path to u.item')

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer_init=self.reducer_init,
                   reducer=self.reducer_count_ratings),

            MRStep(mapper=self.mapper_passthrough,
                   reducer=self.reducer_find_max)
        ]

    def mapper_get_ratings(self, _, line):
        (user_id, movie_id, rating, timestamp) = line.split("\t")
        yield movie_id, 1

        # This mapper does nothing; it's just here to avoid a bug in some
        # versions of mrjob related to "non-script steps." Normally this
        # wouldn't be needed.

    def mapper_passthrough(self, key, value):
        yield key, value

    def reducer_init(self):
        self.movie_names = {}
        with open("u.item") as data:
            for line in data:
                feilds = line.split('|')
                self.movie_names[feilds[0]] = feilds[1]

    def reducer_count_ratings(self, movie_id, view):
        yield None, (sum(view), self.movie_names[movie_id])

    def reducer_find_max(self, key, views):
        yield max(views)


if __name__ == '__main__':
    MRMostPopularMovie.run()
