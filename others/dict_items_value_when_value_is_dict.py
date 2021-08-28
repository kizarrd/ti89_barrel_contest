a_dict = { "203232_2019": {'b1': 1, 'b2': 34, 'hr': 354},  "203232_2018": {'b1': 71, 'b2': 3, 'hr': 42}}

for key in a_dict.keys():
    print(key, end=' ')
    for value in a_dict[key].values():
        print(value, end=' ')
    print()