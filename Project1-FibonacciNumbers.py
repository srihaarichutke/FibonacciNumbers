n = 13
n1 = 0
n2 = 1
count = 0


if n<= 0:
    print("Enter a int greater than zero")
else:
    print("Fibonacci Numbers: ")
    
    
    while count < n:
          print(n1,",")

          nth = n1+n2
          n1 = n2
          n2 = nth
          count += 1
          print()
