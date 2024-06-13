def unique(lst):
    nlst = []
    for num in lst:
        if num not in nlst:
            nlst.append(num)
    return nlst

list = [1, 2, 3, 3, 2]
print(unique(list))