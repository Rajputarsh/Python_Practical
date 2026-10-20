filename = "sample.txt"

with open(filename, "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("Python file handling practical.\n")
print("File written.")

with open(filename, "a") as f:
    f.write("This line was appended.\n")
print("Line appended.")

with open(filename, "r") as f:
    content = f.read()
print("\nFile contents:")
print(content)

print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))
print("Characters:", len(content))
