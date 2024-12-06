class Calculator:
    def add(x, y):
        return x + y
    def sub_pos(x, y):
        if x > y:
            return x - y
        elif y > x:
            return y - x
    def mult(x,y):
        return x * y
    def divide(x, y):
        return x / y
    
randomshit = Calculator
print(randomshit.sub_pos(5, 9))