ListA = [6,3,5,4,1];
ListB = ["Adan", "Pablo", "Omar", "Julio","Edgar"]


print(sorted(list(zip(ListA, ListB)), key=lambda x: x[1]))


print(ListA)
print(ListB)