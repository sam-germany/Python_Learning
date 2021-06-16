def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    return RuntimeError(f"{expected}")

friends =[
    {"name": "aaa", "age": 24},
    {"name": "bbb", "age": 30},
    {"name": "ccc", "age": 27}
]

print(search(friends, "aaa", lambda x: x["name"]))