# test_capitalize.py

import pytest

class Test_Smoketest():

    test_input = "3, 4, 5, 7, 9, 12, 8, 0, 4, 21, 132, 3"
    inputlist = test_input.split(",")   # split function splits string into a list.
    print(inputlist)

    print("list ----------------------------------------------------------------------------------\n")

    tuple = tuple(inputlist)
    print(tuple)

    print("tuple ---------------------------------------------------------------------------------\n")