def main():
    file_name = input("File name: ").strip().lower()
    print(media_type(file_name))

def media_type(s):
    if s.endswith(".gif"):
        return "image/gif"
    elif s.endswith(".jpg") or s.endswith("jpeg"):
        return "image/jpeg"
    elif s.endswith(".png"):
        return "image/png"
    elif s.endswith(".pdf"):
        return "application/pdf"
    elif s.endswith(".txt"):
        return "text/plain"
    elif s.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()
    