def print_b_words(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) == 3 and word.lower().startswith('b'):
                        print(word)
    except FileNotFoundError:
        print("File not found.")

# Example usage:
file_name = 'example.txt'  # Replace 'example.txt' with the name of your text file
print_b_words(file_name)


def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# Example usage:
number = 24  # Replace 20 with any integer you want to find divisors for
print(find_divisors(number))


def get_multiple_of_6():
    while True:
        try:
            number = int(input("Please enter a multiple of 6: "))
            if number % 6 == 0:
                return number
            else:
                print("The number is not a multiple of 6. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage:
multiple_of_6 = get_multiple_of_6()
print("You entered:", multiple_of_6)
