"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations. The Intersight OpenAPI document defines the complete set of properties that are returned in the HTTP response. From that perspective, a client can expect that no additional properties are returned, unless these properties are explicitly defined in the OpenAPI document. However, when a client uses an older version of the Intersight OpenAPI document, the server may send additional properties because the software is more recent than the client. In that case, the client may receive properties that it does not know about. Some generated SDKs perform a strict validation of the HTTP response body against the OpenAPI document.  # noqa: E501

    The version of the OpenAPI document: 1.0.11-2025062323
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from intersight.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    set_model_init_error,
    OpenApiModel
)
from intersight.exceptions import ApiAttributeError


def lazy_import():
    from intersight.model.connector_download_status import ConnectorDownloadStatus
    from intersight.model.connector_file_checksum import ConnectorFileChecksum
    from intersight.model.display_names import DisplayNames
    from intersight.model.mo_base_mo_relationship import MoBaseMoRelationship
    from intersight.model.mo_tag import MoTag
    from intersight.model.mo_version_context import MoVersionContext
    from intersight.model.network_element_relationship import NetworkElementRelationship
    from intersight.model.softwarerepository_cached_image_all_of import SoftwarerepositoryCachedImageAllOf
    from intersight.model.softwarerepository_file_relationship import SoftwarerepositoryFileRelationship
    globals()['ConnectorDownloadStatus'] = ConnectorDownloadStatus
    globals()['ConnectorFileChecksum'] = ConnectorFileChecksum
    globals()['DisplayNames'] = DisplayNames
    globals()['MoBaseMoRelationship'] = MoBaseMoRelationship
    globals()['MoTag'] = MoTag
    globals()['MoVersionContext'] = MoVersionContext
    globals()['NetworkElementRelationship'] = NetworkElementRelationship
    globals()['SoftwarerepositoryCachedImageAllOf'] = SoftwarerepositoryCachedImageAllOf
    globals()['SoftwarerepositoryFileRelationship'] = SoftwarerepositoryFileRelationship


class SoftwarerepositoryCachedImage(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('class_id',): {
            'SOFTWAREREPOSITORY.CACHEDIMAGE': "softwarerepository.CachedImage",
        },
        ('object_type',): {
            'SOFTWAREREPOSITORY.CACHEDIMAGE': "softwarerepository.CachedImage",
        },
        ('action',): {
            'NONE': "None",
            'GENERATEPRESIGNEDUPLOADURL': "GeneratePreSignedUploadUrl",
            'GENERATEPRESIGNEDDOWNLOADURL': "GeneratePreSignedDownloadUrl",
            'COMPLETEIMPORTPROCESS': "CompleteImportProcess",
            'MARKIMPORTFAILED': "MarkImportFailed",
            'PRECACHE': "PreCache",
            'CANCEL': "Cancel",
            'EXTRACT': "Extract",
            'EVICT': "Evict",
        },
        ('cache_state',): {
            'READYFORIMPORT': "ReadyForImport",
            'IMPORTING': "Importing",
            'IMPORTED': "Imported",
            'PENDINGEXTRACTION': "PendingExtraction",
            'EXTRACTING': "Extracting",
            'EXTRACTED': "Extracted",
            'FAILED': "Failed",
            'METAONLY': "MetaOnly",
            'READYFORCACHE': "ReadyForCache",
            'CACHING': "Caching",
            'CACHED': "Cached",
            'CACHINGFAILED': "CachingFailed",
            'CORRUPTED': "Corrupted",
            'EVICTED': "Evicted",
            'INVALID': "Invalid",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'class_id': (str,),  # noqa: E501
            'object_type': (str,),  # noqa: E501
            'action': (str,),  # noqa: E501
            'cache_state': (str,),  # noqa: E501
            'cached_time': (datetime,),  # noqa: E501
            'last_access_time': (datetime,),  # noqa: E501
            'md5sum': (str,),  # noqa: E501
            'original_sha512sum': (str,),  # noqa: E501
            'path': (str,),  # noqa: E501
            'registered_workflows': ([str], none_type,),  # noqa: E501
            'used_count': (int,),  # noqa: E501
            'file': (SoftwarerepositoryFileRelationship,),  # noqa: E501
            'network_element': (NetworkElementRelationship,),  # noqa: E501
            'account_moid': (str,),  # noqa: E501
            'create_time': (datetime,),  # noqa: E501
            'domain_group_moid': (str,),  # noqa: E501
            'mod_time': (datetime,),  # noqa: E501
            'moid': (str,),  # noqa: E501
            'owners': ([str], none_type,),  # noqa: E501
            'shared_scope': (str,),  # noqa: E501
            'tags': ([MoTag], none_type,),  # noqa: E501
            'version_context': (MoVersionContext,),  # noqa: E501
            'ancestors': ([MoBaseMoRelationship], none_type,),  # noqa: E501
            'parent': (MoBaseMoRelationship,),  # noqa: E501
            'permission_resources': ([MoBaseMoRelationship], none_type,),  # noqa: E501
            'display_names': (DisplayNames,),  # noqa: E501
            'checksum': (ConnectorFileChecksum,),  # noqa: E501
            'download_error': (str,),  # noqa: E501
            'download_progress': (int,),  # noqa: E501
            'download_retries': (int,),  # noqa: E501
            'sha256checksum': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        val = {
        }
        if not val:
            return None
        return {'class_id': val}

    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'action': 'Action',  # noqa: E501
        'cache_state': 'CacheState',  # noqa: E501
        'cached_time': 'CachedTime',  # noqa: E501
        'last_access_time': 'LastAccessTime',  # noqa: E501
        'md5sum': 'Md5sum',  # noqa: E501
        'original_sha512sum': 'OriginalSha512sum',  # noqa: E501
        'path': 'Path',  # noqa: E501
        'registered_workflows': 'RegisteredWorkflows',  # noqa: E501
        'used_count': 'UsedCount',  # noqa: E501
        'file': 'File',  # noqa: E501
        'network_element': 'NetworkElement',  # noqa: E501
        'account_moid': 'AccountMoid',  # noqa: E501
        'create_time': 'CreateTime',  # noqa: E501
        'domain_group_moid': 'DomainGroupMoid',  # noqa: E501
        'mod_time': 'ModTime',  # noqa: E501
        'moid': 'Moid',  # noqa: E501
        'owners': 'Owners',  # noqa: E501
        'shared_scope': 'SharedScope',  # noqa: E501
        'tags': 'Tags',  # noqa: E501
        'version_context': 'VersionContext',  # noqa: E501
        'ancestors': 'Ancestors',  # noqa: E501
        'parent': 'Parent',  # noqa: E501
        'permission_resources': 'PermissionResources',  # noqa: E501
        'display_names': 'DisplayNames',  # noqa: E501
        'checksum': 'Checksum',  # noqa: E501
        'download_error': 'DownloadError',  # noqa: E501
        'download_progress': 'DownloadProgress',  # noqa: E501
        'download_retries': 'DownloadRetries',  # noqa: E501
        'sha256checksum': 'Sha256checksum',  # noqa: E501
    }

    read_only_vars = {
        'cache_state',  # noqa: E501
        'cached_time',  # noqa: E501
        'last_access_time',  # noqa: E501
        'md5sum',  # noqa: E501
        'original_sha512sum',  # noqa: E501
        'path',  # noqa: E501
        'used_count',  # noqa: E501
        'account_moid',  # noqa: E501
        'create_time',  # noqa: E501
        'domain_group_moid',  # noqa: E501
        'mod_time',  # noqa: E501
        'shared_scope',  # noqa: E501
        'ancestors',  # noqa: E501
        'permission_resources',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SoftwarerepositoryCachedImage - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "softwarerepository.CachedImage", must be one of ["softwarerepository.CachedImage", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "softwarerepository.CachedImage", must be one of ["softwarerepository.CachedImage", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            action (str): The action to be performed on the imported file. If 'PreCache' is set, the image will be cached in endpoint. If 'Evict' is set, the cached file will be removed. Applicable in Intersight appliance deployment. If 'Cancel' is set, the ImportState is marked as 'Failed'. Applicable for local machine source. * `None` - No action should be taken on the imported file. * `GeneratePreSignedUploadUrl` - Generate pre signed URL of file for importing into the repository. * `GeneratePreSignedDownloadUrl` - Generate pre signed URL of file in the repository to download. * `CompleteImportProcess` - Mark that the import process of the file into the repository is complete. * `MarkImportFailed` - Mark to indicate that the import process of the file into the repository failed. * `PreCache` - Cache the file into the Intersight Appliance. * `Cancel` - The cancel import process for the file into the repository. * `Extract` - The action to extract the file in the external repository. * `Evict` - Evict the cached file from the Intersight Appliance.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            cache_state (str): The state  of this file in the endpoint The importState is updated during the cache operation and as part of the cache monitoring process. * `ReadyForImport` - The image is ready to be imported into the repository. * `Importing` - The image is being imported into the repository. * `Imported` - The image has been extracted and imported into the repository. * `PendingExtraction` - Indicates that the image has been imported but not extracted in the repository. * `Extracting` - Indicates that the image is being extracted into the repository. * `Extracted` - Indicates that the image has been extracted into the repository. * `Failed` - The image import from an external source to the repository has failed. * `MetaOnly` - The image is present in an external repository. * `ReadyForCache` - The image is ready to be cached into the Intersight Appliance. * `Caching` - Indicates that the image is being cached into the Intersight Appliance or endpoint cache. * `Cached` - Indicates that the image has been cached into the Intersight Appliance or endpoint cache. * `CachingFailed` - Indicates that the image caching into the Intersight Appliance failed or endpoint cache. * `Corrupted` - Indicates that the image in the local repository (or endpoint cache) has been corrupted after it was cached. * `Evicted` - Indicates that the image has been evicted from the Intersight Appliance (or endpoint cache) to reclaim storage space. * `Invalid` - Indicates that the corresponding distributable MO has been removed from the backend. This can be due to unpublishing of an image.. [optional] if omitted the server will use the default value of "ReadyForImport"  # noqa: E501
            cached_time (datetime): The time when the image or file was cached into the FI storage.. [optional]  # noqa: E501
            last_access_time (datetime): Used by the cache monitoring process to determine the files that are to be evicted from the cache.. [optional]  # noqa: E501
            md5sum (str): The MD5 sum of the firmware image that will be used by the endpoint to validate the integrity of the image.. [optional]  # noqa: E501
            original_sha512sum (str): The actual sha512sum of the cached image.. [optional]  # noqa: E501
            path (str): The absolute path of the imported file in the endpoint.. [optional]  # noqa: E501
            registered_workflows ([str], none_type): [optional]  # noqa: E501
            used_count (int): The number of times this file has been used to copy or upgrade or install actions. Used by the cache monitoring process to determine the files to be evicted from the cache.. [optional]  # noqa: E501
            file (SoftwarerepositoryFileRelationship): [optional]  # noqa: E501
            network_element (NetworkElementRelationship): [optional]  # noqa: E501
            account_moid (str): The Account ID for this managed object.. [optional]  # noqa: E501
            create_time (datetime): The time when this managed object was created.. [optional]  # noqa: E501
            domain_group_moid (str): The DomainGroup ID for this managed object.. [optional]  # noqa: E501
            mod_time (datetime): The time when this managed object was last modified.. [optional]  # noqa: E501
            moid (str): The unique identifier of this Managed Object instance.. [optional]  # noqa: E501
            owners ([str], none_type): [optional]  # noqa: E501
            shared_scope (str): Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.. [optional]  # noqa: E501
            tags ([MoTag], none_type): [optional]  # noqa: E501
            version_context (MoVersionContext): [optional]  # noqa: E501
            ancestors ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            parent (MoBaseMoRelationship): [optional]  # noqa: E501
            permission_resources ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            display_names (DisplayNames): [optional]  # noqa: E501
            checksum (ConnectorFileChecksum): [optional]  # noqa: E501
            download_error (str): Any error encountered. Set to empty when download is in progress or completed.. [optional]  # noqa: E501
            download_progress (int): The download progress of the file represented as a percentage between 0% and 100%. If progress reporting is not possible, a value of -1 is sent.. [optional]  # noqa: E501
            download_retries (int): The number of retries the plugin attempted before succeeding or failing the download.. [optional]  # noqa: E501
            sha256checksum (str): The sha256checksum of the downloaded file as calculated by the download plugin after successfully downloading a file.. [optional]  # noqa: E501
        """

        class_id = "softwarerepository.CachedImage" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "softwarerepository.CachedImage")
        object_type = "softwarerepository.CachedImage" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "softwarerepository.CachedImage")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'class_id': class_id,
            'object_type': object_type,
        }
        kwargs.update(required_args)
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]
        composed_keys = set()
        for instance in self._composed_instances:
            composed_keys.update(set(instance.attribute_map.values()))

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            if var_name in composed_keys:
                continue
            setattr(self, var_name, var_value)

        return self


    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SoftwarerepositoryCachedImage - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "softwarerepository.CachedImage", must be one of ["softwarerepository.CachedImage", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "softwarerepository.CachedImage", must be one of ["softwarerepository.CachedImage", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            action (str): The action to be performed on the imported file. If 'PreCache' is set, the image will be cached in endpoint. If 'Evict' is set, the cached file will be removed. Applicable in Intersight appliance deployment. If 'Cancel' is set, the ImportState is marked as 'Failed'. Applicable for local machine source. * `None` - No action should be taken on the imported file. * `GeneratePreSignedUploadUrl` - Generate pre signed URL of file for importing into the repository. * `GeneratePreSignedDownloadUrl` - Generate pre signed URL of file in the repository to download. * `CompleteImportProcess` - Mark that the import process of the file into the repository is complete. * `MarkImportFailed` - Mark to indicate that the import process of the file into the repository failed. * `PreCache` - Cache the file into the Intersight Appliance. * `Cancel` - The cancel import process for the file into the repository. * `Extract` - The action to extract the file in the external repository. * `Evict` - Evict the cached file from the Intersight Appliance.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            cache_state (str): The state  of this file in the endpoint The importState is updated during the cache operation and as part of the cache monitoring process. * `ReadyForImport` - The image is ready to be imported into the repository. * `Importing` - The image is being imported into the repository. * `Imported` - The image has been extracted and imported into the repository. * `PendingExtraction` - Indicates that the image has been imported but not extracted in the repository. * `Extracting` - Indicates that the image is being extracted into the repository. * `Extracted` - Indicates that the image has been extracted into the repository. * `Failed` - The image import from an external source to the repository has failed. * `MetaOnly` - The image is present in an external repository. * `ReadyForCache` - The image is ready to be cached into the Intersight Appliance. * `Caching` - Indicates that the image is being cached into the Intersight Appliance or endpoint cache. * `Cached` - Indicates that the image has been cached into the Intersight Appliance or endpoint cache. * `CachingFailed` - Indicates that the image caching into the Intersight Appliance failed or endpoint cache. * `Corrupted` - Indicates that the image in the local repository (or endpoint cache) has been corrupted after it was cached. * `Evicted` - Indicates that the image has been evicted from the Intersight Appliance (or endpoint cache) to reclaim storage space. * `Invalid` - Indicates that the corresponding distributable MO has been removed from the backend. This can be due to unpublishing of an image.. [optional] if omitted the server will use the default value of "ReadyForImport"  # noqa: E501
            cached_time (datetime): The time when the image or file was cached into the FI storage.. [optional]  # noqa: E501
            last_access_time (datetime): Used by the cache monitoring process to determine the files that are to be evicted from the cache.. [optional]  # noqa: E501
            md5sum (str): The MD5 sum of the firmware image that will be used by the endpoint to validate the integrity of the image.. [optional]  # noqa: E501
            original_sha512sum (str): The actual sha512sum of the cached image.. [optional]  # noqa: E501
            path (str): The absolute path of the imported file in the endpoint.. [optional]  # noqa: E501
            registered_workflows ([str], none_type): [optional]  # noqa: E501
            used_count (int): The number of times this file has been used to copy or upgrade or install actions. Used by the cache monitoring process to determine the files to be evicted from the cache.. [optional]  # noqa: E501
            file (SoftwarerepositoryFileRelationship): [optional]  # noqa: E501
            network_element (NetworkElementRelationship): [optional]  # noqa: E501
            account_moid (str): The Account ID for this managed object.. [optional]  # noqa: E501
            create_time (datetime): The time when this managed object was created.. [optional]  # noqa: E501
            domain_group_moid (str): The DomainGroup ID for this managed object.. [optional]  # noqa: E501
            mod_time (datetime): The time when this managed object was last modified.. [optional]  # noqa: E501
            moid (str): The unique identifier of this Managed Object instance.. [optional]  # noqa: E501
            owners ([str], none_type): [optional]  # noqa: E501
            shared_scope (str): Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.. [optional]  # noqa: E501
            tags ([MoTag], none_type): [optional]  # noqa: E501
            version_context (MoVersionContext): [optional]  # noqa: E501
            ancestors ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            parent (MoBaseMoRelationship): [optional]  # noqa: E501
            permission_resources ([MoBaseMoRelationship], none_type): An array of relationships to moBaseMo resources.. [optional]  # noqa: E501
            display_names (DisplayNames): [optional]  # noqa: E501
            checksum (ConnectorFileChecksum): [optional]  # noqa: E501
            download_error (str): Any error encountered. Set to empty when download is in progress or completed.. [optional]  # noqa: E501
            download_progress (int): The download progress of the file represented as a percentage between 0% and 100%. If progress reporting is not possible, a value of -1 is sent.. [optional]  # noqa: E501
            download_retries (int): The number of retries the plugin attempted before succeeding or failing the download.. [optional]  # noqa: E501
            sha256checksum (str): The sha256checksum of the downloaded file as calculated by the download plugin after successfully downloading a file.. [optional]  # noqa: E501
        """

        class_id = "softwarerepository.CachedImage" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "softwarerepository.CachedImage")
        object_type = "softwarerepository.CachedImage" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "softwarerepository.CachedImage")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'class_id': class_id,
            'object_type': object_type,
        }
        kwargs.update(required_args)
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in self.read_only_vars:
                set_model_init_error(f"Warning : {var_name} is omitted from request payload as it is a read-only property")
                continue
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              ConnectorDownloadStatus,
              SoftwarerepositoryCachedImageAllOf,
          ],
          'oneOf': [
          ],
        }
