#!/usr/bin/env python
"""
The complete code of Ch. 6, Recipe 4 -- 
Working with the Builder pattern
"""

import abc
from datetime import datetime

datetime_format = '%Y-%m-%d %H:%M:%S'
datetime_display = '%m/%d, %H:%M'

class HasSchedule(metaclass=abc.ABCMeta):

    @property
    def start(self):
        try:
            return self._start
        except AttributeError:
            return None

    @start.setter
    def start(self, value):
        if type(value) == str:
            value = datetime.strptime(value, datetime_format)
        self._start = value

    @property
    def end(self):
        try:
            return self._end
        except AttributeError:
            return None

    @end.setter
    def end(self, value):
        if type(value) == str:
            value = datetime.strptime(value, datetime_format)
        self._end = value

    def __init__(self, start, end):
        self.start = start
        self.end = end

class IsSchedulable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def schedule(self, itinerary:(type,), start:(datetime,), end:(datetime,)):
        pass

class HasLocation(metaclass=abc.ABCMeta):

    @property
    def location(self):
        try:
            return self._location
        except AttributeError:
            return None

    @location.setter
    def location(self, value):
        self._location = value

    def __init__(self, location):
        self.location = location

class Exhibit(HasSchedule, HasLocation):
    @property
    def exhibitors(self):
        try:
            return self._exhibitors
        except AttributeError:
            self._exhibitors = {}
            return self._exhibitors

    @property
    def dict(self):
        return {
            'location':self.location,
            'start':str(self.start),
            'end':str(self.end),
            'exhibitors':{
                i.name:i.dict for i in self.exhibitors.values()
            },
        }

    def __init__(self, location, start, end):
        HasLocation.__init__(self, location)
        HasSchedule.__init__(self, start, end)

    def add_exhibitor(self, name:(str,), location=None, start=None, end=None):
        exhibitor = Exhibitor(name, self, location, start, end)
        self.exhibitors[name] = exhibitor

class Convention(HasSchedule, HasLocation):
    @property
    def events(self):
        try:
            return self._events
        except AttributeError:
            self._events = []
            return self._events

    @property
    def exhibit(self):
        try:
            return self._exhibit
        except AttributeError:
            return None

    @exhibit.setter
    def exhibit(self, value):
        self._exhibit = value

    @property
    def name(self):
        try:
            return self._name
        except AttributeError:
            self._name = None

    @name.setter
    def name(self, value:(str,)):
        # TODO: Type-and value-check the value
        self._name = value

    @name.deleter
    def name(self):
        try:
            del self._name
        except AttributeError:
            pass

    def __init__(
        self, name:(str,), exhibit:(Exhibit,None)=None, 
        location=None, start:(datetime,str,None)=None, 
        end:(datetime,str,None)=None
    ):
        self.name = name
        self.exhibit = exhibit
        HasLocation.__init__(self, location)
        HasSchedule.__init__(self, start, end)

    def add_event(self, name, location, start, end):
        event = Event(name, location, start, end)
        self.events.append(event)

    def add_exhibit(self, location, start, end):
        self.exhibit = Exhibit(location, start, end)

    def add_exhibitor(self, name:(str,), location, start=None, end=None):
        if self.exhibit:
            exhibitor = Exhibitor(name, self.exhibit, location, start, end)
            self.exhibit.exhibitors[name] = exhibitor
        else:
            raise AttributeError(
                'The "%s" %s was not created with an exhibit, so '
                'adding an exhibitor is not allowed' % 
                (self.name, self.__class__.__name__)
            )

    @property
    def dict(self):
        return {
            'name':self.name,
            'exhibit':self.exhibit.dict if self.exhibit else None,
            'events':[i.dict for i in self.events],
        }

    def print_details(self):
        print('#'*66)
        print(('# %s ' % self.name).ljust(65, ' ') + '#')
        if self.events:
            print('#' + '='*64 + '#')
            print('EVENTS:')
            for event in sorted(self.events, key=lambda e: e.start):
                print(
                    ('%s ' % event.location).ljust(16,'.')
                    + (
                        ' %s-%s ' % (
                            event.start.strftime(datetime_display), 
                            event.end.strftime('%H:%M')
                        )
                    ).ljust(23, '.')
                    + (' %s ' % event.name[0:25]).ljust(25, ' ')
                )
        if self.exhibit:
            print('#' + '='*64 + '#')
            print('EXHIBITORS:')
            print(
                'Open in %s from %s until %s' % 
                (
                    self.exhibit.location, 
                    self.exhibit.start.strftime(datetime_display), 
                    self.exhibit.end.strftime(datetime_display), 
                )
            )
            for name in sorted(self.exhibit.exhibitors):
                exhibitor = self.exhibit.exhibitors[name]
                if exhibitor.start == self.exhibit.start and exhibitor.end == self.exhibit.end:
                    print(
                        ('%s ' % exhibitor.location).ljust(16, '.')
                        + (' %s ' % exhibitor.name[0:50]).ljust(50, ' ')
                    )
                else:
                    print(
                        ('%s ' % exhibitor.location).ljust(16, '.')
                        + (
                            ' [limited] %s ' % exhibitor.name[0:50]
                        ).ljust(50, ' ')
                    )
        print('#'*66)

    @classmethod
    def get(cls, convention=None):
        # - The convention data. Though these are retrieved from 
        #   local JSON data-files, they are roughly equivalent to 
        #   the results that would be expected if the same data 
        #   were retrieved from a database
        with open('C06R03_Convention.json', 'r') as confile:
            print('Loading main convention data')
            convention = json.load(confile)
            print('Main convention data loaded')
        new_instance = cls(**convention)

        # - Ditto for the exhibit data...
        with open('C06R03_Exhibit.json', 'r') as exhfile:
            print('Loading main convention exhibit data')
            exhibit = json.load(exhfile)
            print('Main convention exhibitors data loaded')
            new_instance.exhibit = Exhibit(**exhibit)

        # - ...and the exhibitors...
        with open('C06R03_Exhibitors.json', 'r') as exsfile:
            print('Loading main convention exhibitors data')
            exhibitors = json.load(exsfile)
            print('Main convention exhibit exhibitors loaded')
            for exhibitor in exhibitors:
                new_instance.exhibit.add_exhibitor(**exhibitor)

        # - ...and the events
        with open('C06R03_Events.json', 'r') as evtfile:
            print('Loading main convention events data')
            events = json.load(evtfile)
            print('Main convention events loaded')
            for event in events:
                new_instance.add_event(**event)

        print('new_instance: %s' % new_instance)
        return new_instance

class Exhibitor(HasLocation, HasSchedule, IsSchedulable):
    def __init__(self, name, exhibit=None, location=None, start=None, end=None):
        self.name = name
        HasLocation.__init__(self, location)
        if exhibit:
            if not start:
                start = exhibit.start
            if not end:
                end = exhibit.end
        if start and end:
            HasSchedule.__init__(self, start, end)

    @property
    def dict(self):
        return {
            'name':self.name,
            'location':self.location,
            'start':str(self.start),
            'end':str(self.end),
        }

    def schedule(self, itinerary):
        # - Start and end are acquired from the event
        pass

class Event(HasLocation, HasSchedule, IsSchedulable):
    def __init__(self, name, location, start, end):
        self.name = name
        HasLocation.__init__(self, location)
        HasSchedule.__init__(self, start, end)

    @property
    def dict(self):
        return {
            'name':self.name,
            'location':self.location,
            'start':str(self.start),
            'end':str(self.end),
        }

    def schedule(self, itinerary):
        # - Start and end are acquired from the event
        pass

# - A free-standing function approach, which is common to many 
#   Python modules as a builder- (or at least builder-like-) 
#   implementation for creating complext object hierarchies
def get_convention():
    # - The convention data. Though these are retrieved from 
    #   local JSON data-files, they are rouchly equivalent to 
    #   the results that would be expected if the same data 
    #   were retrieved from a database
    with open('C06R03_Convention.json', 'r') as confile:
        print('Loading main convention data')
        convention = json.load(confile)
        print('Main convention data loaded')
    new_instance = Convention(**convention)

    # - Ditto for the exhibit data...
    with open('C06R03_Exhibit.json', 'r') as exhfile:
        print('Loading main convention exhibit data')
        exhibit = json.load(exhfile)
        print('Main convention exhibitors data loaded')
        new_instance.exhibit = Exhibit(**exhibit)

    # - ...and the exhibitors...
    with open('C06R03_Exhibitors.json', 'r') as exsfile:
        print('Loading main convention exhibitors data')
        exhibitors = json.load(exsfile)
        print('Main convention exhibit exhibitors loaded')
        for exhibitor in exhibitors:
            new_instance.exhibit.add_exhibitor(**exhibitor)

    # - ...and the events
    with open('C06R03_Events.json', 'r') as evtfile:
        print('Loading main convention events data')
        events = json.load(evtfile)
        print('Main convention events loaded')
        for event in events:
            new_instance.add_event(**event)

    print('new_instance: %s' % new_instance)
    return new_instance

if __name__ == '__main__':

    import json

    object_con = Convention.get()

#    object_con.print_details()

#    object_con = get_convention()

#    object_con.print_details()

    print(json.dumps(object_con.dict, indent=4))
