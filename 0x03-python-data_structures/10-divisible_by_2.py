#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [True for i in my_list if i % 2 == 0 else False]
    return(new_list)
