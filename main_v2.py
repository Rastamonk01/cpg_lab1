def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def main():

    # Greet a user
    print(greet("Alice"))

    # Simple addition
    result = add(3, 5)
    print(f"3 + 5 = {result}")

    # Simple loop
    for i in range(1, 4):
        print(f"Count: {i}")

if __name__ == "__main__":
    main()
