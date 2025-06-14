# exception handling

def div():
    try:
        num1 = int(input("num1 = "))
        num2 = int(input("num2 = "))

        div = num1 / num2

    except ZeroDivisionError as e:
        print("error2")
    except Exception as e:
        print(e)
    else:
        return print(div)
    finally:
        print("the code run successfully")

div()