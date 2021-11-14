def merger(a, b):
    new_list = []
    c = a + b
    while c:
        delete_num = min(c)
        while delete_num in c:
            new_list.append(delete_num)
            c.remove(delete_num)
    return new_list
 
 
list_a = [7, 21, 93]
list_b = [2, 58, 101, 237]
list_c = merger(list_a, list_b)
print(list_c)