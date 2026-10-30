import re

text = """
The library opens at 08:30 AM and closes at 6:00 PM.
There are 125 books, 24 students, and 7 teachers.
Contact us at library@example.com or admin@test.org.
Python is easy to learn. python is popular.
The website is https://example.com/page?id=25.
"""

# find first number
pattern = r"\d+"
match = re.search(pattern, text)
print(match)

# find all number
pattern = r"\d+"
match = re.findall(pattern, text)
print(match)

# find all email address
pattern = r"[\w.]+@[\w.]+\.[a-z]+"
match = re.findall(pattern, text)
print(match)

# usage of word boundary
pattern = r"\bPython\b"
match = re.findall(pattern, text)
print(match)

# find times
pattern = r"\d+:\d+\s*(?:AM|PM)"
match = re.findall(pattern, text)
print(match)

# replace irrespective to case sensitivity
match = re.sub(r"Python", "Java", text, flags=re.IGNORECASE)
print(match)

# split at white space or comma
pattern = r"[,.]"
match = re.split(pattern, text)
print(match)

# find exact 5 numbers match
pattern = r"\d{2}"
match = re.findall(pattern, text)
print(match)
