#!/usr/bin/env python
"""
The complete code of Ch. 4, Recipe 3 -- 
Using metaclass to automatically register a subclass
"""

import abc

file_extensions = {}
mime_types = {}

class AssetMeta(abc.ABCMeta):
    # - Because AssetMeta is being applied to classes that derive 
    #   from ABCMeta, *this* class must also derive from 
    #   ABCMeta...
    # - Classes that represent assets must provide a list of file-
    #   extentions and mime-types that can be used to map to the 
    #   classes that can represent assets of those types
    _required_attributes = (
        'file_extensions',
        'mime_types',
    )
    # - Override the constructor
    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        # - Check for required class-attributes
        for required_attribute in AssetMeta._required_attributes:
            if not hasattr(new_class, required_attribute) \
                or type(getattr(new_class, required_attribute)) \
                != list:
                raise AttributeError(
                    '%s does not supply a non-None %s '
                    'attribute' %
                    (new_class.__name__, required_attribute)
                )
        # - If the class has the required attributes, then 
        #   register it with those values
        # - By file-extension
        for ext in new_class.file_extensions:
            # - Check to make sure that the extension isn't 
            #   already registered
            if file_extensions.get(ext):
                raise AttributeError(
                    'The "%s" file-extension cannot be '
                    'registered with AssetClassifier: an asset-'
                    'class has already been registered with '
                    'it (%s)' % (
                        ext, file_extensions[ext]
                    )
                )
            file_extensions[ext] = new_class
        # - By MIME-type
        for ext in new_class.mime_types:
            # - Check to make sure that the mime-type isn't 
            #   already registered
            if mime_types.get(ext):
                raise AttributeError(
                    'The "%s" MIME-type cannot be registered '
                    'with AssetClassifier: an asset-class has '
                    'already been registered with it (%s)' % 
                    (ext, mime_types[ext])
                )
            mime_types[ext] = new_class
        return new_class

class BaseAsset(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements and type-
identity for objects that can represent a digital asset
    """

    # PROPERTY DEFINITIONS (Not implemented, since implementation 
    # isn't needed for the recipe)
    # - 
    @abc.abstractproperty
    def metadata(self):
        """
Gets the metadata associated with the asset
        """
        raise NotImplementedError(
            '%s.metadata has not been implemented as required by '
            'BaseAsset' % (self.__class__.__name__)
        )

    # OBJECT INITIALIZATION
    def __init__(self, asset_file):
        self.asset_file = asset_file

    # REQUIRED/ABSTRACT METHODS
    @abc.abstractmethod
    def generate_previews(self):
        """
Requires that derived classes implement a method to generate a 
set of preview-images of the asset.
        """
        # NOTE: The expectation is that assets will have one to 
        #       many preview-images associated with them - image-
        #       assets will have one, presentation assets will 
        #       have one (minimum), but may have several!
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

    @property
    def metadata(self):
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'pages':1,
                'original_resolution':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self):
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

    @property
    def metadata(self):
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'pages':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self):
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

    @property
    def metadata(self):
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'pages':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self):
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

    @property
    def metadata(self):
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'pages':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self):
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

class DOCXAsset(WordProcessingAsset, metaclass=AssetMeta):
    file_extensions=['.doc', '.docx']
    mime_types = [
        'application/msword', 
        'application/vnd.openxmlformats-officedocument.'
        'wordprocessingml.document'
    ]

class JPEGAsset(ImageAsset, metaclass=AssetMeta):
    file_extensions=['.jpg', '.jpeg']
    mime_types = ['image/jpeg']

class INDDAsset(LayoutAsset, metaclass=AssetMeta):
    file_extensions=['.ind', '.indd']
    mime_types = []

class ODPAsset(PresentationAsset, metaclass=AssetMeta):
    file_extensions=['.odp']
    mime_types = [
        'application/vnd.oasis.opendocument.presentation'
    ]

class ODTAsset(WordProcessingAsset, metaclass=AssetMeta):
    file_extensions=['.odt']
    mime_types = [
        'application/vnd.oasis.opendocument.text'
    ]

class PNGAsset(ImageAsset, metaclass=AssetMeta):
    file_extensions=['.png']
    mime_types = ['image/png']

class PPTXAsset(PresentationAsset, metaclass=AssetMeta):
    file_extensions=['.ppt', '.pptx']
    mime_types = [
        'application/vnd.ms-powerpoint', 
        'application/vnd.openxmlformats-officedocument.'
        'presentationml.presentation'
    ]

class PDFAsset(BaseAsset, metaclass=AssetMeta):
    """
Provides concrete implementation of functionality required by 
BaseAsset for PDF assets
    """

    file_extensions=['.pdf']
    mime_types = ['application/pdf']

    @property
    def metadata(self):
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {
                'pages':0,
                'original_height':0,
                'original_width':0,
                'original_color_space':'TBD'
            }
            return self._metadata

    def generate_previews(self):
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
class GenericAsset(BaseAsset, metaclass=AssetMeta):

    file_extensions=['.*']
    mime_types = ['application/octet-stream']

    @property
    def metadata(self):
        """Gets the metadata associated with the instance"""
        try:
            return self._metadata
        except AttributeError:
            self._metadata = {}
            return self._metadata

    def generate_previews(self):
        """Generates a set of preview-images of the asset."""
        # NOTE: Same notes as LayoutAsset's generate_previews
        # - For now, we'll just print what needs to happen
        print(
            '+- %s.generate_previews called' % 
            (self.__class__.__name__)
        )
        print('  +- Cannot generate a preview')

if __name__ == '__main__':
    from pprint import pprint
    pprint(file_extensions)
    pprint(mime_types)

    # - This preserves the abstraction too... If, for example, 
    #   GenericAsset.generate_previews is commented out or 
    #   renamed, and we try to create an instance:
    generic = GenericAsset('')
    # - It will raise:
    # TypeError: Can't instantiate abstract class GenericAsset with abstract methods generate_previews
