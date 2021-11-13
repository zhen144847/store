
def factorial_iteration(n):

        result = 1
        for i in range(1, n + 1):
            result *= i
        return  result
print("",factorial_iteration(19))