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
    from intersight.model.ippool_ip_lease_relationship import IppoolIpLeaseRelationship
    from intersight.model.ippool_ip_v4_config import IppoolIpV4Config
    from intersight.model.ippool_ip_v6_config import IppoolIpV6Config
    from intersight.model.macpool_lease_relationship import MacpoolLeaseRelationship
    from intersight.model.motemplate_action_entry import MotemplateActionEntry
    from intersight.model.motemplate_sync_error import MotemplateSyncError
    from intersight.model.policy_abstract_config_profile_relationship import PolicyAbstractConfigProfileRelationship
    from intersight.model.vnic_eth_if_relationship import VnicEthIfRelationship
    from intersight.model.vnic_lan_connectivity_policy_relationship import VnicLanConnectivityPolicyRelationship
    from intersight.model.vnic_placement_settings import VnicPlacementSettings
    from intersight.model.vnic_vnic_template_relationship import VnicVnicTemplateRelationship
    globals()['IppoolIpLeaseRelationship'] = IppoolIpLeaseRelationship
    globals()['IppoolIpV4Config'] = IppoolIpV4Config
    globals()['IppoolIpV6Config'] = IppoolIpV6Config
    globals()['MacpoolLeaseRelationship'] = MacpoolLeaseRelationship
    globals()['MotemplateActionEntry'] = MotemplateActionEntry
    globals()['MotemplateSyncError'] = MotemplateSyncError
    globals()['PolicyAbstractConfigProfileRelationship'] = PolicyAbstractConfigProfileRelationship
    globals()['VnicEthIfRelationship'] = VnicEthIfRelationship
    globals()['VnicLanConnectivityPolicyRelationship'] = VnicLanConnectivityPolicyRelationship
    globals()['VnicPlacementSettings'] = VnicPlacementSettings
    globals()['VnicVnicTemplateRelationship'] = VnicVnicTemplateRelationship


class VnicEthIfAllOf(ModelNormal):
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
            'VNIC.ETHIF': "vnic.EthIf",
        },
        ('object_type',): {
            'VNIC.ETHIF': "vnic.EthIf",
        },
        ('iscsi_ip_v4_address_allocation_type',): {
            'NONE': "None",
            'DHCP': "DHCP",
            'STATIC': "Static",
            'POOL': "Pool",
        },
        ('iscsi_ip_v6_address_allocation_type',): {
            'NONE': "None",
            'DHCP': "DHCP",
            'STATIC': "Static",
            'POOL': "Pool",
        },
        ('mac_address_type',): {
            'POOL': "POOL",
            'STATIC': "STATIC",
        },
        ('template_sync_status',): {
            'NONE': "None",
            'OK': "OK",
            'SCHEDULED': "Scheduled",
            'INPROGRESS': "InProgress",
            'OUTOFSYNC': "OutOfSync",
        },
    }

    validations = {
        ('iscsi_ipv4_address',): {
            'regex': {
                'pattern': r'^$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$',  # noqa: E501
            },
        },
        ('iscsi_ipv6_address',): {
            'regex': {
                'pattern': r'^$|^(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:)$',  # noqa: E501
            },
        },
        ('name',): {
            'max_length': 31,
            'regex': {
                'pattern': r'^[a-zA-Z0-9-._:]+$',  # noqa: E501
            },
        },
        ('order',): {
            'inclusive_minimum': 0,
        },
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
            'iscsi_ip_v4_address_allocation_type': (str,),  # noqa: E501
            'iscsi_ip_v4_config': (IppoolIpV4Config,),  # noqa: E501
            'iscsi_ip_v6_address_allocation_type': (str,),  # noqa: E501
            'iscsi_ip_v6_config': (IppoolIpV6Config,),  # noqa: E501
            'iscsi_ipv4_address': (str,),  # noqa: E501
            'iscsi_ipv6_address': (str,),  # noqa: E501
            'mac_address': (str,),  # noqa: E501
            'mac_address_type': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'order': (int,),  # noqa: E501
            'overridden_list': ([str], none_type,),  # noqa: E501
            'placement': (VnicPlacementSettings,),  # noqa: E501
            'standby_vif_id': (int,),  # noqa: E501
            'static_mac_address': (str,),  # noqa: E501
            'template_actions': ([MotemplateActionEntry], none_type,),  # noqa: E501
            'template_sync_errors': ([MotemplateSyncError], none_type,),  # noqa: E501
            'template_sync_status': (str,),  # noqa: E501
            'vif_id': (int,),  # noqa: E501
            'ip_lease': (IppoolIpLeaseRelationship,),  # noqa: E501
            'lan_connectivity_policy': (VnicLanConnectivityPolicyRelationship,),  # noqa: E501
            'lcp_vnic': (VnicEthIfRelationship,),  # noqa: E501
            'mac_lease': (MacpoolLeaseRelationship,),  # noqa: E501
            'profile': (PolicyAbstractConfigProfileRelationship,),  # noqa: E501
            'sp_vnics': ([VnicEthIfRelationship], none_type,),  # noqa: E501
            'src_template': (VnicVnicTemplateRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'iscsi_ip_v4_address_allocation_type': 'IscsiIpV4AddressAllocationType',  # noqa: E501
        'iscsi_ip_v4_config': 'IscsiIpV4Config',  # noqa: E501
        'iscsi_ip_v6_address_allocation_type': 'IscsiIpV6AddressAllocationType',  # noqa: E501
        'iscsi_ip_v6_config': 'IscsiIpV6Config',  # noqa: E501
        'iscsi_ipv4_address': 'IscsiIpv4Address',  # noqa: E501
        'iscsi_ipv6_address': 'IscsiIpv6Address',  # noqa: E501
        'mac_address': 'MacAddress',  # noqa: E501
        'mac_address_type': 'MacAddressType',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'order': 'Order',  # noqa: E501
        'overridden_list': 'OverriddenList',  # noqa: E501
        'placement': 'Placement',  # noqa: E501
        'standby_vif_id': 'StandbyVifId',  # noqa: E501
        'static_mac_address': 'StaticMacAddress',  # noqa: E501
        'template_actions': 'TemplateActions',  # noqa: E501
        'template_sync_errors': 'TemplateSyncErrors',  # noqa: E501
        'template_sync_status': 'TemplateSyncStatus',  # noqa: E501
        'vif_id': 'VifId',  # noqa: E501
        'ip_lease': 'IpLease',  # noqa: E501
        'lan_connectivity_policy': 'LanConnectivityPolicy',  # noqa: E501
        'lcp_vnic': 'LcpVnic',  # noqa: E501
        'mac_lease': 'MacLease',  # noqa: E501
        'profile': 'Profile',  # noqa: E501
        'sp_vnics': 'SpVnics',  # noqa: E501
        'src_template': 'SrcTemplate',  # noqa: E501
    }

    read_only_vars = {
        'iscsi_ip_v4_address_allocation_type',  # noqa: E501
        'iscsi_ip_v6_address_allocation_type',  # noqa: E501
        'iscsi_ipv4_address',  # noqa: E501
        'iscsi_ipv6_address',  # noqa: E501
        'mac_address',  # noqa: E501
        'standby_vif_id',  # noqa: E501
        'template_sync_status',  # noqa: E501
        'vif_id',  # noqa: E501
        'sp_vnics',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """VnicEthIfAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "vnic.EthIf", must be one of ["vnic.EthIf", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "vnic.EthIf", must be one of ["vnic.EthIf", ]  # noqa: E501
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
            iscsi_ip_v4_address_allocation_type (str): Static/Pool/DHCP Type of IP address allocated to the vNIC. It is derived from iSCSI boot policy IP Address type. * `None` - Type indicates that there is no IP associated to an vnic. * `DHCP` - The IP address is assigned using DHCP, if available. * `Static` - Static IPv4 address is assigned to the iSCSI boot interface based on the information entered in this area. * `Pool` - An IPv4 address is assigned to the iSCSI boot interface from the management IP address pool.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            iscsi_ip_v4_config (IppoolIpV4Config): [optional]  # noqa: E501
            iscsi_ip_v6_address_allocation_type (str): Static/Pool/DHCP Type of IPv6 address allocated to the vNIC. It is derived from iSCSI boot policy IP Address type. * `None` - Type indicates that there is no IP associated to an vnic. * `DHCP` - The IP address is assigned using DHCP, if available. * `Static` - Static IPv4 address is assigned to the iSCSI boot interface based on the information entered in this area. * `Pool` - An IPv4 address is assigned to the iSCSI boot interface from the management IP address pool.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            iscsi_ip_v6_config (IppoolIpV6Config): [optional]  # noqa: E501
            iscsi_ipv4_address (str): IP address associated to the vNIC.. [optional]  # noqa: E501
            iscsi_ipv6_address (str): IPv6 address associated to the iSCSI vNIC.. [optional]  # noqa: E501
            mac_address (str): The MAC address that is assigned to the vNIC based on the MAC pool that has been assigned to the LAN Connectivity Policy.. [optional]  # noqa: E501
            mac_address_type (str): Type of allocation selected to assign a MAC address for the vnic. * `POOL` - The user selects a pool from which the mac/wwn address will be leased for the Virtual Interface. * `STATIC` - The user assigns a static mac/wwn address for the Virtual Interface.. [optional] if omitted the server will use the default value of "POOL"  # noqa: E501
            name (str): Name of the virtual ethernet interface.. [optional]  # noqa: E501
            order (int): The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The order should start from zero with no overlaps. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1340, VIC 1380 and VIC 1385 which have two.. [optional]  # noqa: E501
            overridden_list ([str], none_type): [optional]  # noqa: E501
            placement (VnicPlacementSettings): [optional]  # noqa: E501
            standby_vif_id (int): The Standby VIF Id is applicable for failover enabled vNICS. It should be the same as the channel number of the standby vethernet created on switch in order to set up the standby data path.. [optional]  # noqa: E501
            static_mac_address (str): The MAC address must be in hexadecimal format xx:xx:xx:xx:xx:xx. To ensure uniqueness of MACs in the LAN fabric, you are strongly encouraged to use the following MAC prefix 00:25:B5:xx:xx:xx.. [optional]  # noqa: E501
            template_actions ([MotemplateActionEntry], none_type): [optional]  # noqa: E501
            template_sync_errors ([MotemplateSyncError], none_type): [optional]  # noqa: E501
            template_sync_status (str): The sync status of the current MO wrt the attached Template MO. * `None` - The Enum value represents that the object is not attached to any template. * `OK` - The Enum value represents that the object values are in sync with attached template. * `Scheduled` - The Enum value represents that the object sync from attached template is scheduled from template. * `InProgress` - The Enum value represents that the object sync with the attached template is in progress. * `OutOfSync` - The Enum value represents that the object values are not in sync with attached template.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            vif_id (int): The Vif Id should be same as the channel number of the vethernet created on switch in order to set up the data path. The property is applicable only for FI attached servers where a vethernet is created on the switch for every vNIC.. [optional]  # noqa: E501
            ip_lease (IppoolIpLeaseRelationship): [optional]  # noqa: E501
            lan_connectivity_policy (VnicLanConnectivityPolicyRelationship): [optional]  # noqa: E501
            lcp_vnic (VnicEthIfRelationship): [optional]  # noqa: E501
            mac_lease (MacpoolLeaseRelationship): [optional]  # noqa: E501
            profile (PolicyAbstractConfigProfileRelationship): [optional]  # noqa: E501
            sp_vnics ([VnicEthIfRelationship], none_type): An array of relationships to vnicEthIf resources.. [optional]  # noqa: E501
            src_template (VnicVnicTemplateRelationship): [optional]  # noqa: E501
        """

        class_id = "vnic.EthIf" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "vnic.EthIf")
        object_type = "vnic.EthIf" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "vnic.EthIf")
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
        """VnicEthIfAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "vnic.EthIf", must be one of ["vnic.EthIf", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "vnic.EthIf", must be one of ["vnic.EthIf", ]  # noqa: E501
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
            iscsi_ip_v4_address_allocation_type (str): Static/Pool/DHCP Type of IP address allocated to the vNIC. It is derived from iSCSI boot policy IP Address type. * `None` - Type indicates that there is no IP associated to an vnic. * `DHCP` - The IP address is assigned using DHCP, if available. * `Static` - Static IPv4 address is assigned to the iSCSI boot interface based on the information entered in this area. * `Pool` - An IPv4 address is assigned to the iSCSI boot interface from the management IP address pool.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            iscsi_ip_v4_config (IppoolIpV4Config): [optional]  # noqa: E501
            iscsi_ip_v6_address_allocation_type (str): Static/Pool/DHCP Type of IPv6 address allocated to the vNIC. It is derived from iSCSI boot policy IP Address type. * `None` - Type indicates that there is no IP associated to an vnic. * `DHCP` - The IP address is assigned using DHCP, if available. * `Static` - Static IPv4 address is assigned to the iSCSI boot interface based on the information entered in this area. * `Pool` - An IPv4 address is assigned to the iSCSI boot interface from the management IP address pool.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            iscsi_ip_v6_config (IppoolIpV6Config): [optional]  # noqa: E501
            iscsi_ipv4_address (str): IP address associated to the vNIC.. [optional]  # noqa: E501
            iscsi_ipv6_address (str): IPv6 address associated to the iSCSI vNIC.. [optional]  # noqa: E501
            mac_address (str): The MAC address that is assigned to the vNIC based on the MAC pool that has been assigned to the LAN Connectivity Policy.. [optional]  # noqa: E501
            mac_address_type (str): Type of allocation selected to assign a MAC address for the vnic. * `POOL` - The user selects a pool from which the mac/wwn address will be leased for the Virtual Interface. * `STATIC` - The user assigns a static mac/wwn address for the Virtual Interface.. [optional] if omitted the server will use the default value of "POOL"  # noqa: E501
            name (str): Name of the virtual ethernet interface.. [optional]  # noqa: E501
            order (int): The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The order should start from zero with no overlaps. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1340, VIC 1380 and VIC 1385 which have two.. [optional]  # noqa: E501
            overridden_list ([str], none_type): [optional]  # noqa: E501
            placement (VnicPlacementSettings): [optional]  # noqa: E501
            standby_vif_id (int): The Standby VIF Id is applicable for failover enabled vNICS. It should be the same as the channel number of the standby vethernet created on switch in order to set up the standby data path.. [optional]  # noqa: E501
            static_mac_address (str): The MAC address must be in hexadecimal format xx:xx:xx:xx:xx:xx. To ensure uniqueness of MACs in the LAN fabric, you are strongly encouraged to use the following MAC prefix 00:25:B5:xx:xx:xx.. [optional]  # noqa: E501
            template_actions ([MotemplateActionEntry], none_type): [optional]  # noqa: E501
            template_sync_errors ([MotemplateSyncError], none_type): [optional]  # noqa: E501
            template_sync_status (str): The sync status of the current MO wrt the attached Template MO. * `None` - The Enum value represents that the object is not attached to any template. * `OK` - The Enum value represents that the object values are in sync with attached template. * `Scheduled` - The Enum value represents that the object sync from attached template is scheduled from template. * `InProgress` - The Enum value represents that the object sync with the attached template is in progress. * `OutOfSync` - The Enum value represents that the object values are not in sync with attached template.. [optional] if omitted the server will use the default value of "None"  # noqa: E501
            vif_id (int): The Vif Id should be same as the channel number of the vethernet created on switch in order to set up the data path. The property is applicable only for FI attached servers where a vethernet is created on the switch for every vNIC.. [optional]  # noqa: E501
            ip_lease (IppoolIpLeaseRelationship): [optional]  # noqa: E501
            lan_connectivity_policy (VnicLanConnectivityPolicyRelationship): [optional]  # noqa: E501
            lcp_vnic (VnicEthIfRelationship): [optional]  # noqa: E501
            mac_lease (MacpoolLeaseRelationship): [optional]  # noqa: E501
            profile (PolicyAbstractConfigProfileRelationship): [optional]  # noqa: E501
            sp_vnics ([VnicEthIfRelationship], none_type): An array of relationships to vnicEthIf resources.. [optional]  # noqa: E501
            src_template (VnicVnicTemplateRelationship): [optional]  # noqa: E501
        """

        class_id = "vnic.EthIf" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "vnic.EthIf")
        object_type = "vnic.EthIf" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "vnic.EthIf")
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
