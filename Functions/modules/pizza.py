def makes_pizza(size, *toppings):

    print('Making the ' + str(size)+'-inch pizza' ,
          'with toppings as follows')

    for topping in toppings:
        print('-', topping)
