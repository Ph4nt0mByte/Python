nums = []
while True:
    num = input("Enter a number (or 'q' to quit): ")
    if num == 'q':
        break
    num = int(num)
    nums.append(num)
minimum = nums[0]
maximum = nums[0]
for n in nums:
		if n > maximum:
			maximum=n
		if n < minimum:
			minimum=n
print("maximum number is:",maximum)
print("minimum number is:",minimum)