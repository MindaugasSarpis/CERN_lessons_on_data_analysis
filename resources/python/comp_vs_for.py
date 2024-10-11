numbers = [1, 2, 3, 4, 5]
fruits  = ['apple', 'banana', 'cherry', 'date', 'elderberry']




my_new_list = []
for i in range(len(numbers)):
    print(numbers[i], fruits[i])
    # my_new_list += [(numbers[i], fruits[i])]
    # my_new_list.append((numbers[i], fruits[i]))
# print(my_new_list)

my_new_list = [i for i in zip(numbers, fruits)]
my_new_list = [zip(numbers, fruits)]
print(my_new_list)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = list(zip(a, b))
print(x)