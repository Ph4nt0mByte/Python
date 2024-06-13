with open('file.txt', 'r') as file:
    word_freq = {}
    for line in file:
        words = line.split()
        for word in words:
            word = word.strip(",.!?")
            word = word.lower()
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
