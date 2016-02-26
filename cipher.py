# create a loop to put all the ascii characters in a list
def cipher (word, n):
	list_of_word = list(word)
	new_list_of_words = []
	print ("original words: ", list_of_word)

	for i in range (0, len(list_of_word)):
		# uppercase
		if (ord(list_of_word[i]) in range (65,91)):
			new_pos = ord(list_of_word[i])+n
			if new_pos not in range (65+n,92-n):
				x = (new_pos - 90)
				new_pos = (x + 64)
		# lowercase
		elif (ord(list_of_word[i]) in range (97,123)):
			new_pos = ord(list_of_word[i])+n
			if new_pos not in range (97+n,124-n):
				x = (new_pos - 122)
				new_pos = (x + 96)
		# other characters
		else:
			new_pos = ord(list_of_word[i])
		new_list_of_words.append(chr(new_pos))
	print ("new word: ", new_list_of_words)	

print (cipher("AA!vZ a?Bz",5))



'''
	print ("Original word:", word)
	lower_case = []
	upper_case=[]
	new_string_list = [] 

	# list of all lowercase letters
	for i in range (97,123):
		lower_case.append(chr(i))
	#print (lower_case)

	length = len(lower_case)

	# list of all uppercase letters
	for i in range (65,91):
		upper_case.append(chr(i))
	#print (upper_case)

	for i in range (0,length):
		if lower_case[i] in word:
			new_string_list.append(lower_case[i+n]) 
		if upper_case[i] in word:
			new_string_list.append(upper_case[i+n])

	new_string = "".join(new_string_list)
	print ("New word:", new_string)				
'''





