#!usr/bin/python3
#include "LIST-H"

def element_at(my_list, idx):
	
	while True:
		if idx < 0 or idx >= len(my_list):
			return None
		return my_list[idx]

