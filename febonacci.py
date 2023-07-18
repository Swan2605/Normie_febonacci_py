def febonacci(n):
   '''This function solves for the febonacci value for the required number.'''
   if(n==0):
    return 0
   elif(n==1):
    return 1
   else: 
    return febonacci(n-1) + febonacci(n-2)

x = int(input("Enter a number : "))
print(febonacci(x))


print(febonacci.__doc__)
