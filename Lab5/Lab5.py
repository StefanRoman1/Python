import utils
import app

def my_function(*args, **kwargs):
    return sum(kwargs.values())

my_anonymus_function = lambda *args, **kwargs: sum(kwargs.values())

def is_vowel(letter):
    return letter.lower() in "aeiou"

def exercise3_function(text):
    vowels = []
    for letter in text:
        if is_vowel(letter):
            vowels.append(letter)
    return vowels

exercise3_anonymus_function = lambda text: [letter for letter in text if is_vowel(letter)]

def exercise4_function(*args, **kwargs):
    aux = []
    for arg in args:
        if type(arg) is dict and len(arg) >= 2 and any([type(key) is str and len(key) >= 3 for key in arg.keys()]):
            aux.append(arg)
    for key, value in kwargs.items():
        if type(value) is dict and len(value) >= 2 and any([type(key) is str and len(key) >= 3 for key in value.keys()]):
            aux.append(value)
    return aux

def exercise5(list) :
    return [number for number in list if type(number) is int or type(number) is float]

def exercise6(list) :
    even = []
    odd = []
    for number in list:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    pairs = []
    for i in range(len(even)):
        pairs.append((even[i], odd[i]))
    return pairs

def exercise9(pairs):
    return [{ "sum": pair[0] + pair[1], "prod": pair[0] * pair[1], "pow": pair[0] ** pair[1] } for pair in pairs]

#print(my_function(1, 2, c = 3, d = 4))
#print(my_anonymus_function(1, 2, c = 3, d = 4))

#print(exercise3_function("Programming in Python is fun"))
#print(exercise3_anonymus_function("Programming in Python is fun"))
#print([letter for letter in "Programming in Python is fun" if is_vowel(letter)])
#print(list(filter(is_vowel, "Programming in Python is fun")))

#print(exercise4_function({1: 2, 3: 4, 5: 6},{'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3],{'abc': 4, 'def': 5},3764,dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},test={1: 1, 'test': True}))

#print(exercise5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

#print(exercise6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

print(exercise9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] ))

