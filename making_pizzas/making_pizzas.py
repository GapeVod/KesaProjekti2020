import pizzamodule

pizzamodule.make_pizza(16, 'pepperoni')
pizzamodule.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizzamodule import make_pizza

make_pizza(16, 'pepperoni')