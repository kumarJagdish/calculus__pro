# Simple Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    while True:
        print("\n===== 🧮 Simple Calculator =====")
        print("1️⃣ Addition (+)")
        print("2️⃣ Subtraction (-)")
        print("3️⃣ Multiplication (×)")
        print("4️⃣ Division (÷)")
        print("5️⃣ Exit")
        
        choice = input("👉 Choose an operation (1-5): ")

        if choice == "5":
            print("👋 Exiting... Thank you for using the calculator!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"✅ Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"✅ Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"✅ Result: {num1} × {num2} = {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"✅ Result: {num1} ÷ {num2} = {divide(num1, num2)}")
            except ValueError:
                print("⚠️ Please enter valid numbers!")
        else:
            print("⚠️ Invalid choice! Please select from 1 to 5.")

if __name__ == "__main__":
    calculator()
