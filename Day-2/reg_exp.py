#find pattern
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")



#match pattern
import re
emails = [
    "user@example.com",
    "another.user@subdomain.example.org",
    "invalid.email",
    "third.user@invalid@domain.com"
]

# Regular expression pattern for matching an email address
pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'

# Loop through each email and check if it matches the pattern
for email in emails:
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

#replace
import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)   

#search
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

#soilt
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)
