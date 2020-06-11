# Import the regex module with import re.
import re

# Create a Regex object with the re.compile() function using a raw string
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# Pass the string you want to search into the Regex object’s search() method to return a Match object
myNum = phoneNumRegex.search('My number is 949-459-4012.')
# Call the Match object’s group() method to return a string of the actual matched text
print('Phone number found: ' + myNum.group())

# Create g
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# Pass the string you want to search into the Regex object’s search() method to return a Match object
myNumGrouping = phoneNumRegex.search('My number is 949-459-4012.')
print(myNumGrouping.group(1))
print(myNumGrouping.group(2))
print(myNumGrouping.group(3))
print(myNumGrouping.groups())

print(myNumGrouping.group(0))
print(myNumGrouping.group())

areaCode, mainNumberBeginning, mainNumberEnding = myNumGrouping.groups()

print(areaCode)
print(mainNumberBeginning)
print(mainNumberEnding)
#  escape characters
# .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
#  becomes
# \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)
phoneNumRegexParenthesis = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegexParenthesis.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
# Matching Multiple Groups with the Pipe -> |
myNameRegex = re.compile(r'Anisa|George')
mo1 = myNameRegex.search('Anisa and Apple and George')
print(mo1.group())
mo2 = myNameRegex.search("Apple and George and Anisa")

print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))

# Matching Zero or More with the Star
nameObj = re.compile(r'Anisa(na)*Mohamed')
naNa = nameObj.search('The AnisaMohamed is my weird name')
naNa2 = nameObj.search('The AnisanananananaMohamed is my weird name')
print(naNa.group())
print(naNa2.group())

# Matching One or More with the Plus
nameObj = re.compile(r'Anisa(na)+Mohamed')
naNa = nameObj.search('The AnisanaMohamed is my weird name')
naNa2 = nameObj.search('The AnisanananananaMohamed is my weird name')
naNa3 = nameObj.search('The AnisaMohamed is my weird name')

print(naNa.group())
print(naNa2.group())
print(naNa3 == None)

# Matching Specific Repetitions with Braces
repPattern = re.compile(r'(hi){2}')
hi = repPattern.search('Hello hiHellohihihehe')
print(hi.group())
hi = repPattern.search('Hello hiHellohihehihehi')
print(hi == None)

# Greedy and Non-greedy Matching
greedyPattern = re.compile(r'(He){3,5}')
greed = greedyPattern.search('HezzheHeHeHeHeHeHE')
print(greed.group())

nonGreedyPattern = re.compile(r'(He){3,5}?')
noGreed = nonGreedyPattern.search('ezzheHeHeHeHeHeHE')
print(noGreed.group())

