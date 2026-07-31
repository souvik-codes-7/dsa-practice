# Problem: Linear Search
# Language: Python
# Time Complexity: O(n)
# Space Complexity: O(1)

L = [12, 45, 7, 89, 23]
k = int(input("Enter the element to search: "))

found = False
c = 0

for i in L:
    if k == i:
        found = True
        print("Found at index", c)
        break
    c += 1

if not found:
    print("Not Found")
