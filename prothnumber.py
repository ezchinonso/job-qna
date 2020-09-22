import math
		

#PROTH_THEOREM = k * 2^(n+2) +1
def isPowerOfTwo(n): 

	return (n and (not(n & (n - 1))))  
	
	
def isProthNumber( n): 	
	k = 1
	while(k < (n//k)): 
		# check if k divides n or not 
		if(n % k == 0): 
			# Check if n / k is power of 2 or not 
			if(isPowerOfTwo(n//k)): 
					return True
		# update k to next odd number 
		k = k + 2	
	 
	return False


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True	

def isProthPrime(n):
	if isProthNumber(n-1) and is_prime(n):
		print ('{n} IS a proth prime number'.format(n=n))
	else:
		print ('{n} IS NOT a proth prime number'.format(n=n))			

n = input("NUMBER ")

#check if n is_proth_prime
isProthPrime(n) 


