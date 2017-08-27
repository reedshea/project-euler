# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


x = 600851475143
i = 2
j = 0


def is_prime (x):
	prime = True
	for i in range(2,x):
		if x%i == 0:
			prime = False
			break					# If X has a divisor without remainder, it's not prime
	return prime

while i <= x**.5:					# No need to check for numbers that can't be factors
    if x%i == 0:					# Check if I is a factor
    	if is_prime(i):
       		print "Largest prime factor so far is: %d" % i 				# Show progress
    		j = i 					# Save the largest prime so far
    i = i+1

print "Done. Largest prime factor of %s is %s" % (x, j)

