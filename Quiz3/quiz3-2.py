#  Name : Barış Yıldız | Student ID : 2210356107
import sys


def find_lucky_numbers(sequence):
    index = 0       # index variable is the index of delete_index in sequence.
    delete_index = int(number_list[index])      # every [delete_index]'th index will be removed from the remaining list in each iteration
    if sequence != [str(i) for i in range(1, int(sequence[-1])+1)]:  # this if statement checks if the sequence that is provided is in ascending order with increments of 1 and starts with 1. So, if the sequence contains numbers less that or equal to zero, or if the sequence is not in ascending order, the program will terminate.
        sequence.clear()  # I chose to output an empty list if this condition is not met. a.k.a. if the input is invalid.
        return ""
    try:
        while delete_index <= len(number_list) and index < len(number_list):
            if index == 0:      # in the first iteration, delete every second element.
                del number_list[1::2]
            else:               # in the following iterations, delete every [delete_index]'th element
                print(" ".join(number_list))
                del number_list[delete_index-1::delete_index]
            index += 1
            delete_index = int(number_list[index])
        print(" ".join(number_list))
    except:
        print(" ".join(number_list))
        pass


numbers = sys.argv[1]
number_list = numbers.split(",")
find_lucky_numbers(number_list)
