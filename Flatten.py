#to flatten the list
def flatten(raw_list, newlist = []):
  #to find item of list
    for item in raw_list:
      #to find if item is list
        if isinstance(item , list):         
            flatten(item)
        #if item is not list or to had flatten, to add newlist
        else:
            newlist.append(item)
            
            
    return newlist


input1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


print(flatten(input1))
