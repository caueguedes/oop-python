from collections import defaultdict
from collections import Counter


def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


def letter_frequency_default(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


def letter_frequency_counter(sentence):
    return Counter(sentence)


num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])


d = defaultdict(tuple_counter)
d['a'][1].append("hello")
d['b'][1].append('world')
d  # defaultdict(<function tuple_counter at 0x82f2c6c>, {'a': (1, ['hello']), 'b': (2, ['world'])})


responses = [
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla"
]

print(
    "The children voted for {} ice cream".format(
        Counter(responses).most_common(1)[0][0]
    )
)
