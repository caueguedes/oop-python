class Average(list):
    @property
    def average(self):
        return sum(self) / len(self)


average = Average([1, 2, 3, 4])
average.average  # 2.5
