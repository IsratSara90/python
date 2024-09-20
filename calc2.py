# main.py
import calc1  # Importing the calculator module

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Choose an operation (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {calc1.add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {calc1.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {calc1.multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {calc1.divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
