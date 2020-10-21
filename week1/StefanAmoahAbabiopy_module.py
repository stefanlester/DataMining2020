#By: Amoah Stefan Ababio(ENITS 1)


'''
ListKeeper Class
'''
class ListKeeper:

    def __init__(self):  # constructor for list keeper initializing list
        self.items = {} #init list

    def add(self, name, itemsList):  #adds a list of items to the list with a given name 
        self.items[name] = itemsList

    def delete(self, name): #removes an itemsList by name
        del self.items[name]

    def show(self): #returns the list of items
        return self.items

    def append(self, name, _list): #appends to an already existing list
        old_list = self.items[name] #get the old list 
        new_list = old_list + _list #join with the new list
        self.items[name] = new_list #store the joined list

    def sort(self, name): #returns a sorted itemsList by name
        return sorted(self.items[name])


if __name__ == '__main__':

    #Test cases 
    #Test cases also done in main notebook(Assignment-01.ipynb)
    ls = ListKeeper()

    ls.add("shop", [2, 4, 1, 5])
    ls.append("shop", [8, 7, 3, 0])
    ls.add("main", [8, 7, 3, 0])
    ls.add("step", [8, 7, 3, 0])

    print(ls.show())
    print(ls.sort("shop"))

    ls.delete("step")
    print(ls.show())
