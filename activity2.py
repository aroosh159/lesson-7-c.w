#empty dictionary
my_dict = {}
#dictionary with integers
my_dict = {1:'apple',2:'banana'}
#mixed dictionary
my_dict = {'name':'Ali',1:[2,3,4]}
my_dict = {'name':'Aroosh','age':12}
#output
print(my_dict['name'])
print(my_dict['age'])
##update value
my_dict['age']=13
print(my_dict['age']) 
print(my_dict)
#add item
my_dict['address'] = 'Faisalabad'
#remove item
my_dict.pop('age')
print(my_dict)
#access to a item
print("Address :",my_dict.get('address'))
#remove all the items
my_dict.clear()
print(my_dict)