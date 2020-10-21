input_strings = ["1","5", "28", "131", "3"]

output_integers = []
for num in input_strings:
    output_integers.append(int(num))

# is the same as above code
output_comprehensions = [int(num) for num in input_strings]
output_filtered = [int(num) for num in input_strings if len(num) < 3]
