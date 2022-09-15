#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.
    Args:
     my_list (list): The list to print elements from.

     """
     ret = 0
     for i in range(0, x):
         try:
             print("{:d}".format(my_list[i]), end="")
             ret += 1
         except (ValueError, TypeError)
         continue
     print("")
     return (ret)
