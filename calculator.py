def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: division by zero"
    return a / b 


def main():
    print("Calculator")
    
    while True:
        cmd = input("> ")
        
        if cmd == 'quit':
            break
        
        parts = cmd.split()
        if len(parts) != 3:
            print("invalid input")
            continue
        
        op = parts[0]
        try:
            x = float(parts[1])
            y = float(parts[2])
        except:
            print("invalid numbers")
            continue
        
        if op == 'add':
            print(add(x, y))

        elif op == 'subtract':
            print(subtract(x, y))

        elif op == 'multiply':
            print(multiply(x, y))

        elif op == 'divide':
            print(divide(x, y))
        else:
            print("unknown operation")
        

if __name__ == "__main__":
    main()