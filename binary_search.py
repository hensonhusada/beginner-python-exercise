import random
import math

def binary_search(array, choice, count=0):
    count += 1
    length = len(array)
    if length < 1:
        print('No such element!')
        return None
    half_point = math.ceil(length/2)
    if choice < array[half_point]:
        binary_search(array[:half_point], choice, count)
    elif choice > array[half_point]:
        binary_search(array[(half_point+1):], choice, count)
    else:
        print('Found in %s iteration(s)!' %count)


search_array = [random.randint(0,100) for i in range(100)]
search_array.sort()

choice = input('Select the number you want to find (0-100): ')
try:
    choice = int(choice)
    binary_search(search_array, choice)
except Exception as e:
    print(e)

