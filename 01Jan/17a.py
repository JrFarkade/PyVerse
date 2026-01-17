# To find the Maximun Number
nums = []
n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)

maximum = nums[0]

for num in nums:
    if maximum < num:
        maximum = num

print("Max =", maximum)
