#!/usr/bin/python3

def input_validation():
    try:
        value = int(input(">> "))
        return value
        
    except KeyboardInterrupt:
        return "KeyboardInterrupt"
        
    except ValueError:
        return "ValueError"



def random_number_generator():
    import random

    try:
        the_list_of_integers = []
        print("Enter how many values you want the program to generate.")
        the_integers = input_validation()
        if the_integers == "KeyboardInterrupt" or the_integers == "ValueError":
            return the_integers
        else:
            for i in range(the_integers):
                the_randomly_generated_value = random.randint(1, the_integers)
                the_list_of_integers.append(the_randomly_generated_value)
                
            return the_list_of_integers
            
    except KeyboardInterrupt:
        return "KeyboardInterrupt"



def bubble_sort():
    import time

    the_integer_list = random_number_generator()

    try:
        if the_integer_list == "KeyboardInterrupt":
            print("Keyboard Interrupt!")
        elif the_integer_list == "ValueError":
            print("Error: Value Error!")
        else:
            length = len(the_integer_list)
            
            start = time.perf_counter()
            
            for i in range(length - 1):
                swap = False
                
                for j in range(length - i - 1):
                    if the_integer_list[j] > the_integer_list[j + 1]:
                        the_integer_list[j], the_integer_list[j + 1] = the_integer_list[j + 1], the_integer_list[j]
                        swap = True 
                        
                if not swap:
                    break
            
            end = time.perf_counter()
            time_to_proccess = end - start 
            print(f"Time to sort the integers: {time_to_proccess}s.")
            
    except KeyboardInterrupt:
        print("Keyboard Interrupt!")
    


def main():
    bubble_sort()



main()
