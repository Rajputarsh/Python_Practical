n = int(input("Enter n: "))

cubes = {i: i**3 for i in range(1, n + 1)}
print(cubes)

for key, value in cubes.items():
    print(f"{key} -> {value}")
