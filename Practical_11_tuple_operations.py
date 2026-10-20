t = tuple(int(x) for x in input("Enter numbers separated by spaces: ").split())

print("Tuple:", t)
print("Length:", len(t))
print("Max:", max(t))
print("Min:", min(t))
print("Sum:", sum(t))
print("Sorted:", tuple(sorted(t)))
print("Reversed:", t[::-1])
print("First element:", t[0])
print("Last element:", t[-1])

x = int(input("Enter a number to count/search: "))
print("Count:", t.count(x))
print("Index:", t.index(x) if x in t else "not found")

t2 = (100, 200)
print("Concatenation:", t + t2)
print("Repetition:", t2 * 2)
