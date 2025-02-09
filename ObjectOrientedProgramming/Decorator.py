
def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("**You add sprinkles**")
        func(*args,**kwargs)
    return wrapper


def add_fuzz(func):
    def wrapper(*args,**kwargs):
        print("You added Fuzz")
        func(*args,**kwargs)
    return wrapper


@add_sprinkles
@add_fuzz
def get_icecream(flavor):
    print(f"Here is {flavor} Ice Cream")

get_icecream('ChocoChips')