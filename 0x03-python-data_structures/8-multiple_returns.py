#!/usr/bin/pyrthon3

#include "LIST_H"

def multiple_returns(sentence):
	if not sentence:
		return (0, None)
	return (len(sentence), sentence[0])
