def sum_numbers(*args):
    return sum(args)


def get_multiplied_amount(*args):
    multiplied = 1
    for arg in args:
        multiplied *= arg

    return multiplied


def word_concatenator(*args):
    concatenated = ""
    for arg in args:
        concatenated += arg

    return concatenated


def inverted_word_factory():
    def inverted_word(word):
        return word[::-1]

    return inverted_word


def dictionary_separator(**kwargs):
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    return (keys, values)


def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs):
        return None

    modified_dict = {}
    for i, (key, value) in enumerate(kwargs.items()):
        if i < len(args):
            modified_dict[key] = args[i]

    return modified_dict


def purchase_logger(**kwargs):
    quantity = kwargs.get("quantity")
    name = kwargs.get("name")
    price = kwargs.get("price")
    purchase_log = f"{quantity} {name} bought by {price}"

    return purchase_log


def world_cup_logger(country, *args):
    sorted_years = sorted(args)
    years_string = ", ".join(str(year) for year in sorted_years)
    log = f"{country} - {years_string}"

    return log
