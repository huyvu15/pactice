# code again algorithm list primes use statament break

# find list primes smaller or equals(bằng) n

# enter info interger n
n = int(input())
primes = [] # Create a list empty to contain elements is primes
# Create a loop for from 2 to n+1, since 1 haven't to is primes
for i in range(2, n+1):
    # continue create a loop but avail run from 2 to sqrt(i) + 1
    for j in range(2, int(i ** 0.5)+1):
        # have avail i primes
        # if i divisible(chia hết) for every number from 2 to n-1
        # i is primes
        if i % j == 0:
            break
    else: # combine when for end loop 
        primes.append(i)
# sum primes          
print(len(primes))

# the most understand else in python

# for example:
B = [0, 2, 4, 5]

for b in B:
    print(b, end = " ")
else:
    print("Printed  out all numbers") # đã in hết số
    
# else in for will run when haven't break combine

