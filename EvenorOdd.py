def EvenorOdd(num):
    if num % 2 == 0:
        print(num, " is even number")
    else:
        print(num,"is Odd Number ")
    return 

num = int(input("Enter a Number to check Even or Odd "))
EvenorOdd(num)