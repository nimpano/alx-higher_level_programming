#!/usr/bin/python3

#include "LIST_H"

def replace_in_list(my_list, idx, element):
	
	if idx < 0 | idx >= len(my_list):
		return my_list

	else:
		my_list[idx] = element
		return my_list

	return my_list


