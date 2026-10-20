s = input("Enter the main string: ")
sub = input("Enter the substring: ")

indices = []
start = 0
while True:
    pos = s.find(sub, start)
    if pos == -1:
        break
    indices.append(pos)
    start = pos + 1

if indices:
    print(f"'{sub}' found at indices:", indices)
else:
    print(f"'{sub}' not found.")
