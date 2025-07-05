def get_brick_spaces(space, brick_count, brick_type):
    space = space * ' '
    brick_count = brick_count * brick_type
    return f'{space}{brick_count}{space}'

def print_pyramid(max_brick_count, brick_type):
    max_spaces_count = (max_brick_count - 1) // 2
    pyramid = ''
    for spaces_count in range(max_spaces_count, -1, -1):
        brick_count = max_brick_count - (2 * spaces_count)
        pyramid += "\n"+get_brick_spaces(spaces_count, brick_count, brick_type)
    return pyramid


def main():
    max_brick_count = int(input('Enter the max brick count: '))
    if max_brick_count % 2 == 0:
        print('Code will not work, please provide an odd number')
        quit()
    brick_type = input('Enter the brick type: ')
    if len(brick_type) != 1:
        print('Invalid brick type')
        quit()
    pyramidblabla = print_pyramid(max_brick_count, brick_type)
    print(pyramidblabla)
main()


