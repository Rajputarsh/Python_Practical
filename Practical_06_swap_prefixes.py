s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Prefix length to swap: "))

if n > len(s1) or n > len(s2):
    print("Prefix length is larger than a string.")
else:
    print("After swapping:", s2[:n] + s1[n:], s1[:n] + s2[n:])
