def count_frequency(word, list):
    frequency = {}
    for item in list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency 
with open("file.txt", "r") as file:
    words = file.read().split() 
    word_counts = count_frequency("word", words)
    print(word_counts) 