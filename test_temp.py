def move_zeros_to_end(lst):
    zeros = [x for x in lst if x == 0]
    non_zeros = [x for x in lst if x != 0]
    return non_zeros + zeros  


if __name__ == "__main__":
    my_list = [each for each in [1, 0, 3, 0, 5, 0, 7, 8, 0] if each != 0] + [each for each in [1, 0, 3, 0, 5, 0, 7, 8, 0] if each == 0]
    print(my_list)
    
    

