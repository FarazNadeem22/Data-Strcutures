def find_factors(test_number: int) -> None:
    """
    Finds and prints all factors of a given number, determines if it's prime,
    and lists its prime factors if it is not prime.
    
    :param test_number: The number for which factors need to be found.
    """
    factor_list = []  # List to store all factors
    prime_factor_list = []  # List to store prime factors
    
    # Finding factors of the given number
    for x in range(1, test_number + 1):
        if test_number % x == 0:
            factor_list.append(x)
    
    # Check if the number is prime
    if len(factor_list) <= 2:
        print(f"\nNumber: {test_number}")
        print(f"Status: Prime Number\n")
        return
    else:
        print(f"\nNumber: {test_number}")
        print(f"Status: Not a Prime Number\n")
    
    # Display factors
    print(f"Factors: {', '.join(map(str, factor_list))}")
    print(f"Total Factors: {len(factor_list)}\n")
    
    # Finding prime factors from the list of factors if the number is not prime
    for factor in factor_list:
        if len([x for x in range(1, factor + 1) if factor % x == 0]) == 2:
            prime_factor_list.append(factor)
    
    print(f"Prime Factors Count: {len(prime_factor_list)}")
    print(f"Prime Factors: {', '.join(map(str, prime_factor_list))}\n")


if __name__ == "__main__":
    print("This program will find all the factors of a given number.")
    number = int(input("Please enter the number you want to find factors for: "))
    find_factors(number)