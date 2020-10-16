class ListKeeper:
    
    #function show returns all list names with .keys
    def show():
        print(dict0.keys())

    def add(name, list):
        dict0[name] = list

    def delete(name):
        dict0.pop(name)

    def sort(name):
        print(dict0[name])

    def append(name,list):
        dict0[name].extend(list)



#example = [1,2,3,4,5]

dict0 = {}

dict0["example"] = [1,2,3,4,5]