#!/usr/bin/python3
"""Based on the 8-my_class creating the same class"""


class Student():
    """Student class implemented with slight modification"""
    def __init__(self, first_name, last_name, age):
        """instantiating the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a json represnatation based on attrs
            Args:
                attrs: optional list of attributes
            returns: a json representaion of the object
        """
        dict1 = {}
        if attrs is not None and isinstance(attrs, list) and len(attrs) > 0:
            for attr in attrs:
                if hasattr(self, attr):
                    value = getattr(self, attr)
                    if isinstance(value, str):
                        value = value.replace("'", "").replace('"', "")
                    dict1[attr] = value
        elif attrs == []:
            return {}
        else:
            return self.__dict__

        return dict1


student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])
j_student_4 = student_1.to_json([])

print(j_student_1)
print(j_student_2)
print(j_student_3)
print(j_student_4)