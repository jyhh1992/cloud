

def remove_if_exists(mylist, item):
    """ Remove item from mylist if it exists, do nothing otherwise """
    to_remove = []
    for i in range(len(mylist)):
        if mylist[i] == item:
            to_remove.append(mylist[i])
            
    for el in to_remove:
        mylist.remove(el)
        
