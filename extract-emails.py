import re

text = "Contact us at info@xyz.com or support@abc.org for help."
emails = re.findall(r'\S+@\S+', text)
print(emails)