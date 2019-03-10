#!/usr/bin/env python
"""
The complete code of Ch. 3, Recipe 5 -- Creating interface requirements
"""

# - Import the abc module to provide abstraction mechanisms
import abc

class BasePerson(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can represent any of several types 
of people in a system
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

    # - Full name, an abstract property definition here, 
    #   that will require an implementation in derived classes
    @abc.abstractproperty
    def full_name(self):
        # - Methods in Python, even if they are abstract, 
        #   must have *something* in their body, even if 
        #   it's just a "pass" statement. Just to be on 
        #   the safe side, we'll raise a NotImplementedError 
        #   in abstract members...
        raise NotImplementedError(
            '%s.full_name has not been implemented, as required '
            'by BasePerson' % (self.__class__.__name__)
        )

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
    # - This is made abstract because *how* the derived classes'
    #   string-representations get rendered is expected to vary.
    # - Note that we're *not* raising a NotImplementedError here; 
    #   we *could*, as was done above with full_name, but it's 
    #   not *required*
    @abc.abstractmethod
    def __str__(self):
        """
Requires implementation of a __str__ method in derived classes.
The output should look something like:
<[ClassName] at [id(self) as hex-number] ([property=value...])>
        """
        pass

    def send_email(self, message):
        raise NotImplementedError(
            '%s.send_email has not been implemented yet.' %
            (self.__class__.__name__)
        )

class Faculty(BasePerson):
    """
Represents a faculty-member in a post-secondary context/setting
    """

    # PROPERTY DEFINITIONS
    # - Full name, a calculated read-only property
    #   Implemented as required by BasePerson, includes 
    #   student_id
    @property
    def full_name(self):
        results = []
        if self.prefix != None:
            results.append(self.prefix)
        if self.given_name != None:
            results.append(self.given_name)
        if self.initials != None:
            results.append(self.initials)
        if self.family_name != None:
            results.append(self.family_name)
        if self.suffix != None:
            results.append(', %s' % self.suffix)
        if results:
            return ' '.join(results).replace(' ,', ',')

    # - Department -- The department that the faculty-person 
    #   is a member of
    @property
    def department(self):
        try:
            return self._department
        except AttributeError:
            return None
    @department.setter
    def department(self, value):
        self._department = value
    @department.deleter
    def department(self):
        try:
            del self._department
        except AttributeError:
            pass

    # - Prefix -- The prefix of the faculty-member, if any
    @property
    def prefix(self):
        try:
            return self._prefix
        except AttributeError:
            return None
    @prefix.setter
    def prefix(self, value):
        self._prefix = value
    @prefix.deleter
    def prefix(self):
        try:
            del self._prefix
        except AttributeError:
            pass

    # - Suffix -- The suffix of the faculty-member, if any
    @property
    def suffix(self):
        try:
            return self._suffix
        except AttributeError:
            return None
    @suffix.setter
    def suffix(self, value):
        self._suffix = value
    @suffix.deleter
    def suffix(self):
        try:
            del self._suffix
        except AttributeError:
            pass

    # OBJECT INITIALIZATION
    def __init__(self, 
        # - Putting "prefix" first
        prefix=None, 
        # - Arguments from Person
        given_name=None, initials=None, family_name=None, 
        # - More local arguments
        suffix=None, 
        # - More Person arguments
        email_address=None,
        # - Other faculty-specific arguments
        department=None
    ):
        """
Object initialization
prefix ............ (str|None, optional, defaults to None) The 
                    prefix (Dr., Prof., etc.) of the faculty-
                    member the instance represents, if any.
given_name ........ (str|None, optional, defaults to None) The 
                    given (first) name of the faculty-member the 
                    instance represents.
initials .......... (str|None, optional, defaults to None) The 
                    middle initial(s) of the faculty-member the 
                    instance represents.
family_name ....... (str|None, optional, defaults to None) The 
                    family (last) name of the faculty-member the 
                    instance represents.
suffix ............ (str|None, optional, defaults to None) The 
                    suffix (PhD, etc.) of the faculty-member the 
                    instance represents, if any.
email_address ..... (str|None, optional, defaults to None) The 
                    email address of the faculty-member the 
                    instance represents.
department ........ (str|None, optional, defaults to None) The 
                    department that the faculty-member the 
                    instance represents is a member of, if any.
        """
        # - We can use super() to call the parent class' __init__ 
        #   because there's only one parent class...
        super().__init__(
            given_name, initials, family_name, email_address
        )
        # - But we ALSO need to initialize properties that are 
        #   members of THIS class
        self.department = department
        self.prefix = prefix
        self.suffix = suffix

    def get_schedule(self):
        raise NotImplementedError(
            '%s.get_schedule has not been implemented yet.' %
            (self.__class__.__name__)
        )

    # STRING RENDERING (a convenience for debugging/display 
    # purposes)
    # Implemented as required by BasePerson, includes student_id
    def __str__(self):
        return (
            '<%s at %s (prefix=%s given_name=%s initials=%s '
            'family_name=%s suffix=%s email_address=%s '
            'department=%s)>' % 
            (
                self.__class__.__name__, hex(id(self)), 
                self.prefix, self.given_name, self.initials, 
                self.family_name, self.suffix, 
                self.email_address, self.department
            )
        )

class Staff(BasePerson):
    """
Represents a staff-member in a post-secondary context/setting
    """

    # PROPERTY DEFINITIONS
    # - Full name, a calculated read-only property
    #   Implemented as required by BasePerson, includes 
    #   student_id
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

    # - Department -- The department that the faculty-person 
    #   is a member of
    @property
    def department(self):
        try:
            return self._department
        except AttributeError:
            return None
    @department.setter
    def department(self, value):
        self._department = value
    @department.deleter
    def department(self):
        try:
            del self._department
        except AttributeError:
            pass

    # - Prefix -- The prefix of the faculty-member, if any
    @property
    def prefix(self):
        try:
            return self._prefix
        except AttributeError:
            return None
    @prefix.setter
    def prefix(self, value):
        self._prefix = value
    @prefix.deleter
    def prefix(self):
        try:
            del self._prefix
        except AttributeError:
            pass

    # - Suffix -- The suffix of the faculty-member, if any
    @property
    def suffix(self):
        try:
            return self._suffix
        except AttributeError:
            return None
    @suffix.setter
    def suffix(self, value):
        self._suffix = value
    @suffix.deleter
    def suffix(self):
        try:
            del self._suffix
        except AttributeError:
            pass

    # OBJECT INITIALIZATION
    def __init__(self, 
        # - Arguments from Person
        given_name=None, initials=None, family_name=None, 
        email_address=None,
        # - Other staff-specific arguments
        department=None
    ):
        """
Object initialization
given_name ........ (str|None, optional, defaults to None) The 
                    given (first) name of the faculty-member the 
                    instance represents.
initials .......... (str|None, optional, defaults to None) The 
                    middle initial(s) of the faculty-member the 
                    instance represents.
family_name ....... (str|None, optional, defaults to None) The 
                    family (last) name of the faculty-member the 
                    instance represents.
email_address ..... (str|None, optional, defaults to None) The 
                    email address of the faculty-member the 
                    instance represents.
department ........ (str|None, optional, defaults to None) The 
                    department that the faculty-member the 
                    instance represents is a member of, if any.
        """
        # - We can use super() to call the parent class' __init__ 
        #   because there's only one parent class...
        super().__init__(
            given_name, initials, family_name, email_address
        )
        # - But we ALSO need to initialize properties that are 
        #   members of THIS class
        self.department = department

    def get_schedule(self):
        raise NotImplementedError(
            '%s.get_schedule has not been implemented yet.' %
            (self.__class__.__name__)
        )

    # STRING RENDERING (a convenience for debugging/display 
    # purposes)
    # Implemented as required by BasePerson, includes student_id
    def __str__(self):
        return (
            '<%s at %s (given_name=%s initials=%s family_name=%s '
            'email_address=%s department=%s)>' % 
            (
                self.__class__.__name__, hex(id(self)), 
                self.given_name, self.initials, self.family_name, 
                self.email_address, self.department
            )
        )

class Student(BasePerson):
    """
Represents a Student in a post-secondary context/setting
    """
    # PROPERTY DEFINITIONS
    # - Full name, a calculated read-only property
    #   Implemented as required by BasePerson, includes 
    #   student_id
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
        # - We can use super() to call the parent class' __init__ 
        #   because there's only one parent class...
        super().__init__(
            given_name, initials, family_name, email_address
        )
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
    # purposes)
    # Implemented as required by BasePerson, includes student_id
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

    class ExamplePerson(BasePerson):
        pass

    try:
        me = ExamplePerson('Brian', 'D', 'Allbee', None)
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, error))

    my_student = Student(
        1, 'Brooke', None, 'Owens', None, 'CIS', None
    )
    print(my_student)
    print(my_student.full_name)

    my_faculty = Faculty(
        'Dr.', 'Chris', 'L', 'Powell', 'PhD', 'clpowell@uu.edu', 
        'CIS'
    )
    print(my_faculty)
    print(my_faculty.full_name)

    my_staff = Staff(
        'Edwin', None, 'Coyne', 'ecoyne@uu.edu', 'Lab Assistant'
    )
    print(my_staff)
    print(my_staff.full_name)
