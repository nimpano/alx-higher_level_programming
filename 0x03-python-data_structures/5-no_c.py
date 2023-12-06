#!usr/bin/python3

#include "LIST_H"

def no_c(my_string):
	
	new_string = ""
	for i in my_string:
		
		if i == 'c' or i == 'C':
			continue			
		new_string += i
	return new_string
