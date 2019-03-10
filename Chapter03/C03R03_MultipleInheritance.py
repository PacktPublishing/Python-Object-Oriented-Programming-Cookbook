#!/usr/bin/env python
"""
The complete code of Ch. 3, Recipe 3 -- Inheriting from 
    multiple parent classes
"""

class DataObject:
    """
Provides common functionality for objects that can store their 
state-data in some kind of back-end data-store (a database, a 
file-system, whatever).
    """

    # OBJECT INITIALIZATION
    def __init__(self):
        print(
            '%s calling DataObject.__init__' % 
            self.__class__.__name__
        )

    # NOTE: The members implemented here don't actually DO 
    #       anything at this point, but can be called to 
    #       prove that they are being inherited...

    # CRUD Operations (Create, Read, Update and Delete)
    # - Create
    def create(self):
        raise NotImplementedError(
            '%s.create (from DataObject) has not been '
            'implemented yet' % (self.__class__.__name__)
        )
    # - Read -- defined as a class-method so that no existing 
    #   instance is required to read an instance
    @classmethod
    def read(cls):
        raise NotImplementedError(
            '%s.read (from DataObject) has not been '
            'implemented yet' % (cls.__name__)
        )
    # - Update
    def update(self):
        raise NotImplementedError(
            '%s.update (from DataObject) has not been '
            'implemented yet' % (self.__class__.__name__)
        )
    # - Delete -- also defined as a class-method so that no 
    #   existing instance is required for deletion
    @classmethod
    def delete(cls):
        raise NotImplementedError(
            '%s.delete (from DataObject) has not been '
            'implemented yet' % (cls.__name__)
        )

class Person:
    """
Represents a Person
    """

    # PROPERTY DEFINITIONS
    # - Email address
    @property
    def email_address(self):
        try:
            return self._email_address
        except AttributeError:
            return None
    @email_address.setter
    def email_address(self, value):
        self._email_address = value
    @email_address.deleter
    def email_address(self):
        try:
            del self._email_address
        except AttributeError:
            pass

    # - Family name
    @property
    def family_name(self):
        try:
            return self._family_name
        except AttributeError:
            return None
    @family_name.setter
    def family_name(self, value):
        self._family_name = value
    @family_name.deleter
    def family_name(self):
        try:
            del self._family_name
        except AttributeError:
            pass

    # - Full name, a calculated read-only property
    @property
    def full_name(self):
        results = []
        if self.given_name != None:
            results.append(self.given_name)
        if self.initials != None:
            results.append(self.initials)
        if self.family_name != None:
            results.append(self.family_name)
        if results:
            return ' '.join(results)

    # - Given name
    @property
    def given_name(self):
        try:
            return self._given_name
        except AttributeError:
            return None
    @given_name.setter
    def given_name(self, value):
        self._given_name = value
    @given_name.deleter
    def given_name(self):
        try:
            del self._given_name
        except AttributeError:
            pass

    # - Initials
    @property
    def initials(self):
        try:
            return self._initials
        except AttributeError:
            return None
    @initials.setter
    def initials(self, value):
        self._initials = value
    @initials.deleter
    def initials(self):
        try:
            del self._initials
        except AttributeError:
            pass

    # OBJECT INITIALIZATION
    def __init__(self, 
        given_name=None, initials=None, family_name=None, 
        email_address=None
    ):
        """
Object initialization
given_name ........ (str|None, optional, defaults to None) The 
                    given (first) name of the person the 
                    instance represents.
initials .......... (str|None, optional, defaults to None) The 
                    middle initial(s) of the person the 
                    instance represents.
family_name ....... (str|None, optional, defaults to None) The 
                    family (last) name of the person the 
                    instance represents.
email_address ..... (str|None, optional, defaults to None) The 
                    email address of the person the 
                    instance represents.
        """
        self.given_name = given_name
        self.initials = initials
        self.family_name = family_name
        self.email_address = email_address

    # STRING RENDERING (a convenience for debugging/display 
    # purposes)
    def __str__(self):
        return (
            '<%s at %s (given_name=%s initials=%s '
            'family_name=%s email_address=%s)>' % 
            (
                self.__class__.__name__, hex(id(self)), 
                self.given_name, self.initials, 
                self.family_name, self.email_address
            )
        )

    def send_email(self, message):
        raise NotImplementedError(
            '%s.send_email has not been implemented yet.' %
            (self.__class__.__name__)
        )

class Student(Person, DataObject):
    """
Represents a Student in a post-secondary context/setting
    """

    # PROPERTY DEFINITIONS
    # - Full name, a calculated read-only property
    #   OVERRIDDEN from Person to include student_id
    @property
    def full_name(self):
        results = []
        if self.given_name != None:
            results.append(self.given_name)
        if self.initials != None:
            results.append(self.initials)
        if self.family_name != None:
            results.append(self.family_name)
        if self.student_id != None:
            results.append('[%s]' % self.student_id)
        if results:
            return ' '.join(results)

    # - Major -- The declared major for a student, if any
    @property
    def major(self):
        try:
            return self._major
        except AttributeError:
            return None
    @major.setter
    def major(self, value):
        self._major = value
    @major.deleter
    def major(self):
        try:
            del self._major
        except AttributeError:
            pass

    # - Minor -- The declared minor for a student, if any
    @property
    def minor(self):
        try:
            return self._minor
        except AttributeError:
            return None
    @minor.setter
    def minor(self, value):
        self._minor = value
    @minor.deleter
    def minor(self):
        try:
            del self._minor
        except AttributeError:
            pass

    # - Student ID -- The unique identifier of a student
    @property
    def student_id(self):
        try:
            return self._student_id
        except AttributeError:
            return None
    @student_id.setter
    def student_id(self, value):
        self._student_id = value
    @student_id.deleter
    def student_id(self):
        try:
            del self._student_id
        except AttributeError:
            pass

    # OBJECT INITIALIZATION
    def __init__(self, 
        student_id=0,
        # - Arguments from Person
        given_name=None, initials=None, family_name=None, 
        email_address=None,
        # - Other student-specific arguments
        major=None, minor=None
    ):
        """
Object initialization
student_id ........ (int|None, optional, defaults to 0 [zero]) 
                    The unique identifying number of the student
given_name ........ (str|None, optional, defaults to None) The 
                    given (first) name of the student the 
                    instance represents.
initials .......... (str|None, optional, defaults to None) The 
                    middle initial(s) of the student the 
                    instance represents.
family_name ....... (str|None, optional, defaults to None) The 
                    family (last) name of the student the 
                    instance represents.
email_address ..... (str|None, optional, defaults to None) The 
                    email address of the student the 
                    instance represents.
major ............. (str|None, optional, defaults to None) The 
                    declared major (if any) of the student the 
                    instance represents.
minor ............. (str|None, optional, defaults to None) The 
                    declared minor (if any) of the student the 
                    instance represents.
        """
        # - We can't use super in this case, because there are 
        #   multiple parent classes. Each parent's __init__ has 
        #   to be called explicitly instead:
        Person.__init__(
            self, given_name, initials, family_name, email_address
        )
        DataObject.__init__(self)
        # - But we ALSO need to initialize properties that are 
        #   members of THIS class
        self.student_id = student_id
        self.major = major
        self.minor = minor

    def get_schedule(self):
        raise NotImplementedError(
            '%s.get_schedule has not been implemented yet.' %
            (self.__class__.__name__)
        )

    # STRING RENDERING (a convenience for debugging/display 
    # purposes) OVERRIDDEN from Person to include Student-
    # specific data
    def __str__(self):
        return (
            '<%s at %s (student_id=%s given_name=%s initials=%s '
            'family_name=%s email_address=%s major=%s '
            'minor=%s)>' % 
            (
                self.__class__.__name__, hex(id(self)), 
                self.student_id, self.given_name, self.initials, 
                self.family_name, self.email_address, 
                self.major, self.minor
            )
        )

if __name__ == '__main__':

    my_student = Student(
        1, 'Brooke', None, 'Owens', None, 'CIS', None
    )
    print(my_student)

    try:
        my_student.send_email('some message')
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))

    try:
        my_student.create()
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))

    try:
        Student.read()
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))

    try:
        my_student.update()
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))

    try:
        Student.delete()
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))

    person = Person()
    try:
        person.create()
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))

    # - How Python solves the diamond problem
    class RootClass:
        def some_method(self):
            print('RootClass.some_method called')

    class SubclassA(RootClass):
        def some_method(self):
            print('SubclassA.some_method called')

    class SubclassB(RootClass):
        def some_method(self):
            print('SubclassB.some_method called')

    class FinalClass1(SubclassA, SubclassB):
        pass

    class FinalClass2(SubclassB, SubclassA):
        pass

    final_instance1 = FinalClass1()
    final_instance1.some_method()
    final_instance2 = FinalClass2()
    final_instance2.some_method()
