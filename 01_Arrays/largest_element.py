# Find the largest element in a list

L = [12, 45, 7, 89, 23]

largest = L[0]

for i in L:
    if i > largest:
        largest = i

print("Largest element:", largest)
