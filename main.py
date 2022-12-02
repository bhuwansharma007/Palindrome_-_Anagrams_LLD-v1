def isAnagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()

# check if length is same
        if(len(str1) == len(str2)):

    # sort the strings
            sorted_str1 = sorted(str1)
            sorted_str2 = sorted(str2)

    # if sorted char arrays are same
            if(sorted_str1 == sorted_str2):
                return True
            else:
                return False

        else:
            return False



def isPalindrome(str1):
 
    # Run loop from 0 to len/2
    return str1 == str1[::-1]


data = []
str_data = []
palindrome_data = []
anagram_data = []

with open('data.txt', encoding='utf8') as f:
    for line in f:
        data.append(line.strip())

for i in data:
	if i.isalpha():
		str_data.append(i)

for i in range(0,len(str_data)-1):
	if isPalindrome(data[i]):
		palindrome_data.append(data[i])
	if isAnagram(data[i],data[i+1]):
		anagram_data.append((data[i],data[i+1]))
		
print("Palindrome strings are : ",palindrome_data,"\n")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Anagram strings are : ",anagram_data,"\n")
	
 
