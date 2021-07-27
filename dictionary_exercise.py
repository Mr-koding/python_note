def remove_items_with_a(dict):
    for x in list(dict):
        if 'a' in x:
            dict.pop(x)
    return dict

print(remove_items_with_a({'name':'John','age':23, 'gender':'Male'})) 
     