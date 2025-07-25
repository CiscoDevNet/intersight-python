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
    from intersight.model.asset_contract_information import AssetContractInformation
    from intersight.model.asset_customer_information import AssetCustomerInformation
    from intersight.model.asset_device_registration_relationship import AssetDeviceRegistrationRelationship
    from intersight.model.asset_global_ultimate import AssetGlobalUltimate
    from intersight.model.asset_product_information import AssetProductInformation
    globals()['AssetContractInformation'] = AssetContractInformation
    globals()['AssetCustomerInformation'] = AssetCustomerInformation
    globals()['AssetDeviceRegistrationRelationship'] = AssetDeviceRegistrationRelationship
    globals()['AssetGlobalUltimate'] = AssetGlobalUltimate
    globals()['AssetProductInformation'] = AssetProductInformation


class AssetDeviceContractNotificationAllOf(ModelNormal):
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
            'ASSET.DEVICECONTRACTNOTIFICATION': "asset.DeviceContractNotification",
        },
        ('object_type',): {
            'ASSET.DEVICECONTRACTNOTIFICATION': "asset.DeviceContractNotification",
        },
        ('contract_status',): {
            'UNKNOWN': "Unknown",
            'NOT_COVERED': "Not Covered",
            'ACTIVE': "Active",
            'EXPIRING_SOON': "Expiring Soon",
        },
        ('contract_status_reason',): {
            'EMPTY': "",
            'LINE_ITEM_EXPIRED': "Line Item Expired",
            'LINE_ITEM_TERMINATED': "Line Item Terminated",
        },
        ('state_contract',): {
            'UPDATE': "Update",
            'OK': "OK",
            'FAILED': "Failed",
            'RETRY': "Retry",
        },
        ('state_sn2_info',): {
            'UPDATE': "Update",
            'OK': "OK",
            'FAILED': "Failed",
            'RETRY': "Retry",
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
            'contract': (AssetContractInformation,),  # noqa: E501
            'contract_status': (str,),  # noqa: E501
            'contract_status_reason': (str,),  # noqa: E501
            'contract_updated_time': (datetime,),  # noqa: E501
            'covered_product_line_end_date': (str,),  # noqa: E501
            'device_id': (str,),  # noqa: E501
            'end_customer': (AssetCustomerInformation,),  # noqa: E501
            'end_user_global_ultimate': (AssetGlobalUltimate,),  # noqa: E501
            'is_valid': (bool,),  # noqa: E501
            'item_type': (str,),  # noqa: E501
            'last_date_of_support': (datetime,),  # noqa: E501
            'maintenance_purchase_order_number': (str,),  # noqa: E501
            'maintenance_sales_order_number': (str,),  # noqa: E501
            'product': (AssetProductInformation,),  # noqa: E501
            'purchase_order_number': (str,),  # noqa: E501
            'reseller_global_ultimate': (AssetGlobalUltimate,),  # noqa: E501
            'sales_order_number': (str,),  # noqa: E501
            'service_description': (str,),  # noqa: E501
            'service_end_date': (datetime,),  # noqa: E501
            'service_level': (str,),  # noqa: E501
            'service_sku': (str,),  # noqa: E501
            'service_start_date': (datetime,),  # noqa: E501
            'state_contract': (str,),  # noqa: E501
            'state_sn2_info': (str,),  # noqa: E501
            'warranty_end_date': (str,),  # noqa: E501
            'warranty_type': (str,),  # noqa: E501
            'registered_device': (AssetDeviceRegistrationRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'contract': 'Contract',  # noqa: E501
        'contract_status': 'ContractStatus',  # noqa: E501
        'contract_status_reason': 'ContractStatusReason',  # noqa: E501
        'contract_updated_time': 'ContractUpdatedTime',  # noqa: E501
        'covered_product_line_end_date': 'CoveredProductLineEndDate',  # noqa: E501
        'device_id': 'DeviceId',  # noqa: E501
        'end_customer': 'EndCustomer',  # noqa: E501
        'end_user_global_ultimate': 'EndUserGlobalUltimate',  # noqa: E501
        'is_valid': 'IsValid',  # noqa: E501
        'item_type': 'ItemType',  # noqa: E501
        'last_date_of_support': 'LastDateOfSupport',  # noqa: E501
        'maintenance_purchase_order_number': 'MaintenancePurchaseOrderNumber',  # noqa: E501
        'maintenance_sales_order_number': 'MaintenanceSalesOrderNumber',  # noqa: E501
        'product': 'Product',  # noqa: E501
        'purchase_order_number': 'PurchaseOrderNumber',  # noqa: E501
        'reseller_global_ultimate': 'ResellerGlobalUltimate',  # noqa: E501
        'sales_order_number': 'SalesOrderNumber',  # noqa: E501
        'service_description': 'ServiceDescription',  # noqa: E501
        'service_end_date': 'ServiceEndDate',  # noqa: E501
        'service_level': 'ServiceLevel',  # noqa: E501
        'service_sku': 'ServiceSku',  # noqa: E501
        'service_start_date': 'ServiceStartDate',  # noqa: E501
        'state_contract': 'StateContract',  # noqa: E501
        'state_sn2_info': 'StateSn2Info',  # noqa: E501
        'warranty_end_date': 'WarrantyEndDate',  # noqa: E501
        'warranty_type': 'WarrantyType',  # noqa: E501
        'registered_device': 'RegisteredDevice',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AssetDeviceContractNotificationAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "asset.DeviceContractNotification", must be one of ["asset.DeviceContractNotification", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "asset.DeviceContractNotification", must be one of ["asset.DeviceContractNotification", ]  # noqa: E501
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
            contract (AssetContractInformation): [optional]  # noqa: E501
            contract_status (str): Calculated contract status that is derived based on the service line status and contract end date. It is different from serviceLineStatus property. serviceLineStatus gives us ACTIVE, OVERDUE, EXPIRED. These are transformed into Active, Expiring Soon and Not Covered. * `Unknown` - The device's contract status cannot be determined. * `Not Covered` - The Cisco device does not have a valid support contract. * `Active` - The Cisco device is covered under a active support contract. * `Expiring Soon` - The contract for this Cisco device is going to expire in the next 30 days.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            contract_status_reason (str): Reason for contract status. In case of Not Covered, reason is either Terminated or Expired. * `` - There is no reason for the specified contract status. * `Line Item Expired` - The Cisco device does not have a valid support contract, it has expired. * `Line Item Terminated` - The Cisco device does not have a valid support contract, it has been terminated.. [optional] if omitted the server will use the default value of ""  # noqa: E501
            contract_updated_time (datetime): Date and time indicating when the contract data is last refreshed.. [optional]  # noqa: E501
            covered_product_line_end_date (str): End date of the covered product line. The coverage end date is fetched from Cisco SN2INFO API.. [optional]  # noqa: E501
            device_id (str): Unique identifier of the Cisco device.. [optional]  # noqa: E501
            end_customer (AssetCustomerInformation): [optional]  # noqa: E501
            end_user_global_ultimate (AssetGlobalUltimate): [optional]  # noqa: E501
            is_valid (bool): Validates if the device is a genuine Cisco device. Validated is done using the Cisco SN2INFO APIs.. [optional]  # noqa: E501
            item_type (str): Item type of this specific Cisco device. example \"Chassis\".. [optional]  # noqa: E501
            last_date_of_support (datetime): The last date of hardware support for this device.. [optional]  # noqa: E501
            maintenance_purchase_order_number (str): Maintenance purchase order number for the Cisco device.. [optional]  # noqa: E501
            maintenance_sales_order_number (str): Maintenance sales order number for the Cisco device.. [optional]  # noqa: E501
            product (AssetProductInformation): [optional]  # noqa: E501
            purchase_order_number (str): Purchase order number for the Cisco device. It is a unique number assigned for every purchase.. [optional]  # noqa: E501
            reseller_global_ultimate (AssetGlobalUltimate): [optional]  # noqa: E501
            sales_order_number (str): Sales order number for the Cisco device. It is a unique number assigned for every sale.. [optional]  # noqa: E501
            service_description (str): The type of service contract that covers the Cisco device.. [optional]  # noqa: E501
            service_end_date (datetime): End date for the Cisco service contract that covers this Cisco device.. [optional]  # noqa: E501
            service_level (str): The type of service contract that covers the Cisco device.. [optional]  # noqa: E501
            service_sku (str): The SKU of the service contract that covers the Cisco device.. [optional]  # noqa: E501
            service_start_date (datetime): Start date for the Cisco service contract that covers this Cisco device.. [optional]  # noqa: E501
            state_contract (str): Internal property used for triggering and tracking actions for contract information. * `Update` - Sn2Info/Contract information needs to be updated. * `OK` - Sn2Info/Contract information was fetched succcessfuly and updated. * `Failed` - Sn2Info/Contract information was not available  or failed while fetching. * `Retry` - Sn2Info/Contract information update failed and will be retried later.. [optional] if omitted the server will use the default value of "Update"  # noqa: E501
            state_sn2_info (str): Internal property used for triggering and tracking actions for sn2info information. * `Update` - Sn2Info/Contract information needs to be updated. * `OK` - Sn2Info/Contract information was fetched succcessfuly and updated. * `Failed` - Sn2Info/Contract information was not available  or failed while fetching. * `Retry` - Sn2Info/Contract information update failed and will be retried later.. [optional] if omitted the server will use the default value of "Update"  # noqa: E501
            warranty_end_date (str): End date for the warranty that covers the Cisco device.. [optional]  # noqa: E501
            warranty_type (str): Type of warranty that covers the Cisco device.. [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
        """

        class_id = "asset.DeviceContractNotification" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "asset.DeviceContractNotification")
        object_type = "asset.DeviceContractNotification" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "asset.DeviceContractNotification")
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
        """AssetDeviceContractNotificationAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "asset.DeviceContractNotification", must be one of ["asset.DeviceContractNotification", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "asset.DeviceContractNotification", must be one of ["asset.DeviceContractNotification", ]  # noqa: E501
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
            contract (AssetContractInformation): [optional]  # noqa: E501
            contract_status (str): Calculated contract status that is derived based on the service line status and contract end date. It is different from serviceLineStatus property. serviceLineStatus gives us ACTIVE, OVERDUE, EXPIRED. These are transformed into Active, Expiring Soon and Not Covered. * `Unknown` - The device's contract status cannot be determined. * `Not Covered` - The Cisco device does not have a valid support contract. * `Active` - The Cisco device is covered under a active support contract. * `Expiring Soon` - The contract for this Cisco device is going to expire in the next 30 days.. [optional] if omitted the server will use the default value of "Unknown"  # noqa: E501
            contract_status_reason (str): Reason for contract status. In case of Not Covered, reason is either Terminated or Expired. * `` - There is no reason for the specified contract status. * `Line Item Expired` - The Cisco device does not have a valid support contract, it has expired. * `Line Item Terminated` - The Cisco device does not have a valid support contract, it has been terminated.. [optional] if omitted the server will use the default value of ""  # noqa: E501
            contract_updated_time (datetime): Date and time indicating when the contract data is last refreshed.. [optional]  # noqa: E501
            covered_product_line_end_date (str): End date of the covered product line. The coverage end date is fetched from Cisco SN2INFO API.. [optional]  # noqa: E501
            device_id (str): Unique identifier of the Cisco device.. [optional]  # noqa: E501
            end_customer (AssetCustomerInformation): [optional]  # noqa: E501
            end_user_global_ultimate (AssetGlobalUltimate): [optional]  # noqa: E501
            is_valid (bool): Validates if the device is a genuine Cisco device. Validated is done using the Cisco SN2INFO APIs.. [optional]  # noqa: E501
            item_type (str): Item type of this specific Cisco device. example \"Chassis\".. [optional]  # noqa: E501
            last_date_of_support (datetime): The last date of hardware support for this device.. [optional]  # noqa: E501
            maintenance_purchase_order_number (str): Maintenance purchase order number for the Cisco device.. [optional]  # noqa: E501
            maintenance_sales_order_number (str): Maintenance sales order number for the Cisco device.. [optional]  # noqa: E501
            product (AssetProductInformation): [optional]  # noqa: E501
            purchase_order_number (str): Purchase order number for the Cisco device. It is a unique number assigned for every purchase.. [optional]  # noqa: E501
            reseller_global_ultimate (AssetGlobalUltimate): [optional]  # noqa: E501
            sales_order_number (str): Sales order number for the Cisco device. It is a unique number assigned for every sale.. [optional]  # noqa: E501
            service_description (str): The type of service contract that covers the Cisco device.. [optional]  # noqa: E501
            service_end_date (datetime): End date for the Cisco service contract that covers this Cisco device.. [optional]  # noqa: E501
            service_level (str): The type of service contract that covers the Cisco device.. [optional]  # noqa: E501
            service_sku (str): The SKU of the service contract that covers the Cisco device.. [optional]  # noqa: E501
            service_start_date (datetime): Start date for the Cisco service contract that covers this Cisco device.. [optional]  # noqa: E501
            state_contract (str): Internal property used for triggering and tracking actions for contract information. * `Update` - Sn2Info/Contract information needs to be updated. * `OK` - Sn2Info/Contract information was fetched succcessfuly and updated. * `Failed` - Sn2Info/Contract information was not available  or failed while fetching. * `Retry` - Sn2Info/Contract information update failed and will be retried later.. [optional] if omitted the server will use the default value of "Update"  # noqa: E501
            state_sn2_info (str): Internal property used for triggering and tracking actions for sn2info information. * `Update` - Sn2Info/Contract information needs to be updated. * `OK` - Sn2Info/Contract information was fetched succcessfuly and updated. * `Failed` - Sn2Info/Contract information was not available  or failed while fetching. * `Retry` - Sn2Info/Contract information update failed and will be retried later.. [optional] if omitted the server will use the default value of "Update"  # noqa: E501
            warranty_end_date (str): End date for the warranty that covers the Cisco device.. [optional]  # noqa: E501
            warranty_type (str): Type of warranty that covers the Cisco device.. [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
        """

        class_id = "asset.DeviceContractNotification" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "asset.DeviceContractNotification")
        object_type = "asset.DeviceContractNotification" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "asset.DeviceContractNotification")
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
