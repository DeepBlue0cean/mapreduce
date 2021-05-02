from mrjob.job import MRJob
from mrjob.step import MRStep


class MRSpendByCustomerSorted(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_customer,
                   reducer=self.reducer_count_order_amount),
            MRStep(mapper=self.mapper_make_order_amount_key,
                   reducer=self.reducer_output_results)
        ]

    def mapper_get_customer(self, _, line):
        (customer_id, item_id, order_amount) = line.split(',')
        yield customer_id, float(order_amount)

    def reducer_count_order_amount(self, customer_id, order_amount):
        yield customer_id, sum(order_amount),

    def mapper_make_order_amount_key(self, customer_id, total_amount):
        yield ('%04.02f' % float(total_amount)), customer_id

    def reducer_output_results(self, total_amount, customers):
        for customer in customers:
            yield customer, total_amount


if __name__ == '__main__':
    MRSpendByCustomerSorted.run()
