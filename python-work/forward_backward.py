# lists and loops

forward = []
backward = []

values = ["a", "b", "c"]

for value in values:
    forward.append(value)
    backward.insert(0, value)

print forward
print backward

forward.reverse()

print forward == backward

