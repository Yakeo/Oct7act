userNums = int(input("How many things to do you want to add?: "))
list= []

for n in range(userNums):
    word = input("What items do you want to add?: ")
    list.append(word)
    
print(list)

warning = str(input("Do you want to sort your list or reverse its arrangement?: (sort/reverse)"))
if warning == "sort":
    list.sort()
elif warning == "reverse":
    list.reverse()
    
print(list)