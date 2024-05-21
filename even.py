def getEven(nums):
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
    return even
nums = map(int, input("Please enter a list of integers (put a space between each integer): ").split())
print(getEven(nums))
