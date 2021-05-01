from mrjob.job import MRJob


class MRFiendsByAge(MRJob):
    def mapper(self, _, line):
        (id, name, age, number_of_friends) = line.split(",")
        yield age, float(number_of_friends)

    def reducer(self, age, number_of_friends):
        total = 0
        number_elements = 0
        for x in number_of_friends:
            total += x
            number_elements += 1

        yield age, total / number_elements


if __name__ == '__main__':
    MRFiendsByAge.run()

# python RatingCounter.py data\fakefriends.csv >> friends_by_age.txt
