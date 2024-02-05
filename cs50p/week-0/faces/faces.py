def main():
    text = input("Enter text containing a happy or sad face: ")
    converted_text = convert(text)
    print(converted_text)


def convert(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")


main()
