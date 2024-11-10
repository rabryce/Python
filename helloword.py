def print_numbers(print_to_num):
    for i in range(print_to_num):
        print(i)

def main():
    print_numbers(get_number_to_print)

def get_number_to_print():
    return 4

if __name__ == '__main__':
    main()
