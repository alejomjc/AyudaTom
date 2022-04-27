import random
import threading
import time

from sympy import isprime


class StructWS:
    max_number = 0
    min_number = 0
    first_number = 0
    last_number = 0
    number_of_prime_numbers = 0
    number_of_even_numbers = 0
    number_of_odd_numbers = 0

    def __init__(self):
        self.max_number = 0
        self.min_number = 0
        self.first_number = 0
        self.last_number = 0
        self.number_of_prime_numbers = 0
        self.number_of_even_numbers = 0
        self.number_of_odd_numbers = 0

    def set_max_number(self, number):
        self.max_number = number

    def get_max_number(self):
        return self.max_number

    def set_min_number(self, number):
        self.min_number = number

    def get_min_number(self):
        return self.min_number

    def set_first_number(self, number):
        self.first_number = number

    def get_first_number(self):
        return self.first_number

    def set_last_number(self, number):
        self.last_number = number

    def get_last_number(self):
        return self.last_number

    def set_number_of_prime_numbers(self, number):
        self.number_of_prime_numbers = number

    def get_number_of_prime_numbers(self):
        return self.number_of_prime_numbers

    def set_number_of_even_numbers(self, number):
        self.number_of_even_numbers = number

    def get_number_of_even_numbers(self):
        return self.number_of_even_numbers

    def set_number_of_odd_numbers(self, number):
        self.number_of_odd_numbers = number

    def get_number_of_odd_numbers(self):
        return self.number_of_odd_numbers

    def get_all_data(self):
        return {"max_number":  self.get_max_number(),
                "min_number": self.get_min_number(),
                "first_number": self.get_first_number(),
                "last_number": self.get_last_number(),
                "number_of_prime_numbers": self.get_number_of_prime_numbers(),
                "number_of_even_numbers": self.get_number_of_even_numbers(),
                "number_of_odd_numbers": self.get_number_of_odd_numbers()
                }


def proyecto():
    while True:
        struct_ws = StructWS()
        a = 1
        while a <= 100:
            b = random.randint(0, 2**32)
            if b > struct_ws.get_max_number():
                struct_ws.set_max_number(b)
            if b < struct_ws.get_min_number():
                struct_ws.set_min_number(b)
            if a == 1:
                struct_ws.set_min_number(b)
            if a == 100:
                struct_ws.set_max_number(b)
            if isprime(b):
                struct_ws.set_number_of_prime_numbers(struct_ws.get_number_of_prime_numbers() + 1)
            if b % 2 == 0:
                struct_ws.set_number_of_even_numbers(struct_ws.get_number_of_even_numbers() + 1)
            if b % 2 != 0:
                struct_ws.set_number_of_odd_numbers(struct_ws.get_number_of_odd_numbers() + 1)
            a += 1

        print(struct_ws.get_all_data())
        time.sleep(60)


if __name__ == '__main__':
    t = threading.Thread(target=proyecto)
    t.start()
