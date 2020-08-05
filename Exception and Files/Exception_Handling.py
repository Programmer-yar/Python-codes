try:
    variable=10
    print(variable+'hello')
    print(variable/2)
except ZeroDivisionError:
    print('divided by zero')
except (ValueError, TypeError):
    print('error occured')
finally:
    print('just runs it no matter what!')
