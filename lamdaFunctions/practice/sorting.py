persons = [
    {
        "name": 'Wajid',
        "age": 26
    },
    {
        "name": 'Affan',
        "age": 25
    },
    {
        "name": 'Ahmad',
        "age": 26
    },
    {
        "name": 'Prankster',
        "age": 27
    },

]

sortedList = sorted(persons, key=lambda x: x['name'])
sortedList = sorted(sortedList, key=lambda x: x['age'])
print(list(sortedList))