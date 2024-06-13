def create_dictionary():
    dictionary = {}

    while True:
        key = input("Enter the key (or 'q' to quit): ")
        if key == 'q':
            break

        value = input("Enter the value: ")
        dictionary[key] = value

    return dictionary

result = create_dictionary()
print(result)