def fizz_buzz():
    for i in range(1,100):
        if i % 15 == 0:
            print("fizzbuzz")
        if i % 3 == 0:
            print("fizz")
        if i % 5 == 0:
            print("buzz")
def main():
    print("Let's get started!")
    fizz_buzz()

if __name__ == "__main__":
    main()
