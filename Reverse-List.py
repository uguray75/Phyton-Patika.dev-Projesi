# to reverse the list
def funcreversing(raw_list):
    #to reverse the main list
    raw_list.reverse()
      #to find item of list
    for item in raw_list:
        #to find if item is list
        if isinstance(item, list):
            #to reverse the item list
            item.reverse()
            
            
    return raw_list



input1 = l =[[1, 2], [3, 4], [5, 6, 7]]
print(funcreversing(input1))
