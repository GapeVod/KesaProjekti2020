def city_country(city, country):
    """asd"""
    city_country = f"{city}, {country}"
    return city_country.title()

cc = city_country('santiago', 'chile')
print(cc)
cc = city_country('oulu', 'suomi')
print(cc)
cc = city_country('helsinki', 'suomi')
print(cc)