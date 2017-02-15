# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them

number = input('How many Fibonnaci numbers do you want to generate? \n>')

def Fib(n):
    F_list = [1, 1]
    if n == 0 :
        return []
    elif n == 1:
         return [1]
    else:
        for i in range(0, n-2):
            x = F_list[i] +F_list[i+1]
            F_list.append(x)
        return F_list

if number < 0:
    print 'Enter a number bigger than 0.'
else:
    print Fib(number)
