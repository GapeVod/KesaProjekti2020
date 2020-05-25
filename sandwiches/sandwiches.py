def make_sandwich(*innards):
    """asd"""
    print("\nMaking a sandwich with these items in it:")
    for innard in innards:
        print(f"- {innard}")

make_sandwich('cheese', 'pepperoni', 'egg')
make_sandwich('ham')
make_sandwich('pickles', 'olives')
