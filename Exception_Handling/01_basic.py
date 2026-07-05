
def main():
    print("Hello ! Good Morning")
    try:
        a = int(input("Enter a number : "))
        b= 10/a
        print("The value of b is ", b)
    # except Exception as e :

    except ValueError as v:
        print("Oops! ValueError 💣" , v)
    except ZeroDivisionError as z:
        print("Oops! ZeroDivisionError 💣" , z)

    finally:
        print("Happy Coding !")

    








if __name__ =='__main__':
    main()