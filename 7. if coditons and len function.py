name=input('What is your name ?')
if len(name)<3:
    print('name should be grater than 3 characters')
elif len(name)>50:
    print('name should be less than 50 characters')
else:
    print('good name')


