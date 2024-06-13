def name_frequency(names):
    frequency = {}
    for name in names:
        frequency[name] = frequency.get(name, 0) + 1
    return frequency
name_list = ["John", "Jane", "John", "Alice", "John", "Jane"]
names_frequency = name_frequency(name_list)

for name, frequency in names_frequency.items():
    print(f"{name}: {frequency}")