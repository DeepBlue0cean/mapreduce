from mrjob.job import MRJob


class MRMaxTemperatures(MRJob):

    def make_fahrenheit(self, tenths_of_celsius):
        celsius = float(tenths_of_celsius) / 10.0
        fahrenheit = celsius * 1.8 + 32.0
        return fahrenheit

    def mapper(self, key, line):
        (location, date, type, data, x, y, z, w) = line.split(",")
        if type == 'TMAX':
            temperature = self.make_fahrenheit(data)
            yield location, temperature

    def reducer(self, location, temperature):
        yield location, max(temperature)


if __name__ == '__main__':
    MRMaxTemperatures.run()
