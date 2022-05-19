import os

def main():
    print("This is my first test procedure...")
    print("git push my@github.com")
    print(os.getcwd())
    print(os.__doc__)
    print(dir(os))
    str1 = "hello, python env is build..."
    str2 = 'env'
    print(str2 in str1)
    print('path' in dir(os))


if __name__ == "__main__":
    main()