#!usr/bin/python3

#include "LIST_H"

def new_in_list(my_list, idx, element):
	if idx < 0 or idx >= len(my_list):
		return my_list[:]

	copy_list = my_list[:]
	
	copy_list[idx] = element
	
	return copy_list
