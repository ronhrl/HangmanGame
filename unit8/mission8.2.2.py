def sort_prices(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
    return sorted_list
