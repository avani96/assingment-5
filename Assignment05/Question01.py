from ast import literal_eval

class Power:
    
    def power_number(self,x,n):
        if isinstance(x, (int,float)):        # check whether x object belong to int, float class    
            if isinstance(n, (int, float)):   # check whether x object belong to int, float class 
                if x == 0:
                    if n <=0:
                        return ("Math Domin Error ")   # checking its belong to maths domin or not
                    else:
                        return 0                      
                elif n == 0:                   #  checking whether power is 0 or not  
                    return 1
                elif n < 0:                    # checking whether power is inverse or not       
                    n = abs(n)
                    x = 1/(x**n)
                    return x
                else:
                    res = x**n
                    return res
            else: 
                return ("Not a valid number")      
        else: 
            return ("Not a valid number")
    def __str__(self):
        return ("Sample Inputs are x = {} and n = {}".format(x, n))
    
x = literal_eval(input("Enter base number (x) :- "))     # using literal_eval with input to take input from user
n = literal_eval(input("Enter power number (n) :- "))
obj1 = Power()
result = obj1.power_number(x,n)
print(obj1)
print("The Expected output = {}".format(result)) 