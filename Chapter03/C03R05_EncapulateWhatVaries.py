#!/usr/bin/env python
"""
The complete code of Ch. 3, Recipe 6 -- Encapsulating what varies
"""

import abc

# - Define a base class that captures all the common aspects 
#   of ANY asset

class BaseAsset(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements and type-
identity for objects that can represent a digital asset
    """

    # PROPERTY DEFINITIONS
    @abc.abstractproperty
    def metadata(self) -> dict:
        """
Gets the metadata associated with the asset
        """
        raise NotImplementedError(
            '%s.metadata has not been implemented as required by '
            'BaseAsset' % (self.__class__.__name__)
        )

    # OBJECT INITIALIZATION
    def __init__(self, asset_file:str):
        if self.__class__ == BaseAsset:
            raise NotImplementedError(
                'BaseAsset is a foundational ABC, and should '
                'not be instantiated'
            )
        self.asset_file = asset_file

    # REQUIRED/ABSTRACT METHODS
    @abc.abstractmethod
    def generate_previews(self) -> list:
        """
Requires that derived classes implement a method to generate a 
set of preview-images of the asset.
        """
        # NOTE: The expectation is that assets will have one to 
        #       many preview-images associated with them - image-
        #       assets will have one, other assets will have one
        #       (at minimum), but may have several!
        raise NotImplementedError(
            '%s.generate_previews has not been implemented as '
            'required by BaseAsset' % (self.__class__.__name__)
        )

# - Define the intermediate classes, that provide concrete 
#   implementations of BaseAsset functionality where possible

class ImageAsset(BaseAsset):
    """
Provides concrete implementation of functionality required by 
BaseAsset that is common to all assets that are images of some 
sort (JPG, PNG, etc.)
    """

    def __init__(self, asset_file:str):
        if self.__class__ == ImageAsset:
            raise NotImplementedError(
                'ImageAsset is an intermediate ABC, and should '
                'not be instantiated'
            )
        BaseAsset.__init__(self, asset_file)

    @property
    def metadata(self) -> dict:
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'mime_type':self.__class__._mime_type,
                'asset_file':self.asset_file,
                'pages':1,
                'original_resolution':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD',
            }
            return self._metadata

    def generate_previews(self) -> list:
        """Generates a set of preview-images of the asset."""
        # NOTE: This assumes a single common mechanism, like 
        #       ImageMagick or the Pillow library is available 
        #       and can do what is needed
        # - For now, we'll just print what needs to happen
        print(
            '+- %s.generate_previews called' % 
            (self.__class__.__name__)
        )
        print('   +- Get original file')
        print('   +- Resize and convert to output format')
        print('   +- Return list (one item) of preview-files')

class LayoutAsset(BaseAsset):
    """
Provides concrete implementation of functionality required by 
BaseAsset that is common to all assets that are layout-documents 
of some sort (InDesign INDD files, for example)
    """

    def __init__(self, asset_file:str):
        if self.__class__ == LayoutAsset:
            raise NotImplementedError(
                'LayoutAsset is an intermediate ABC, and should '
                'not be instantiated'
            )

    @property
    def metadata(self) -> dict:
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'mime_type':self.__class__._mime_type,
                'asset_file':self.asset_file,
                'pages':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self) -> list:
        """Generates a set of preview-images of the asset."""
        # NOTE: This assumes a single common mechanism, like 
        #       GhostScript is available, and can convert PDFs 
        #       into a series of page-images.
        #       It also requires the same image-manipulation 
        #       capabilities that ImageAsset does, to resize 
        #       those page-images.
        # - For now, we'll just print what needs to happen
        print(
            '+- %s.generate_previews called' % 
            (self.__class__.__name__)
        )
        print('   +- Get original file-name')
        print(   '+- Find and fetch a PDF with the same name')
        print('      +- If no PDF is available, raise an error')
        print('   +- "Print" each page to a high-res image')
        print('      +- Resize/convert each to output format')
        print('   +- Return list of preview-files')

class PresentationAsset(BaseAsset):
    """
Provides concrete implementation of functionality required by 
BaseAsset that is common to all assets that are presentation-
documents of some sort (PowerPoint, OpenDocument odp files, etc.)
    """

    def __init__(self, asset_file:str):
        if self.__class__ == PresentationAsset:
            raise NotImplementedError(
                'PresentationAsset is an intermediate ABC, and '
                'should not be instantiated'
            )
        BaseAsset.__init__(self, asset_file)

    @property
    def metadata(self) -> dict:
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'mime_type':self.__class__._mime_type,
                'asset_file':self.asset_file,
                'pages':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self) -> list:
        """Generates a set of preview-images of the asset."""
        # NOTE: This assumes a single common mechanism, like 
        #       LibreOffice (headless) is available that can 
        #       read and render documents to a PDF.
        #       It also requires GhostScript or an equivalent, 
        #       like LayoutAsset and PDFAsset do, to generate 
        #       high-res page-images.
        #       It ALSO requires the same image-manipulation 
        #       capabilities that ImageAsset does, to resize 
        #       those page-images.
        # - For now, we'll just print what needs to happen
        print(
            '+- %s.generate_previews called' % 
            (self.__class__.__name__)
        )
        print('   +- Get original file')
        print('   +- Open with LibreOffice and convert to PDF')
        print('      +- "Print" each PDF page to a high-res image')
        print('         +- Resize/convert each to output format')
        print('   +- Return list of preview-files')

class WordProcessingAsset(BaseAsset):
    """
Provides concrete implementation of functionality required by 
BaseAsset that is common to all assets that are word-processor 
documents of some sort (MS Word, or OpenDocument odt files, 
for example)
    """

    def __init__(self, asset_file:str):
        if self.__class__ == WordProcessingAsset:
            raise NotImplementedError(
                'WordProcessingAsset is an intermediate ABC, '
                'and should not be instantiated'
            )

    @property
    def metadata(self) -> dict:
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'mime_type':self.__class__._mime_type,
                'asset_file':self.asset_file,
                'pages':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self) -> list:
        """Generates a set of preview-images of the asset."""
        # NOTE: Same notes/requirements as PresentationAsset
        # - For now, we'll just print what needs to happen
        print(
            '+- %s.generate_previews called' % 
            (self.__class__.__name__)
        )
        print('   +- Get original file')
        print('   +- Open with LibreOffice and convert to PDF')
        print('      +- "Print" each PDF page to a high-res image')
        print('         +- Resize/convert each to output format')
        print('   +- Return list of preview-files')

# - Define the concrete classes

class DOCXAsset(WordProcessingAsset):

    _mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

    def __init__(self, asset_file:str):
        WordProcessingAsset.__init__(self, asset_file)

class JPEGAsset(ImageAsset):

    _mime_type = 'image/jpeg'

    def __init__(self, asset_file:str):
        ImageAsset.__init__(self, asset_file)

class INDDAsset(LayoutAsset):

    _mime_type = 'application/octet-stream'

    def __init__(self, asset_file:str):
        LayoutAsset.__init__(self, asset_file)

class ODPAsset(PresentationAsset):

    _mime_type = (
        'application/vnd.oasis.opendocument.presentation'
    )

    def __init__(self, asset_file:str):
        PresentationAsset.__init__(self, asset_file)

class ODTAsset(WordProcessingAsset):

    _mime_type = 'application/vnd.oasis.opendocument.text'

    def __init__(self, asset_file:str):
        WordProcessingAsset.__init__(self, asset_file)

class PNGAsset(ImageAsset):

    _mime_type = 'image/png'

    def __init__(self, asset_file:str):
        ImageAsset.__init__(self, asset_file)

class PPTXAsset(PresentationAsset):

    _mime_type = (
        'application/vnd.openxmlformats-officedocument.'
        'presentationml.presentation'
    )

    def __init__(self, asset_file:str):
        PresentationAsset.__init__(self, asset_file)

class PDFAsset(BaseAsset):
    """
Provides concrete implementation of functionality required by 
BaseAsset for PDF assets
    """

    _mime_type = 'application/pdf'

    def __init__(self, asset_file:str):
        BaseAsset.__init__(self, asset_file)

    @property
    def metadata(self) -> dict:
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'mime_type':self.__class__._mime_type,
                'asset_file':self.asset_file,
                'pages':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self) -> list:
        """Generates a set of preview-images of the asset."""
        # NOTE: Same notes as LayoutAsset's generate_previews
        # - For now, we'll just print what needs to happen
        print(
            '%s.generate_previews called' % 
            (self.__class__.__name__)
        )
        print('+- Get original file')
        print('+- "Print" each page to a high-res image')
        print('   +- Resize/convert each to output format')
        print('+- Return list of preview-files')

# - Also define a "generic" asset-type to deal with unrecognized 
#   file-/asset-types
class GenericAsset(BaseAsset):

    _mime_type = 'application/octet-stream'

    def __init__(self, asset_file:str):
        BaseAsset.__init__(self, asset_file)

    @property
    def metadata(self) -> dict:
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'mime_type':self.__class__._mime_type,
                'asset_file':self.asset_file,
            }
            return self._metadata

    def generate_previews(self) -> list:
        """Generates a set of preview-images of the asset."""
        # NOTE: Same notes as LayoutAsset's generate_previews
        # - For now, we'll just print what needs to happen
        print(
            '+- %s.generate_previews called' % 
            (self.__class__.__name__)
        )
        print('  +- Cannot generate a preview')

if __name__ == '__main__':
    # - Get the list of asset-files in the asset_files directory
    import os
    asset_files = os.listdir('asset_files')
    assets = {}
    for asset in asset_files:
        # - The sequence here is trying to make sure that more 
        #   common asset-types are identified first, just in case 
        #   the asset-object creation-process is lengthy...
        asset_ext = os.path.splitext(asset.lower())[-1]
        if asset_ext == '.pptx':
            assets[asset] = PPTXAsset(asset)
        elif asset_ext == '.odp':
            assets[asset] = ODPAsset(asset)
        elif asset_ext in ('.jpg', '.jpeg'):
            assets[asset] = JPEGAsset(asset)
        elif asset_ext in ('.indd', '.ind'):
            assets[asset] = LayoutAsset(asset)
        elif asset_ext == '.pdf':
            assets[asset] = PDFAsset(asset)
        elif asset_ext == '.png':
            assets[asset] = PNGAsset(asset)
        elif asset_ext == '.docx':
            assets[asset] = DOCXAsset(asset)
        elif asset_ext == '.odt':
            assets[asset] = ODTAsset(asset)
        else:
            assets[asset] = GenericAsset(asset)
    # - Print a nicely-formatted list of assets
    if assets:
        print('%d assets:' % len(assets))
        for asset in sorted(assets):
            print(
                (
                    '%s' % assets[asset].__class__.__name__
                ).ljust(23, '.')
                + ' %s' % asset
            )
            print(assets[asset].metadata)
            assets[asset].generate_previews()
    else:
        print('No assets found in asset_files directory')
