#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x < 0 or x >= len(my_list):
        print("Index is out of range.")
    else:
        print(my_list[x])
