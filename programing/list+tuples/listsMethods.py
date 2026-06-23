def listMethods():
    list = [1,2,2,3,4,5,9,8,7,6,5]
    n=len(list)
    print(list)
    newList = sorted(list)
    list.sort()
    list.append("cherry")
    list.insert(2,2)
    last=list.pop()
    list.append("cherry")
    print(last)
    # list.remove(2)
    # print(first)
    print(list)
    print(newList)
    # return list[1]
print(listMethods())