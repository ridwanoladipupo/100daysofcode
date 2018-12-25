#Tribonacci List

lists = []

size = int(input("specify the list size :"))
iteration = int(input("How many iteration do you want to perform? :"))

for i in range (size):
    elements = int(input("Input your elements :"))
    lists.append(elements)

print("lists = ", lists)

print("tribonacci sequence :")
print(str(lists[-3 :]))

for i in range (iteration):
    add = 0
    for j in lists[-3 :]:
        add +=j
    lists.append(add)
    print(lists)
