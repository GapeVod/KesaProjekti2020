def make_shirt(size, text):
    """make shirt"""
    print(f"\nThe size of the shirt is {size.title()}.")
    print(f"Text printed on the shirt says {text.title()}")

make_shirt('l', 'shirt text')
make_shirt(size = 'm', text = 'keyword text')
