from operator import truediv


Number=int(input("Enter the number you want to find the sum of all prime numbers less than it:"))
prime=[]
for i in range(2,Number+1):
    if i%i==0 or i%1==0:
        is_prime=True
    for j in range(2,(i//2)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime==True:
        prime.append(i)
print(f"Prime numbers less than {Number} are : {prime}")
print(f"The sum of prime numbers less than {Number} is {sum(prime)}")
