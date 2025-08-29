def to_upper(name):
    return name.upper()
def say_hello(name):
    print(f'hello, {name}')
    
if __name__=='__main__':
    name = 'filza'
    say_hello(name)
    up = to_upper(name)
    print(up)
