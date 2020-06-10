# Import the regex module with import re.
import re
# Create a Regex object with the re.compile() function using a raw string
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# Pass the string you want to search into the Regex object’s search() method to return a Match object
myNum = phoneNumRegex.search('My number is 949-459-4012.')
# Call the Match object’s group() method to return a string of the actual matched text
print('Phone number found: ' + myNum.group())