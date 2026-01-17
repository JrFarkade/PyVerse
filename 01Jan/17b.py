# To find the Minimum Number.
nums = []
n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)

minimum = nums[0]

for num in nums:
    if minimum > num:
        minimum = num

print("Min =", minimum)
