# Fix this bug:
# def add_item(item, lst=[]):
#     lst.append(item)
#     return lst

def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
