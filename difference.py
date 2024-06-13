li1 = [1, 2, 3, 4, 5]
li2 = [4, 5, 6, 7, 8]

difference = []
for num in li1:
    if num not in li2:
        difference.append(num)

print("Difference:", difference)