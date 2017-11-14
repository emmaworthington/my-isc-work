# list ranges

one_to_ten = range(1, 11)
print one_to_ten

one_to_ten[0] = 10
print one_to_ten

one_to_ten.append(11)
print one_to_ten

twelve_to_fourteen = [12, 13, 14]

one_to_ten.extend(twelve_to_fourteen)
print one_to_ten
