#Write A function to check if a number is prime or not
#Use that function, and print first 100 prime numbers

#Definition: 
#A prime number is a natural number greater than 1 
#that has no positive divisors other than 1 and itself. 
#The first few prime numbers are {2, 3, 5, 7, 11, ….}.


def prime():
    num = int(input("Enter the number : "))

    for i in range(2,num):
        if num % i == 0:
            print("It is not a prime number!")
            break

    else:
        print("It is a prime number!")
        for number in range(num+100):
            if(number>num):
                for i in range(2,number):
                    if(number%i)==0:
                        break
                else:
                    print(number, end = '  ')
prime()