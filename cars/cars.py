def car_thing(manufacturer, model_name, **car_stuff):
    """stuff"""
    car_stuff['manufacturer'] = manufacturer
    car_stuff['model_name'] = model_name
    return car_stuff

car = car_thing('subaru', 'outback',
                color = 'blue',
                tow_package = True)

print(car)

