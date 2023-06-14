def search_replace(my_list, search, replace):
    n_list = my_list.copy()
    for x, item in list(n_list):
        if item == search:
            n_list[x] = replace
    return n_list
