import re
# create regex pattern
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# search using pattern
myNum = phoneNumRegex.search('My number is 949-459-4012.')
print('Phone number found: ' + myNum.group())