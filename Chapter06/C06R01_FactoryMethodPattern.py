#!/usr/bin/env python
"""
The complete code of Ch. 6, Recipe 1 -- 
Decoupling object construction with the Factory Method pattern
"""

# - Imports required for abstract classes, methods, etc.
import abc

# - Placeholder classes for assets and their superclasses. The 
#   names are the same as those in 
#   C04R03_SubclassRegistrationMetaclass.py

class BaseAsset(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements and type-
identity for objects that can represent a digital asset
    """
    # TODO: Define concrete and abstract functionality when/if/as 
    #       needed. For now, just pass
    def __init__(self, *args, **kwargs):
        pass

class ImageAsset(BaseAsset):
    """Represents an Image asset"""
    # TODO: Define concrete and abstract functionality when/if/as 
    #       needed. For now, just provide in __init__
    def __init__(self, *args, **kwargs):
        BaseAsset.__init__(self, *args, **kwargs)

class PresentationAsset(BaseAsset):
    """Represents a Presentation asset"""
    # TODO: Define concrete and abstract functionality when/if/as 
    #       needed. For now, just provide in __init__
    def __init__(self, *args, **kwargs):
        BaseAsset.__init__(self, *args, **kwargs)

class GenericAsset(BaseAsset):
    """Represents a generic file-asset"""
    # TODO: Define concrete and abstract functionality when/if/as 
    #       needed. For now, just provide in __init__
    def __init__(self, *args, **kwargs):
        BaseAsset.__init__(self, *args, **kwargs)

# - Define an abstract class that provides any concrete and 
#   abstract/required functionality for any of the concrete 
#   asset-manager classes

class BaseAssetManager(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements and type-
identity for objects that can act as a manager of a group of 
common asset types
    """

    # - Any properties or methods common to ALL asset-managers 
    #   can be defined here, but for now all we care about is 
    #   the factory method and making sure that __init__ is 
    #   defined

    def __init__(self):
        """Object initializer"""
        # TODO: Deal with any common property initialization 
        #       as/when needed. For now, just pass:
        pass

    # - Require the create_asset method in subclasses

    @abc.abstractmethod
    def create_asset(self, *args, **kwargs) -> (BaseAsset):
        # - Since this method is abstract, 
        raise NotImplementedError(
            '%s.create_asset has not been implemented as '
            'required by BaseAssetManager' % 
            (self.__class__.__name__)
        )

# - Define the concrete asset-managers

class GenericAssetManager(BaseAssetManager):

    # - Make sure that __init__ is defined and calls the parent 
    #   __init__ method(s) needed. Since there's only *one* 
    #   superclass involved at present, we can use super().
    #   If more than one superclass gets involved, each may need 
    #   to be called individually

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # - BaseAssetManager requires implementation of create_asset
    def create_asset(self, *args, **kwargs):
        # TODO: Write an actual implementation for the method. 
        #       For now, just print that it's been called in 
        #       order to show the expected behavior
        print('# GenericAssetManager.create_asset called')
        print('+- args ..... %s' % str(args))
        result = GenericAsset(*args, **kwargs)
        print('+- result ... %s' % result)
        return result

class ImageManager(BaseAssetManager):

    # - Make sure that __init__ is defined and calls the parent 
    #   __init__ method(s) needed. Since there's only *one* 
    #   superclass involved at present, we can use super().
    #   If more than one superclass gets involved, each may need 
    #   to be called individually

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # - BaseAssetManager requires implementation of create_asset
    def create_asset(self, *args, **kwargs):
        # TODO: Write an actual implementation for the method. 
        #       For now, just print that it's been called in 
        #       order to show the expected behavior
        print('# ImageManager.create_asset called')
        print('+- args ..... %s' % str(args))
        result = ImageAsset(*args, **kwargs)
        print('+- result ... %s' % result)
        return result

class PresentationManager(BaseAssetManager):

    # - Make sure that __init__ is defined and calls the parent 
    #   __init__ method(s) needed. Since there's only *one* 
    #   superclass involved at present, we can use super().
    #   If more than one superclass gets involved, each may need 
    #   to be called individually

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # - BaseAssetManager requires implementation of create_asset
    def create_asset(self, *args, **kwargs):
        # TODO: Write an actual implementation for the method. 
        #       For now, just print that it's been called in 
        #       order to show the expected behavior
        print('# PresentationManager.create_asset called')
        print('+- args ..... %s' % str(args))
        result = PresentationAsset(*args, **kwargs)
        print('+- result ... %s' % result)
        return result

if __name__ == '__main__':
    # - Create manager-instance(s)
    preso_mgr = PresentationManager()

    # - Creation of assets can be accomplished by calling the 
    #   manager-object's create_asset method:
    ex1 = preso_mgr.create_asset('asset_files/dna_of_candy.pptx')
    ex2 = preso_mgr.create_asset('asset_files/example.otp')

    img_mgr = ImageManager()
    im1 = img_mgr.create_asset('asset_files/jellybellies.jpg')

    # - Get a list of all asset-files in the directory
    import os
    asset_files = [
        f for f in os.listdir('asset_files')
    ]

    print('='*80)

    # - Specific managers for specific asset-types
    preso_mgr = PresentationManager()
    img_mgr = ImageManager()
    # - Generic manager for cases that can't be handled any other way
    gen_mgr = GenericAssetManager()
    # - Run through the list of asset-files and call the 
    #   create_asset from the relevant manager-class for each of
    #   them as applicable based on the extension of the 
    #   asset-file:
    assets = []
    for asset_file in asset_files:
        # - Get the file's extension
        file_ext = os.path.splitext(asset_file)[-1].lower()[1:]
        # - Create the asset_path of the file to pass to 
        #   create_asset
        asset_path = 'asset_files' + os.sep + asset_file
        # - Make a decision about which manager to use, and call 
        #   its create-asset accordingly, appending to the list 
        #   of assets defined earlier
        if file_ext in ('odp', 'ppt', 'pptx'):
            assets.append(preso_mgr.create_asset(asset_path))
        elif file_ext in ('png', 'jpg', 'jpeg'):
            assets.append(img_mgr.create_asset(asset_path))
        else:
            # - Provide a default case that returns a generic 
            #   asset-object if no explicitly-supported type is 
            #   available
            assets.append(gen_mgr.create_asset(asset_path))
    print('Assets list:')
    print(assets)
