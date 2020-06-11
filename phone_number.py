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

# The findall() Method finds all instances unlike search which finds the first instances without groupings
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# Pass the string you want to search into the Regex object’s search() method to return a Match object
myNumGrouping = phoneNumRegex.findall('My number is 949-459-4012 and my alternate is 312-345-6701')
print(myNumGrouping)

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# Pass the string you want to search into the Regex object’s search() method to return a Match object
myNumGrouping = phoneNumRegex.findall('My number is 949-459-4012 and my alternate is 312-345-6701')
print(myNumGrouping)

# \d
# Any numeric digit from 0 to 9.
# \D
# Any character that is not a numeric digit from 0 to 9.
# \w
# Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W
# Any character that is not a letter, numeric digit, or the underscore character.
# \s
# Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S
# Any character that is not a space, tab, or newline.
# [a-zA-Z]
# matches letters only
vowelRegex = re.compile(r'[aeiouAEIOU]')
allVowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(allVowels)

excludeVowels = re.compile(r'[^aeiouAEIOU]')
constants = excludeVowels.findall('RoboCop eats baby food. BABY FOOD.')
print(constants)


startsWithHello = re.compile(r'^Hello')
mo = startsWithHello.search('Hello guys!')
print(mo)
mo = startsWithHello.search('He said hello.')
print(mo == None)
# Ends with pattern
endsWithDigit = re.compile(r'\d$')
mo = endsWithDigit.search('I end with the lucky number 7')
print(mo)
mo = endsWithDigit.search('I end with the lucky number 7!!')

print(mo == None)

# The Wildcard Character
wildCardPattern = re.compile(r'.all')
allMatches = wildCardPattern.findall('Walk to the wall and call before you fall because you are tall')
print(allMatches)

# Matching Everything with Dot-Star
careerExperiencePattern = re.compile(r'Job:(.*) Experience:(.*)')
mo = careerExperiencePattern.search('Job:Developer Experience:10 years')
print(mo.group(1))
print(mo.group(2))


# non greedy matching dot star
nonGreedyPattern = re.compile(r'\(.*?\)')
mo = nonGreedyPattern.search('(hey what is there to eat?) For dinner of course!)')
print(mo.group())
# greedy matching dot star
nonGreedyPattern = re.compile(r'\(.*\)')
mo = nonGreedyPattern.search('(hey what is there to eat?) For dinner of course!)')
print(mo.group())

