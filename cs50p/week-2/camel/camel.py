def main():
    camel_case = input("camelCase: ").strip()
    print("snake_case:", snake_case(camel_case))

def snake_case(string):
    for letter in string:
        if letter.isupper():
            string = string.replace(letter, "_" + letter.lower())
    return string

main()
