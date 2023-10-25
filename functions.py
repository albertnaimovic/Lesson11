# def convert_to_celsius(temp_f: float = 75) -> float:
#     return round((temp_f - 32) * 5 / 9, 1)
# print(f"Room temperature: {convert_to_celsius()} C")


# def print_letter(letter: str, *args, **kwargs) -> str:
#     print(letter)
#     if args:
#         print(f"Args: {args}")
#     if kwargs:
#         print(f"Kwargs: {kwargs}")
#     return letter
# print_letter("A", 25, 32, 453, 243, name = "Antanas", surname = "Nedzinskas")


# def add_two_numbers(no_a: int, no_b: int = 10) -> int:
#     return no_a + no_b
# print(f"Sum of numbers: {add_two_numbers(5)}")


# def multiply_two_numbers(no_a: int, no_b: int) -> int:
#     return no_a * no_b
# print(f"Multiplication: {multiply_two_numbers(5, 5)}")


# multiplication = lambda a, b: a * b
# print(multiplication(3, 6))


# sum_const = lambda a: print(a + 25)
# sum_const(5)


# 1) Create a function which converts lenght, mass, time units from SI system to CGS. 
# All arguments must hold default values if not provided.

# def convert_SI_to_CGS(my_length: float = 1.0, my_mass: float = 1.0, my_time: float = 1.0) -> str:
#     convert_length: float = my_length * 100
#     convert_mass: float = my_mass * 1000
#     convert_time: float = my_time * 60
#     return f"Converted length: {convert_length}cm\nConverted mass: {convert_mass}g\nConverted time: {convert_time}s"

# print(convert_SI_to_CGS())
    

# 2) Create a program which takes 5 random number per 1 input.
# Then create a function which takes the sum of those numbers (lets agree argument is being called 'num_sum'),
# and all those 5 numbers as separate free arguments as well.
# Multiply all those numbers with with the num_sum you calculated in a list data structure.

# from typing import List

# def sum_and_multiply(numbers: str) -> List[int]:
#     number_list: list = [int(x) for x in numbers.split(",")]
#     num_sum: int = sum(number_list)
#     num_multiply: list = [x * num_sum for x in number_list]
#     return num_multiply

# my_numbers: str = "3,2,6,1,8"
# print(sum_and_multiply(my_numbers))


# 3) Create lamba functions for these caclulations:
#  - calculate circle radius
#  - calculate average speed of the car (knowing distance and time passed to drive that distance)
#  - calculate percentage of value if 5500 is equal 200%

# circle_circumference = lambda radius: radius * 3.14
# print(f"Circle circumference: {circle_circumference(2)}")

# avg_speed = lambda distance, time_passed: round(distance / time_passed, 1)
# print(f"Average speed of the car: {avg_speed(60, 4)} km/h")

# calculate_percentage = lambda my_value: (my_value * 100) / 2750
# print(f"Percentage: {calculate_percentage(5500)} %")



# Write a function that takes two lists and adds the first element in the first list with the first element in the second list, 
# the second element in the first list with the second element in the second list, etc, etc. Return True if all element combinations add up to the same number.
# Otherwise, return False. Example:
# puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True


from typing import List

def puzzle_pieces(list_a: List[int], list_b: List[int]) -> bool:
    # cia gal ir nesamone
    if len(list_a) == len(list_b):
        list_sum: list = [ list_a[x] + list_b[x] for x in range(len(list_a))]
    else:
        return False
    
    print(list_sum)
    counter: int = 0
    for num in list_sum:
        if num == list_sum[0]:
            counter += 1

    if len(list_sum) == counter:
        return True
    else:
        return False

print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))
print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))
