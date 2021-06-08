#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the number and
#for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print
#“FizzBuzz”


while number <101:
    number = 0
    number = number +1
    if number % 3 == 0 and number%5==0:
        print('Fizzbuzz')
    elif number%3 == 0:
        print('Fizz')
    elif number % 5==0:
        print('Buzz')

    else:
        print(number)
