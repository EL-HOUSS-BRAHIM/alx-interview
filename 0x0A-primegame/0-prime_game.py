#!/usr/bin/python3
""" Prime Game """


def sieve_of_eratosthenes(max_num):
    """
    Generates a list of boolean values indicating whether
    numbers up to max_num are prime.

    Args:
        max_num (int): The maximum number up to which to
        check for prime numbers.

    Returns:
        list: A list where index i is True if i is a
        prime number, False otherwise.
    """
    # Initialize a list to True, assuming all numbers are prime initially
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    # Use Sieve of Eratosthenes to mark non-prime numbers
    for start in range(2, int(max_num ** 0.5) + 1):
        if primes[start]:
            for multiple in range(start * start, max_num + 1, start):
                primes[multiple] = False

    return primes


def isWinner(x, nums):
    """
    Determines the winner of the prime game played over x rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (list): A list of integers where each integer represents
        the range of numbers (from 1 to n) for that round.

    Returns:
        str or None: The name of the player with
        the most wins ("Maria" or "Ben").
                    Returns None if the number of wins is tied.
    """
    if x <= 0 or not nums:
        return None

    # Determine the maximum number across all rounds
    max_num = max(nums)

    # Get the prime numbers up to the maximum number using Sieve of
    # Eratosthenes
    primes = sieve_of_eratosthenes(max_num)

    # Initialize win counters for both players
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        # Count the number of primes within the range 1 to n
        prime_count = sum(primes[1:n + 1])

        # Determine the winner of the current round based on the prime count
        if prime_count % 2 != 0:
            # If the count of primes is odd, Maria wins
            maria_wins += 1
        else:
            # If the count of primes is even, Ben wins
            ben_wins += 1

    # Determine the overall winner based on the number of wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
