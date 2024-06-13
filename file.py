def sort(numbers):
  for i in range(len(numbers)):
    index = i
    for j in range(i, len(numbers)):
      if numbers[index] < numbers[j]:
        index = j
    if i != index:
      temp = numbers[i]
      numbers[i] = numbers[index]
      numbers[index] = temp

  # Move the return statement outside the loop to return the sorted list
    print(numbers)
  return numbers

numbers = [1, 3, 2, 7, 4,19,56,71,46,82,88,68,53,90,85,47,96,943,999,537,76,43,56,643,463,765,875,865,996,87,6,74]
sorted_numbers = sort(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 7]
