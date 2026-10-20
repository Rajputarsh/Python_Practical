ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
elif ch.isalpha():
    kind = "vowel" if ch.lower() in "aeiou" else "consonant"
    case = "uppercase" if ch.isupper() else "lowercase"
    print(f"'{ch}' is an alphabet: {case} {kind}")
elif ch.isdigit():
    print(f"'{ch}' is a digit")
elif ch.isspace():
    print("It is a whitespace character")
else:
    print(f"'{ch}' is a special character")
