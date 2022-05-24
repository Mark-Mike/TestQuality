

def func():
    try:
        for i in range(5):
            print("HI ", i)
        x = str(input("enter your name"))
        return x
    except Exception as e:
        raise e


def func():
    try:
        print("hello")
        func()
        x=2;y=0.1
    except Exception as e:
        return "Exception ", e