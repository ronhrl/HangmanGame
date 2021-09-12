def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
