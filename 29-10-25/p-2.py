# Remove Punctuation Example
import string
text = "Hello, World! Welcome to Python programming."
translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator)
print(cleaned_text)  # Hello World Welcome to Python programming