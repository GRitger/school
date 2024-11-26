import re

with open('11.txt', 'r') as file:
    content = file.read()

pattern = r'\b(\d{4}\.\d+)&(\d{4}\.\d+)\b'

matches = re.findall(pattern, content)

max_length = 0
for match in matches:
    full_expression = f"{match[0]}&{match[1]}"
    max_length = max(max_length, len(full_expression))

print(max_length)