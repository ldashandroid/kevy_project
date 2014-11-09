# Dealing with Primes so we need this function

def is_prime(num):
    for j in range(2, num):
	if (num % j) == 0:
	    return False
    
    return True

# I assumed that you will pass the secret(which is a function)
# and integer into this function. n is called prime_bound in this
# function

def check_if_secret_is_additive(secret, prime_bound):
    # I assume that the upper bound for prime 
    # numbers is less 100000000

    if prime_bound > 100000000:
	raise MyException('Take it easy on the large primes')
    
    if prime_bound <= 2:
	raise MyException('There are no prime numbers less than 2')

    # when prime_bound is 3 this becomes a pretty trivial
    # test and it's best to handle this case separately
    if prime_bound == 3:
	return secret(2+2) == (secret(2) + secret(3))
    
    # x will be referred to as current_prime
    # made current prime 2 so I could cheat when checking
    # for primes

    current_prime = 2
    
    # I assume that the x and y passed to the secret are a prime 
    # and the next following prime i.e. x=2 and y=3, x=3 and y=5... 
    for i in range(3, prime_bound, 2):    
	if is_prime(i):
            next_prime = i
	    if not secret(current_prime+next_prime) == (secret(current_prime) + secret(next_prime)):
		return False
	
	current_prime = next_prime
    
    return True


class MyException(Exception):
    pass

