def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        print('0 1', end=' ')
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
            print(b, end=' ')
        return b 
  
# Driver Program 
  
fibonacci(25)