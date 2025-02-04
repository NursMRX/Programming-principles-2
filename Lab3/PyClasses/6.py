class PrimeNumberFilter:
    def __init__(self):
        self.numbers = []
    def get_user_numbers(self):
        input_numbers = input()
        self.numbers = list(map(int, input_numbers.split()))
    def IsPrime(self, num):
        if num < 2:
            return False
        for i in range(2, int((num)**0.5)+1):
            if num % i == 0:
                return False
        return True
    def filter_prime_numbers(self):
        prime_numbers = list(filter(lambda x: self.IsPrime(x), self.numbers))
        return prime_numbers
prime_filter = PrimeNumberFilter()
prime_filter.get_user_numbers()
print(f"Все простые числа из списка: {prime_filter.filter_prime_numbers()}")