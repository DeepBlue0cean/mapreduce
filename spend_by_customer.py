from mrjob.job import MRJob


class MRSpendByCustomer(MRJob):
    def mapper(self, _, line):
        (customer_id, item, order_amount) = line.split(",")
        yield customer_id, float(order_amount)

    def reducer(self, customer, order_amount):
        yield customer, round(sum(order_amount),2)


if __name__ == '__main__':
    MRSpendByCustomer.run()
