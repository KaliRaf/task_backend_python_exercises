users = [{'name': 'Kamil', 'country': 'Poland'}, {'name': 'John', 'country': 'USA'}, {'name': 'Yeti'}]


def find_polish(users):
    return [user for user in users for data in user.items() if data == ('country', 'Poland')]


numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]


def sum_ten_numbers_after_five(numbers):
    return sum(numbers[numbers.index(5):numbers.index(5) + 10])


def fill_with_powers_of_2(n=20):
    return [2 ** i for i in range(n)]


if __name__ == '__main__':
    print(find_polish(users))
    print(sum_ten_numbers_after_five(numbers))
    print(fill_with_powers_of_2())
