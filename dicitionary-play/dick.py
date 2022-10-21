names = ["mac", "john", "dave"]
ages = [44,23,47]

person = {}

for key in names:
    for value in ages:
        person[key] = value
        ages.remove(value)
        break


print(person)