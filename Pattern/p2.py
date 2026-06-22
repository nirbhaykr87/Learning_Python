a = int(input("Enter the number of rows"))
b = int(input("Enter the number of colmns"))

for i in range(a):
    for j in range(i+1):
        print("*", end="")

    print()