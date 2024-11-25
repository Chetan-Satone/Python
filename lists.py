def common_data(list1, list2, list3): 
    for x in list1: 
        for y in list2: 
            for z in list3:
                if x == y and x==y: 
                    result = True 
                    return result 
print(common_data([1,2,3,4,5], [1,2,3,4,5],[1,2,3,4,5,5,6,7,])) 
print(common_data([1,2,3,4,5], [1,7,8,9,510], [1,2,3,4,4,5,5,6,6,7])) 
print(common_data([1,2,3,4,5], [6,7,8,9,10],[1,2,3,4,5,5,6,7,7,8,9,9])) 