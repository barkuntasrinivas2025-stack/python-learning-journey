try:
    number =int(input("enter a number"))
    print(1/number)
except ZeroDivisionError:
    print("your an idiot")
except ValueError:
    print("enter number only")
except Exception:
    print("somthing went wrong")
finally:
    print("all set go be paticent")