#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 27, 2021
# This program asks the user for how many times to add
# numbers together and then adds them if they are positive
# numbers, otherwise it does not add them

def main():
    # define variables
    sum = 0
    sum_as_string = ""
    counter = 0

    while True:
        # ask user for how many numbers to add
        times_added_string = input("How many numbers do you want to add? ")
        try:
            # convert from string to int
            times_added_int = int(times_added_string)
            if (times_added_int <= 0):
                # check if input is a positive number
                print("{} is not a positive number,\
 try again.". format(times_added_int))
            else:
                print("\n")
                while counter < times_added_int:
                    # ask user for what numbers to add
                    number_as_string = input("Enter a positive number\
 to add: ")
                    try:
                        # convert from string to integer
                        number_as_int = int(number_as_string)
                        if (number_as_int > 0):
                            # check if input is a positive number
                            if counter == 0:
                                # first number in the addition
                                sum = sum + number_as_int
                                sum_as_string = number_as_string
                                counter = counter + 1
                                continue
                            else:
                                # rest of the numbers in the addition
                                sum = sum + number_as_int
                                sum_as_string = sum_as_string + "\
 + " + number_as_string
                                counter = counter + 1
                                continue
                        # check if number is negative
                        print("{} is not a positive number,\
 try again.". format(number_as_int))
                    except ValueError:
                        # error message
                        print("{} is not a positive number,\
 try again.". format(number_as_string))
                # display sum
                print("\n")
                print("{0} = {1}". format(sum_as_string, sum))
                break
        except ValueError:
            # error message
            print("{} is not a positive number,\
 try again.". format(times_added_string))


if __name__ == "__main__":
    main()
