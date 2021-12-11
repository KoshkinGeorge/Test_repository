class MyClass:
    name = 'bob'

    def hi(self, spec=None):
        if spec == None:
            print(f'My name is {self.name}')
        else:
            print(f'My name is {spec.name}')

    def change_name(self):
        self.name = str(input("Enter new name: "))

class f:
    pass


class Kryit(MyClass):
    name = 'Press f'


base = MyClass()
pios = Kryit()
base.hi()
pios.hi()
print(super(Kryit))
