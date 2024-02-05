# Take input from user and remove leading and trailing whitespace
text = input().strip()

# Replace remaining whitespace with "..."
text = text.replace(" ", "...")

# Print converted input
print(text)
