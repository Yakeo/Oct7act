userNums = int(input("How many numbers do you want to add to the list?: "))
nums = []

for n in range(userNums):
    number = int(input("What number/s do you want to add?: "))
    nums.append(number)
    
print(nums)

warning = input("Do you want to clear the list? (yes/no): ")
if warning == "yes":
    nums.clear()
    print(nums)
elif warning == "no":
    print(nums)