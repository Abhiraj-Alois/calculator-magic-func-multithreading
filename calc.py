import threading
import time 

class Calculator:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.num + other.num)
        
    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.num - other.num)
        
    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.num * other.num)

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.num // other.num)

# n1 = Calculator(5)
# n2 = Calculator(20)
# output = n1 // n2
# print(output.num)

def perform_operations(operation, n1, n2):
    # operation = input("Select Operation(+,-,*,//): ")
    if operation == "+":
        output = n1 + n2
    elif operation == "-":
        output = n1 - n2
    elif operation == "*":
        output = n1 * n2
    elif operation == "//":
        output = n1 // n2
    else:
        print("Invalid operation choice.")
        return None
    print(f"Result of {operation}: {output.num}")
    return output
    
def main(): 
    n1 = Calculator(int(input("Enter first number: ")))
    n2 = Calculator(int(input("Enter second number: ")))
    
    threads = []
    for operation in ['+', '-', '*', '//']:
        thread = threading.Thread(target=perform_operations, args=(operation, n1, n2))
        thread.start()
        time.sleep(1)
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
if __name__ == "__main__":
    main()