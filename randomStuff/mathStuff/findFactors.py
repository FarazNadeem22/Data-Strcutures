import time

def find_factors(test_number: int) -> list:
    """
    Finds and prints all factors of a given number, determines if it's prime,
    and lists its prime factors if it is not prime.
    
    :param test_number: The number for which factors need to be found.
    :return: A list of prime factors.
    """
    factor_list = [x for x in range(1, test_number + 1) if test_number % x == 0]
    prime_factor_list = []
    
    # Check if the number is prime
    if len(factor_list) <= 2:
        print(f"\nNumber: {test_number}")
        print(f"Status: Prime Number\n")   
    else:
        print(f"\nNumber: {test_number}")
        print(f"Status: Not a Prime Number\n")
    
    # Display factors
    print(f"Factors: {', '.join(map(str, factor_list))}")
    print(f"Total Factors: {len(factor_list)}\n")
    
    # Finding prime factors from the list of factors if the number is not prime
    prime_factor_list = [factor for factor in factor_list if len([x for x in range(1, factor + 1) if factor % x == 0]) == 2]
    
    print(f"Prime Factors Count: {len(prime_factor_list)}")
    print(f"Prime Factors: {', '.join(map(str, prime_factor_list))}\n")
    
    return prime_factor_list


def get_factors(number: int, prime_factor_list: list) -> None:
    """
    Get the prime factor makeup of the number.
    
    :param number: The number to factorize.
    :param prime_factor_list: A list of prime factors of the number.
    """
    new_list = [0] * len(prime_factor_list)  # Initialize counters for each prime factor
    
    for i, prime in enumerate(prime_factor_list):
        while number % prime == 0:
            number /= prime  # Reduce the number by dividing it by the prime factor
            new_list[i] += 1  # Increment the count of this prime factor
    
    factor_representation = [f"{prime}^{count}" for prime, count in zip(prime_factor_list, new_list) if count > 0]
    print(f"Prime Factor Makeup: {', '.join(map(str, factor_representation))}")


if __name__ == "__main__":
    print("This program will find all the factors of a given number.")
    number = int(input("Please enter the number you want to find factors for: "))
    t1 = time.time()
    get_factors(number, find_factors(number))
    print(f'Time taken: {time.time()-t1:.6f} seconds')