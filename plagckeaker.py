
from difflib import SequenceMatcher 

with open('demo.txt') as first_file, open('demo2.txt') as second_file: 
	
	text_file1 = first_file.read() 
	text_file2 = second_file.read() 
	ab = SequenceMatcher(None, text_file1, text_file2).ratio() 
	result = int(ab*100) 
	print(f"{result}% Plagiarized Content") 