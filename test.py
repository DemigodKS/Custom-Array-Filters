#6kyu

#method chaining
class Filter:
    def __init__(self, total: int):
        self.list_of_numbers = []
        self.total = total


    def add_numbers(self) -> list:
        for i in range(1, self.total+1):
            while len(self.list_of_numbers) != self.total:
                n = int(input('Введите число от 1 до 50: '))
                if n > 50:
                    print(f'{n} не в рамках диапазона, введите корректное число')
                else:
                    self.list_of_numbers.append(n)
        print(self.list_of_numbers)
        return self

    def index(self, index_number: int) -> int:
        index_number = self.list_of_numbers.index(index_number)
        return index_number

    #поиск четных
    def even(self) -> list:
       #self.list_of_numbers = [x for x in self.list_of_numbers if x % 2 == 0]
       for x in reversed(self.list_of_numbers):
           if x % 2 != 0:
               self.list_of_numbers.remove(x)
       print(self.list_of_numbers)
       return self

    #поиск нечетных
    def odd(self) -> list:
        for i in reversed(self.list_of_numbers):
            if i % 2 == 0:
               self.list_of_numbers.remove(i)
        print(self.list_of_numbers)
        return self

    #ищем, что идет до элемента
    def under(self, number: int) -> list:
        self.list_of_numbers = self.list_of_numbers[:number]
        print(self.list_of_numbers)
        return self

    #ищем, что идет после элемента
    def over(self, number: int) -> list:

        self.list_of_numbers = self.list_of_numbers[number+1::]
        print(self.list_of_numbers)

        return self

    def in_range(self, start: int, stop: int) -> list:
        index_start = self.list_of_numbers.index(start)
        index_stop = self.list_of_numbers.index(stop)
        self.list_of_numbers = self.list_of_numbers[index_start:index_stop+1]
        print(self.list_of_numbers)
        return self



object = Filter(5)

object.add_numbers()
#object.over(2).even()

#в скобках ставлю индекс
object.under(2).odd()



