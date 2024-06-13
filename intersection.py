li1 = [1, 2, 3, 4, 5]
li2 = [4, 5, 6, 7, 8]

intersection = []
for num in li1:
    if num in li2:
        intersection.append(num)

print("Intersection:", intersection)