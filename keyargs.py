'''def myfunc(**kwargs):
    print(kwargs)

myfunc(fruit='apple', veggie='lettuce')'''

def myfunc1(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))  #has to be args first then kwargs second
myfunc1(10,20,30,fruit='orange',food='eggs',animal='dog')