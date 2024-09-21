from typing import Callable


def is_prime(n: int, computed_primes: list[int]) -> bool:
    tester = computed_primes[-1] if computed_primes else None
    other_primes = computed_primes[:-1]
    return n % tester != 0 and is_prime(n, other_primes) if tester is not None else True


def increment_until(n: int, stop_callback: Callable[[int], bool]) -> int:
    return n + 1 if stop_callback(n + 1) else increment_until(n + 1, stop_callback)


def get_next_prime(computed_primes: list[int]) -> int:
    last_prime = computed_primes[-1] if computed_primes else None
    new_prime = (
        increment_until(last_prime, lambda n: is_prime(n, computed_primes))
        if last_prime is not None
        else 2
    )
    return new_prime


def get_first_n_primes(n: int) -> list[int]:
    computed_primes = get_first_n_primes(n - 1) if n > 0 else []
    return [*computed_primes, get_next_prime(computed_primes)]


print(get_first_n_primes(15))
