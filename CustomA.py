import pickle
from pynamodb.attributes import BinaryAttribute, UnicodeAttribute
from pynamodb import attributes
from pynamodb.models import Model

# class Color(object):
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "<Color: {}>".format(self.name)


# class PickleAttribute(BinaryAttribute):
#     def serialize(self, value):
#         return super(PickleAttribute, self).serialize(pickle.dumps(value))

#     def deserialize(self, value):
#         return pickle.loads(super(PickleAttribute, self).deserialize(value))


# obj: PickleAttribute() = Color("Red")

# print(obj)

grocery: attributes.ListAttribute = ["bread", 1, "Milk", 2]

print(grocery)

class OfficeEmployeeMap(attributes.MapAttribute):
    office_employee_id = attributes.NumberAttribute()
    person = UnicodeAttribute()

emp1: OfficeEmployeeMap = (123, "abc")
emp2: OfficeEmployeeMap = (234, "abc2")

officeEmp: attributes.ListAttribute(of=OfficeEmployeeMap) = [emp1, emp2]

print(officeEmp)

class CarInfo(attributes.DynamicMapAttribute):
    make = UnicodeAttribute(null=False)
    model = UnicodeAttribute(null=True)

    def __str__(self):
        return str(self.attribute_values)

car = CarInfo(make='Make-A', model='Model-A', year=1975)
other_car = CarInfo(make='Make-A', model='Model-A', year=1975, seats=3)

print(other_car)