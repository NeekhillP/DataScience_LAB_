# 5. Use the re module to write a script that searches through a paragraph and extracts all
# words that start with an uppercase letter (e.g., "London", "Python") to identify proper
# nouns or sentence starters.

import re

paragraph = """
Python is a popular programming language created by Guido van Rossum.
It is widely used in Data Science, Machine Learning, and Web Development.
London is the capital of England.
"""

pattern = r'\b[A-Z][a-zA-Z]*\b'

uppercase_words = re.findall(pattern, paragraph)

print("Words starting with uppercase letters:")
print(uppercase_words)
