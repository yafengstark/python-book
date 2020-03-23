
##Define a function to obtain the reverse of a number
def reverse(number):
    reversenumber=''
    while number != 0:
        reversenumber+=str(number%10)
        number//=10
    reversenumber=int(reversenumber)

##Define a function to judge whether a number is a nonpalindrome
def isnonPalindrome(number):
    if number!=reverse(number):
        return True
    else:
        return False

##Define a function to judge whether a number is a prime
def isPrime(number):
    divisor=2
    while divisor<=number/2:
        if number%divisor==0:
            return False
        else:
            divisor+=1
            continue
    return True
    

    
        
##Define a main function to display 100 numbers which is nonpalindrome and prime
def main():
    count=0
    number=2                     #Begin from the smallest nonpalindrome and prime 2
    while count<100:
        if isnonPalindrome(number) and isPrime(number):
            print("%6d"%number,end='')
            count+=1
            number+=1
        else:
            number+=1
            continue             
        if count%10==0:          
            print()

main()
