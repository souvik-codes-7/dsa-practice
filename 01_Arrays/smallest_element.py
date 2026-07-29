# Find the smallest element in a list

L = [12, 45, 7, 89, 23]

smallest = L[0]

for i in L:
    if i < smallest:
        smallest = i

print("Smallest element:", smallest)
