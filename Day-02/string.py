#concatination of string
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2 #here " " its for space between hello world 
print(result)

#define length of string
text = "Python is easy"
length = len(text)
print("Length of the string:", length)

#convert into lowercase and uppercase
text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#divide string into substring
text = "Hello, how are you doing today?"
words = text.split()
print(words)

#replace words in string
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

#remove whitspace
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

#find word within string using in keyword
text = "Python is awesome"
substring = "is"
if substring in text:    #in keyword is used to check if substring is part of the main text or not
 print(substring, "found in the text")



