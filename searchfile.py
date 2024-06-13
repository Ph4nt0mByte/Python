search = None
s=input("enter the word to search:")
with open("file.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.strip(",.!?")
            if word == s:
                search = word 
if search is not None:
    print(search)
else:
    print(f"Word {s} not found in the file.")
