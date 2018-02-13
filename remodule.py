import re
def age():
	Nameage = """
	Amber is 22 and Gautam is 11
	Pooja is 66 and Kharbanda is 55
	"""
	ages = re.findall(r'\d{1,3}',Nameage)
	names = re.findall(r'[A-Z][a-z]*',Nameage)
	print(names)
	print(ages)

# 1. find a word in a given string

def search():
	if re.search("inform", "This is inform to amber gautam"):
		print("it is present")
	else:
		print("no")
# 2. Find all word in string using findall

def findalll():
	allin = re.findall("inform" , "this is inform to all is inform")
	for i in allin:
		print(i)

# 3. Generate Iteration
def iterations():
	string1 = "We need to inform to you"
	# it gives starting and ending index of a word present in a string  
	for i in re.finditer("inform", string1):
		look = i.span()
		print(look)
# 4. Match word of a particular pattern

def match_pattern():
	string2 = "Map, Rap, Cap"
	allstr = re.findall("[MRC]ap", string2)
	for i in allstr:
		print(i)
# 5. Series of range 
# ^ => It means except the given condition 
def match_series():
	string2 = "Map, Rap, Cap"
	allstr = re.findall("[^D-Z]ap", string2)
	for i in allstr:
		print(i)
#6. Replace a string
def replace_string():
	data = "hat, rat, mat"
	regex = re.compile("[r]at") #compile it will provide more methods
	new_data = regex.sub("food",data)
	print(new_data)
# 7. backslash
def back():
	randstr = "this is \\python"
	print(randstr) #it will show one backslash in result
	print(re.search(r"\\python",randstr))


# 8.  Match a single character
def match_single_char():
	randstring = """
	My name is amber gautam
	python is awesome
	"""
	print(randstring)
	regex = re.compile("\n")
	new = regex.sub("",randstring) #all character in one line
	print(new)
	"""
	\b : backspaces
	\f form feed
	\t: tab
	\r: carriage return 
	\v : vertical tab
	"""
# 9 it will give match character 
def single_char():
	num = "123456"
	print("Matches" ,len(re.findall("\d", num))) # \d digits all numerical \D except present

# 10 Verify phone no
# \w it is [a-z][A-Z][0-9] match anything inside sq brackets
# \W 
def phn_number():
	phn = "123-454-8789"
	if re.search("\d{3}-\d{3}-\d{4}", phn): #also use \d
		print("its is a phone no")
	else:
		print("enter valid phone no")
# 11. Full name
# \s = [\f\n\r\v]
#\S [^\f\n\t\v\r]
def name():
	if re.search("\w{2-20}\s\w{2-20}","amber gautam"):
		print("valid name")
name()

# 12. VERIFY EMAIL ADDRESS
def email():
	# 1 - 20 lowercase and uppercase letters, numbers, + ,- % 
	# @symbol etc
	emails = "ambergautam1@gmail.com, gautam@gmail.com, @gmail.com"
	print("Email matches" , len(re.findall("\w{1-20}@[\w.]{2-20}.[A-Za-z]{2,3}",emails)))
email()