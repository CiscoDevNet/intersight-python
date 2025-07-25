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
    from intersight.model.hcl_product import HclProduct
    globals()['HclProduct'] = HclProduct


class HclHardwareCompatibilityProfileAllOf(ModelNormal):
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
            'HCL.HARDWARECOMPATIBILITYPROFILE': "hcl.HardwareCompatibilityProfile",
        },
        ('object_type',): {
            'HCL.HARDWARECOMPATIBILITYPROFILE': "hcl.HardwareCompatibilityProfile",
        },
        ('error_code',): {
            'SUCCESS': "Success",
            'UNKNOWN': "Unknown",
            'UNKNOWNSERVER': "UnknownServer",
            'INVALIDUCSVERSION': "InvalidUcsVersion",
            'PROCESSORNOTSUPPORTED': "ProcessorNotSupported",
            'OSNOTSUPPORTED': "OSNotSupported",
            'OSUNKNOWN': "OSUnknown",
            'UCSVERSIONNOTSUPPORTED': "UCSVersionNotSupported",
            'UCSVERSIONSERVEROSCOMBINATIONNOTSUPPORTED': "UcsVersionServerOSCombinationNotSupported",
            'PRODUCTUNKNOWN': "ProductUnknown",
            'PRODUCTNOTSUPPORTED': "ProductNotSupported",
            'DRIVERNAMENOTSUPPORTED': "DriverNameNotSupported",
            'FIRMWAREVERSIONNOTSUPPORTED': "FirmwareVersionNotSupported",
            'DRIVERVERSIONNOTSUPPORTED': "DriverVersionNotSupported",
            'FIRMWAREVERSIONDRIVERVERSIONCOMBINATIONNOTSUPPORTED': "FirmwareVersionDriverVersionCombinationNotSupported",
            'FIRMWAREVERSIONANDDRIVERVERSIONNOTSUPPORTED': "FirmwareVersionAndDriverVersionNotSupported",
            'FIRMWAREVERSIONANDDRIVERNAMENOTSUPPORTED': "FirmwareVersionAndDriverNameNotSupported",
            'INTERNALERROR': "InternalError",
            'MARSHALLINGERROR': "MarshallingError",
            'EXEMPTED': "Exempted",
        },
        ('version_type',): {
            'UCSM': "UCSM",
            'IMC': "IMC",
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
            'driver_iso_url': (str,),  # noqa: E501
            'error_code': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'os_vendor': (str,),  # noqa: E501
            'os_version': (str,),  # noqa: E501
            'personality': (str,),  # noqa: E501
            'processor_model': (str,),  # noqa: E501
            'products': ([HclProduct], none_type,),  # noqa: E501
            'server_model': (str,),  # noqa: E501
            'server_revision': (str,),  # noqa: E501
            'ucs_version': (str,),  # noqa: E501
            'version_type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'driver_iso_url': 'DriverIsoUrl',  # noqa: E501
        'error_code': 'ErrorCode',  # noqa: E501
        'id': 'Id',  # noqa: E501
        'os_vendor': 'OsVendor',  # noqa: E501
        'os_version': 'OsVersion',  # noqa: E501
        'personality': 'Personality',  # noqa: E501
        'processor_model': 'ProcessorModel',  # noqa: E501
        'products': 'Products',  # noqa: E501
        'server_model': 'ServerModel',  # noqa: E501
        'server_revision': 'ServerRevision',  # noqa: E501
        'ucs_version': 'UcsVersion',  # noqa: E501
        'version_type': 'VersionType',  # noqa: E501
    }

    read_only_vars = {
        'error_code',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """HclHardwareCompatibilityProfileAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "hcl.HardwareCompatibilityProfile", must be one of ["hcl.HardwareCompatibilityProfile", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "hcl.HardwareCompatibilityProfile", must be one of ["hcl.HardwareCompatibilityProfile", ]  # noqa: E501
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
            driver_iso_url (str): Url for the ISO with the drivers supported for the server.. [optional]  # noqa: E501
            error_code (str): Error code indicating the compatibility status. * `Success` - The input combination is valid. * `Unknown` - Unknown API request to the service. * `UnknownServer` - An invalid server model is given API requests or the server model is not present in the HCL database. * `InvalidUcsVersion` - UCS Version is not in expected format. * `ProcessorNotSupported` - Processor is not supported with the given Server or the Processor does not exist in the HCL database. * `OSNotSupported` - OS version is not supported with the given server, processor combination or OS information is not present in the HCL database. * `OSUnknown` - OS vendor or version is not known as per the HCL database. * `UCSVersionNotSupported` - UCS Version is not supported with the given server, processor and OS combination or the UCS version is not present in the HCL database. * `UcsVersionServerOSCombinationNotSupported` - Combination of UCS version, server (model and processor) and os version is not supported. * `ProductUnknown` - Product is not known as per the HCL database. * `ProductNotSupported` - Product is not supported in the given UCS version, server (model and processor) and operating system version. * `DriverNameNotSupported` - Driver protocol or name is not supported for the given product. * `FirmwareVersionNotSupported` - Firmware version not supported for the component and the server, operating system combination. * `DriverVersionNotSupported` - Driver version not supported for the component and the server, operating system combination. * `FirmwareVersionDriverVersionCombinationNotSupported` - Both Firmware and Driver versions are not supported for the component and the server, operating system combination. * `FirmwareVersionAndDriverVersionNotSupported` - Firmware and Driver version combination not supported for the component and the server, operating system combination. * `FirmwareVersionAndDriverNameNotSupported` - Firmware Version and Driver name or not supported with the component and the server, operating system combination. * `InternalError` - API requests to the service have either failed or timed out. * `MarshallingError` - Error in JSON marshalling. * `Exempted` - An exempted error code means that the product is part of the exempted Catalog and should be ignored for HCL validation purposes.. [optional] if omitted the server will use the default value of "Success"  # noqa: E501
            id (str): Identifier of the hardware compatibility profile.. [optional]  # noqa: E501
            os_vendor (str): Vendor of the Operating System running on the server.. [optional]  # noqa: E501
            os_version (str): Version of the Operating System running on the server.. [optional]  # noqa: E501
            personality (str): Personality indicating the personality with the which the sever is used in a Hyperflex environment.. [optional]  # noqa: E501
            processor_model (str): Model of the processor present in the server.. [optional]  # noqa: E501
            products ([HclProduct], none_type): [optional]  # noqa: E501
            server_model (str): Model of the server as returned by UCSM/CIMC XML API.. [optional]  # noqa: E501
            server_revision (str): Revision of the server model.. [optional]  # noqa: E501
            ucs_version (str): Version of the UCS software.. [optional]  # noqa: E501
            version_type (str): Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release. * `UCSM` - The server is managed by UCS Manager. * `IMC` - The server is standalone managed by CIMC.. [optional] if omitted the server will use the default value of "UCSM"  # noqa: E501
        """

        class_id = "hcl.HardwareCompatibilityProfile" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "hcl.HardwareCompatibilityProfile")
        object_type = "hcl.HardwareCompatibilityProfile" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "hcl.HardwareCompatibilityProfile")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
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

        self.class_id = class_id
        self.object_type = object_type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
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
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """HclHardwareCompatibilityProfileAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "hcl.HardwareCompatibilityProfile", must be one of ["hcl.HardwareCompatibilityProfile", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "hcl.HardwareCompatibilityProfile", must be one of ["hcl.HardwareCompatibilityProfile", ]  # noqa: E501
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
            driver_iso_url (str): Url for the ISO with the drivers supported for the server.. [optional]  # noqa: E501
            error_code (str): Error code indicating the compatibility status. * `Success` - The input combination is valid. * `Unknown` - Unknown API request to the service. * `UnknownServer` - An invalid server model is given API requests or the server model is not present in the HCL database. * `InvalidUcsVersion` - UCS Version is not in expected format. * `ProcessorNotSupported` - Processor is not supported with the given Server or the Processor does not exist in the HCL database. * `OSNotSupported` - OS version is not supported with the given server, processor combination or OS information is not present in the HCL database. * `OSUnknown` - OS vendor or version is not known as per the HCL database. * `UCSVersionNotSupported` - UCS Version is not supported with the given server, processor and OS combination or the UCS version is not present in the HCL database. * `UcsVersionServerOSCombinationNotSupported` - Combination of UCS version, server (model and processor) and os version is not supported. * `ProductUnknown` - Product is not known as per the HCL database. * `ProductNotSupported` - Product is not supported in the given UCS version, server (model and processor) and operating system version. * `DriverNameNotSupported` - Driver protocol or name is not supported for the given product. * `FirmwareVersionNotSupported` - Firmware version not supported for the component and the server, operating system combination. * `DriverVersionNotSupported` - Driver version not supported for the component and the server, operating system combination. * `FirmwareVersionDriverVersionCombinationNotSupported` - Both Firmware and Driver versions are not supported for the component and the server, operating system combination. * `FirmwareVersionAndDriverVersionNotSupported` - Firmware and Driver version combination not supported for the component and the server, operating system combination. * `FirmwareVersionAndDriverNameNotSupported` - Firmware Version and Driver name or not supported with the component and the server, operating system combination. * `InternalError` - API requests to the service have either failed or timed out. * `MarshallingError` - Error in JSON marshalling. * `Exempted` - An exempted error code means that the product is part of the exempted Catalog and should be ignored for HCL validation purposes.. [optional] if omitted the server will use the default value of "Success"  # noqa: E501
            id (str): Identifier of the hardware compatibility profile.. [optional]  # noqa: E501
            os_vendor (str): Vendor of the Operating System running on the server.. [optional]  # noqa: E501
            os_version (str): Version of the Operating System running on the server.. [optional]  # noqa: E501
            personality (str): Personality indicating the personality with the which the sever is used in a Hyperflex environment.. [optional]  # noqa: E501
            processor_model (str): Model of the processor present in the server.. [optional]  # noqa: E501
            products ([HclProduct], none_type): [optional]  # noqa: E501
            server_model (str): Model of the server as returned by UCSM/CIMC XML API.. [optional]  # noqa: E501
            server_revision (str): Revision of the server model.. [optional]  # noqa: E501
            ucs_version (str): Version of the UCS software.. [optional]  # noqa: E501
            version_type (str): Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release. * `UCSM` - The server is managed by UCS Manager. * `IMC` - The server is standalone managed by CIMC.. [optional] if omitted the server will use the default value of "UCSM"  # noqa: E501
        """

        class_id = "hcl.HardwareCompatibilityProfile" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "hcl.HardwareCompatibilityProfile")
        object_type = "hcl.HardwareCompatibilityProfile" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "hcl.HardwareCompatibilityProfile")
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

        self.class_id = class_id
        self.object_type = object_type
        for var_name, var_value in kwargs.items():
            if var_name in self.read_only_vars:
                set_model_init_error(f"Warning : {var_name} is omitted from request payload as it is a read-only property")
                continue
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
