userNums = int(input("How many things to do you want to add?: "))
list= []

for n in range(userNums):
    word = str(input("What items do you want to add?: "))
    list.append(word)
    
print(list)


warning = str(input("Do you want to remove an item in the array by index or value?: "))

if warning == "index":
    print(list)
    index = int(input("Which index?: "))
    list.pop(index)
elif warning == "value":
    print(list)
    value = input("Which value?: ")
    list.remove(value)
    
print(list)