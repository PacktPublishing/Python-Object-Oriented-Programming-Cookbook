#!/usr/bin/env python
"""
The complete code of Ch. 6, Recipe 5 -- 
Staying ready with the Object Pool pattern
"""

import random
import time

class ExpensiveObject:
    @property
    def name(self):
        try:
            return self._name
        except AttributeError:
            return None

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        try:
            del self._name
        except AttributeError:
            pass

    def __init__(self, name):
        # - Faking an irregular long creation-time for an object
        time.sleep(random.randint(0,4) + 6)
        # - After the long-running  process is complete, normal 
        #   initialization stuff happens
        self.name = name

    def some_process(self):
        print(
            '   +- %s (%s) some_process called' % 
            (self.__class__.__name__, self.name)
        )

if __name__ == '__main__':
    object_count = 8
    # Timing example: Creating 10 object-instances and keeping 
    # track of the time involved:
    start_time = time.time()
    print('Creating objects every time one is needed:')
    for i in range(1,object_count + 1):
        print('Creating object %d' % i)
        example = ExpensiveObject('object %02d' % i )
        print('+- %s (%s)' % (example.name, example))
        example.some_process()
    run_time = time.time() - start_time
    print(
        'Creating and using %d objects took %0.2f seconds' % 
        (object_count, run_time)
    )

class ExpensiveObjectPool:

    def __init__(self, count):
        self.__pool = []
        created = 0
        while created < count:
            created += 1
            print('+- Creating pool instance %d' % created)
            self.__pool.append(
                ExpensiveObject('instance %d' % created)
            )
     # The original check_out method
#    def check_out(self, *args, **kwargs):
#        instance = self.__pool.pop()
#        instance.on_checkout(*args, **kwargs)
#        return instance

    # The "safer" check_out method, raising a RuntimeError if 
    # no pool-member can be returned in a specified period of 
    # time
    def check_out(self, *args, **kwargs):
        max_wait = 10
        waited = 0
        increment = 0.25
        while self.__pool == []:
            if waited > max_wait:
                raise RuntimeError(
                    '%s.check_out waited for its maximum allowed '
                    'period of time (%s seconds) for a pool-'
                    'instance to become available.' % 
                    (self.__class__.__name__, max_wait)
                )
            waited += increment
            time.sleep(increment)
        instance = self.__pool.pop()
        instance.on_checkout(*args, **kwargs)
        return instance

    def check_in(self, used_object):
        used_object.on_checkin()
        self.__pool.append(used_object)

# - Redefining ExpensiveObject
class ExpensiveObject:

    original_name = None

    @property
    def name(self):
        try:
            return self._name
        except AttributeError:
            return None

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        try:
            del self._name
        except AttributeError:
            pass

    @property
    def in_use(self):
        try:
            return self._in_use
        except AttributeError:
            return False

    @in_use.setter
    def in_use(self, value):
        self._in_use = value

    def __init__(self, name):
        # - Faking an irregular long creation-time for an object
        time.sleep(random.randint(0,4) + 6)
        if not self.original_name:
            self.original_name = name
        self.name = name
        self.in_use = False

    def some_process(self):
        print(
            '   +- %s (%s) some_process called' % 
            (self.__class__.__name__, self.name)
        )

    def on_checkin(self):
        # - Make sure to clean up instance-state!
        print(
            '+- Checking in pool instance %s <== %s' % 
            (self.name, self.original_name)
        )
        self.in_use = False
        self.name = self.original_name

    def on_checkout(self, name):
        self.name = name
        print(
            '+- Checking out pool instance %s (%s)' % 
            (self.name, self.original_name)
        )
        self.in_use = True

if __name__ == '__main__':
    # Comparison to pooled objects
    # - Creating the initial pool takes a while still:
    pool_count = int(object_count / 4)
    start_time = time.time()
    expensive_pool = ExpensiveObjectPool(pool_count)
    run_time = time.time() - start_time
    print(
        'Creating %d objects took %0.2f seconds' % 
        (pool_count, run_time)
    )
    # - But accessing them after they've been created is a LOT 
    #   less time-consuming
    start_time = time.time()
    print('Acquiring pre-built objects:')
    for i in range(1,object_count+1):
        example = expensive_pool.check_out('check_out %s' % i )
        print('+- %s (%s)' % (example.name, example.original_name))
        example.some_process()
        expensive_pool.check_in(example)
    run_time = time.time() - start_time
    print(
        'Using %d pool-objects took %0.2f seconds' % 
        (object_count, run_time)
    )

    # - Retrieving all instances
    instances = {}
    for i in range(1,object_count+1):
        example = instances[i] = expensive_pool.check_out(
            'check_out %s' % i
        )
        print('+- %s (%s)' % (example.name, example.original_name))
        example.some_process()
