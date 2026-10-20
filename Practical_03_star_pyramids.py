n = int(input("Enter number of rows: "))

print("\nRight-angled triangle:")
for i in range(1, n + 1):
    print("* " * i)

print("\nInverted triangle:")
for i in range(n, 0, -1):
    print("* " * i)

print("\nFull pyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nDiamond:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
