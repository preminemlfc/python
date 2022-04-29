user_input = int(input('Please enter ages of class member. Type -1 to end:>'))
ages= []
while user_input>0:
    ages.append(user_input)
    user_input = int(input('next age:>'))
    print('the ages are', ages)

count=0
class_names=[]
name= input('Pleas enter the name, type n to stop')
while name != 'n':
    count+=1
    class_names.append(name)
    print(f'{name} has been added')
    name= input('next name>:')
print(f'There are {count} people in the class, they are {class_names}')