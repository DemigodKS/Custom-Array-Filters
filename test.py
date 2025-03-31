#6kyu

class Filter:
    def __init__(self, total: int):
        self.list_of_numbers = []
        self.total = total

    def add_numbers(self) -> list:

        for i in range(1, self.total+1):
            n = int(input('Введите число: '))
            self.list_of_numbers.append(n)
        return self.list_of_numbers

    def even(self):
        for i in self.list_of_numbers:
            if i % 2 != 0:
               self.list_of_numbers.remove(i)
        return self.list_of_numbers


    def odd(self):
        for i in self.list_of_numbers:
            if i % 2 == 0:
               self.list_of_numbers.remove(i)
        return self.list_of_numbers


    def under(self, number):
        index_number = self.list_of_numbers.index(number)
        return self.list_of_numbers[:index_number]

    def over(self, number):
        index_number = self.list_of_numbers.index(number)
        return self.list_of_numbers[index_number+1:]

    def in_range(self, start, stop):
        index_start = self.list_of_numbers.index(start)
        index_stop = self.list_of_numbers.index(stop)
        return self.list_of_numbers[index_start:index_stop+1]




dd = Filter(5)
print(dd.add_numbers())
#print(dd.even())
#print(dd.odd())
#print(dd.under(17))
#print(dd.over(16))
#print(dd.in_range(2, 14))
