#!/usr/bin/env python
"""
The complete code of Ch. 6, Recipe 2 -- 
Using the Abstract Factory pattern
"""

import abc
import platform

# - Define the various ABCs

# - The abstract classes for the elements that the factories 
#   can create

class BaseGUIButton(metaclass=abc.ABCMeta):

    def __init__(self, window=None):
        print('Creating %s' % self.__class__.__name__)
        self.window = window
        if self.window:
            self.window.buttons.append(self)

    @abc.abstractmethod
    def render(self):
        # - Rendering is dependent on the OS
        raise NotImplementedError(
            '%s.render has not been implemented as required by '
            'BaseGUIButton' % (self.__class__.__name__)
        )

class BaseGUIWindow(metaclass=abc.ABCMeta):

    def __init__(self):
        print('Creating %s' % self.__class__.__name__)
        self.buttons = []

    @abc.abstractmethod
    def render(self):
        # - Rendering is dependent on the OS
        raise NotImplementedError(
            '%s.render has not been implemented as required by '
            'BaseGUIWindow' % (self.__class__.__name__)
        )

# - The interface for the concrete factories
class BaseGUIFactory(metaclass=abc.ABCMeta):

    # - Define methods for each type of object that an instance 
    #   needs to be able to create
    @abc.abstractmethod
    def create_button(self):
        raise NotImplementedError(
            '%s.create_button has not been implemented as '
            'required by BaseGUIFactory' % (self.__class__.__name__)
        )

    @abc.abstractmethod
    def create_window(self):
        raise NotImplementedError(
            '%s.create_button has not been implemented as '
            'required by BaseGUIFactory' % (self.__class__.__name__)
        )

# - Define the concrete classes for windows and buttons in each OS supported

class WindowsButton(BaseGUIButton):
    def render(self):
        print('   +- Rendering %s' % self)

class WindowsWindow(BaseGUIWindow):
    def render(self):
        print('+- Rendering %s' % self)
        for button in self.buttons:
            button.render()

class MacOSButton(BaseGUIButton):
    def render(self):
        print('   +- Rendering %s' % self)

class MacOSWindow(BaseGUIWindow):
    def render(self):
        print('+- Rendering %s' % self)
        for button in self.buttons:
            button.render()

class LinuxButton(BaseGUIButton):
    def render(self):
        print('   +- Rendering %s' % self)

class LinuxWindow(BaseGUIWindow):
    def render(self):
        print('+- Rendering %s' % self)
        for button in self.buttons:
            button.render()

# - Define the concrete factories for each OS

class WindowsGUIFactory(BaseGUIFactory):

    def create_button(self, window=None):
        return WindowsButton(window)

    def create_window(self):
        return WindowsWindow()

class MacOSGUIFactory(BaseGUIFactory):

    def create_button(self, window=None):
        return MacOSButton(window)

    def create_window(self):
        return MacOSWindow()

class LinuxGUIFactory(BaseGUIFactory):

    def create_button(self, window=None):
        return LinuxButton(window)

    def create_window(self):
        return LinuxWindow()

# - An example of a single class that acts as a factory
class GUIFactory(BaseGUIFactory):
    if platform.system() == 'Windows':
        gui_factory = WindowsGUIFactory()
    elif platform.system() == 'Darwin':
        gui_factory = MacOSGUIFactory()
    elif platform.system() == 'Linux':
        gui_factory = LinuxGUIFactory()
    else:
        raise RuntimeError(
            'Unsupported platform (%s)' % platform_system
        )
    # - Force a specific factory-type by uncommenting one of 
    #   the following...
#    gui_factory = WindowsGUIFactory()
#    gui_factory = MacOSGUIFactory()
#    gui_factory = LinuxGUIFactory()

    def __init__(self):
        print('Creating %s' % self.__class__.__name__)
        print('+- gui_factory = %s' % self.gui_factory)

    def create_button(self, window=None):
        return self.gui_factory.create_button(window)

    def create_window(self):
        return self.gui_factory.create_window()
    

if __name__ == '__main__':

    # - Create a function to show what happens when each factory is used the same way
    def window_and_buttons():
        window = gui_factory.create_window()
        button1 = gui_factory.create_button(window)
        button2 = gui_factory.create_button(window)
        return window

    # - Decide which factory to use
    platform_system = platform.system()
    if platform_system == 'Windows':
        gui_factory = WindowsGUIFactory()
    elif platform_system == 'Darwin':
        gui_factory = MacOSGUIFactory()
    elif platform_system == 'Linux':
        gui_factory = LinuxGUIFactory()
    else:
        raise RuntimeError('Unsupported platform (%s)' % platform_system)
    print(gui_factory)
    example = window_and_buttons()
    print(example)
    example.render()

    # - Force a different factory
    gui_factory = MacOSGUIFactory()
    print(gui_factory)
    example = window_and_buttons()
    print(example)
    example.render()

    # - Using the GUIFactory class
    print('='*80)
    factory = GUIFactory()
    print('-'*80)
    window = factory.create_window()
    button1 = factory.create_button(window)
    button2 = factory.create_button(window)
    print('-'*80)
    window.render()
