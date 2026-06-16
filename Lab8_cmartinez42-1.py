"""
Program Name: UPC Validator
Author Name: Chris Martinez
Purpose: The purpose of this program is to read a 12 digit number code from the user, run a algorthm to check if the number is real, then tell the user whether the code is valid or invalid.
Starter Code Information: None
Date: June 15 2026
"""

def find_UPC(upc_string):

    d1 = int(upc_string[0])
    d2 = int(upc_string[1])
    d3 = int(upc_string[2])
    d4 = int(upc_string[3])
    d5 = int(upc_string[4])
    d6 = int(upc_string[5])
    d7 = int(upc_string[6])
    d8 = int(upc_string[7])
    d9 = int(upc_string[8])
    d10 = int(upc_string[9])
    d11 = int(upc_string[10])


    odd_sum = d1 + d3 + d5 + d7 + d9 + d11

    odd_result = odd_sum * 3

    even_sum = d2 + d4 + d6 + d8 + d10
    total = odd_result + even_sum

    M = total % 10

    if M == 0:
        return 0
    else:
        return 10 - M
    


user_input = input("Enter a 12-digit UPC: ")

first_11 = user_input[0:11]

last_digit = int(user_input[11])


