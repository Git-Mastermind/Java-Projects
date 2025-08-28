
def is_odd(index):
    if index % 2 != 0:
        return True
    else:
        return False
def print_sum(list):
    return sum(list)



def main():
    input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    odd_number_index_values = []

    for i in range(len(input_list)):
        is_odd(i)
        if is_odd(i):
            odd_number_index_values.append(input_list[i])
    print(print_sum(odd_number_index_values))


main()








