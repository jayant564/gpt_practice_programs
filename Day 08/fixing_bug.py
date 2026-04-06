# Fix this bug:
# def add_item(item, lst=[]):
#     lst.append(item)
#     return lst

def add_item(item, lst=[]):
    for i in lst:
        lst.append(item)
    return lst