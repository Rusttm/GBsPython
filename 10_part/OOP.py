
class Point:

    def __init__(self, name='name'):
        self.name = name
        self.color = 'white'


first_name = Point('1')
second_name = Point('2')

first_name.color = 'black'
print(f"{first_name.color= }")
print(f"{second_name.color= }")
print(Point.__dir__)


class PointLess:
    """ описание класса """

    def __init__(self):
        self.color = 'white'


first_name = PointLess()


first_name.color = 'black'
print(f"{first_name.color= }")
print(f"{second_name.color= }")

print(second_name.__dir__())

setattr(PointLess, 'new_attr', 5)
second_name = PointLess()
print(PointLess.__dir__)
print(first_name.__dir__())
print(second_name.__dir__())
# print(PointLess.new_attr)
print(getattr(first_name, 'new_attr', False))
print(getattr(second_name, 'new_attr', False))
del PointLess.new_attr
print(hasattr(second_name, 'new_attr'))
print(PointLess.__doc__)