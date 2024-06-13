with open("file.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.strip(",.!?")
            word = word.replace("This","")
            print(word)
