class Burger:

    def __init__(self, cost_in_cents_per_gram, base_weight_in_grams, base_cost_in_cents):
        self._cost_in_cents_per_gram = cost_in_cents_per_gram
        self._base_weight_in_grams = base_weight_in_grams
        self._base_cost_in_cents = base_cost_in_cents
        self._topppings = []
        self._actual_weight_in_grams = 0

    def get_cost_in_center_per_gram(self):
        return self._cost_in_cents_per_gram

    def get_base_weight_in_grams(self):
        return self._base_weight_in_grams

    def get_base_cost_in_cents(self):
        return self._base_cost_in_cents

    def get_toppings(self):
        # ensure they can't modify the original list, they get a copy
        return self._topppings[:]

    def get_actual_weight_in_grams(self):
        return self._actual_weight_in_grams

    def add_topping(self, topping):
        self._topppings.append(topping)

    def set_actual_weight_in_grams(self, actual_weight_in_grams):
        if 0 <= actual_weight_in_grams <= 1000:
            self._actual_weight_in_grams = actual_weight_in_grams
        else:
            raise ValueError("Invalid weight, must be between 0 and 1000")

    def get_total_cost_in_cents(self):
        cost = self._base_cost_in_cents
        if self._actual_weight_in_grams > self._base_weight_in_grams:
            cost += ( self._actual_weight_in_grams - self._base_weight_in_grams ) * self._cost_in_cents_per_gram
        return cost

# https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def sum_of_prime_values_or_values_in_prime_indexes( some_2d_list ):
    sum_of_values = 0
    current_index = 0

    for row in some_2d_list:
        for value in row:
            if is_prime(value) or is_prime(current_index):
                sum_of_values += value
            current_index += 1


def _recursive_scramble(some_string, new_string, start_index, end_index):
    if start_index < end_index:
        new_string += some_string[start_index]
        new_string += some_string[end_index]
        start_index += 1
        end_index -= 1
        return _recursive_scramble(some_string, new_string, start_index, end_index)
    elif start_index == end_index:
        new_string += some_string[start_index]
        return new_string
    else:
        return new_string


def recursive_scramble(some_string):
    return _recursive_scramble(some_string, "", 0, len(some_string)-1)


def iterative_scramble(some_string):
    new_string = ""
    start_index = 0
    end_index = len(some_string) - 1
    while start_index < end_index:
        new_string += some_string[start_index]
        new_string += some_string[end_index]
        start_index += 1
        end_index -= 1
    if start_index == end_index:
        new_string += some_string[start_index]
    return new_string

print(recursive_scramble("abcdefg"))
print(recursive_scramble("abcdef"))

print(iterative_scramble("abcdefg"))
print(iterative_scramble("abcdef"))