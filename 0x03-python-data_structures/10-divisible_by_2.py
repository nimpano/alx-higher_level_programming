#!usr/bin/python3

def divisible_by_2(my_list=[]):
	if not my_list:
		return False
	for num in my_list:
		if num % 2 == 0:
			continue
			num += 1
			return(num)
	return(num, True)
