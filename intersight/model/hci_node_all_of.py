"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations. The Intersight OpenAPI document defines the complete set of properties that are returned in the HTTP response. From that perspective, a client can expect that no additional properties are returned, unless these properties are explicitly defined in the OpenAPI document. However, when a client uses an older version of the Intersight OpenAPI document, the server may send additional properties because the software is more recent than the client. In that case, the client may receive properties that it does not know about. Some generated SDKs perform a strict validation of the HTTP response body against the OpenAPI document.  # noqa: E501

    The version of the OpenAPI document: 1.0.11-2024112619
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
    from intersight.model.asset_device_registration_relationship import AssetDeviceRegistrationRelationship
    from intersight.model.compute_physical_relationship import ComputePhysicalRelationship
    from intersight.model.hci_cluster_relationship import HciClusterRelationship
    from intersight.model.hci_disk_relationship import HciDiskRelationship
    from intersight.model.hci_gpu_relationship import HciGpuRelationship
    from intersight.model.hci_ip_address import HciIpAddress
    from intersight.model.hci_key_management_device_to_cert_status_info import HciKeyManagementDeviceToCertStatusInfo
    globals()['AssetDeviceRegistrationRelationship'] = AssetDeviceRegistrationRelationship
    globals()['ComputePhysicalRelationship'] = ComputePhysicalRelationship
    globals()['HciClusterRelationship'] = HciClusterRelationship
    globals()['HciDiskRelationship'] = HciDiskRelationship
    globals()['HciGpuRelationship'] = HciGpuRelationship
    globals()['HciIpAddress'] = HciIpAddress
    globals()['HciKeyManagementDeviceToCertStatusInfo'] = HciKeyManagementDeviceToCertStatusInfo


class HciNodeAllOf(ModelNormal):
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
            'HCI.NODE': "hci.Node",
        },
        ('object_type',): {
            'HCI.NODE': "hci.Node",
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
            'block_model': (str,),  # noqa: E501
            'block_serial': (str,),  # noqa: E501
            'boot_time_usecs': (int,),  # noqa: E501
            'cluster_ext_id': (str,),  # noqa: E501
            'cluster_name': (str,),  # noqa: E501
            'controller_vm_backplane_address': (HciIpAddress,),  # noqa: E501
            'controller_vm_external_address': (HciIpAddress,),  # noqa: E501
            'controller_vm_id': (int,),  # noqa: E501
            'controller_vm_maintanence_mode': (bool,),  # noqa: E501
            'controller_vm_nat_ip': (HciIpAddress,),  # noqa: E501
            'controller_vm_nat_port': (int,),  # noqa: E501
            'controller_vm_rdma_backplane_address': (HciIpAddress,),  # noqa: E501
            'controller_vm_server_uuid': (str,),  # noqa: E501
            'cpu_capacity_hz': (int,),  # noqa: E501
            'cpu_frequency_hz': (int,),  # noqa: E501
            'cpu_model': (str,),  # noqa: E501
            'cpu_usage_hz': (int,),  # noqa: E501
            'default_vhd_container_uuid': (str,),  # noqa: E501
            'default_vhd_location': (str,),  # noqa: E501
            'default_vm_container_uuid': (str,),  # noqa: E501
            'default_vm_location': (str,),  # noqa: E501
            'disk_count': (int,),  # noqa: E501
            'failover_cluster_fqdn': (str,),  # noqa: E501
            'failover_cluster_node_status': (str,),  # noqa: E501
            'gpu_count': (int,),  # noqa: E501
            'gpu_driver_version': (str,),  # noqa: E501
            'has_csr': (bool,),  # noqa: E501
            'host_name': (str,),  # noqa: E501
            'host_type': (str,),  # noqa: E501
            'hypervisor_acropolis_connection_state': (str,),  # noqa: E501
            'hypervisor_external_address': (HciIpAddress,),  # noqa: E501
            'hypervisor_number_of_vms': (int,),  # noqa: E501
            'hypervisor_state': (str,),  # noqa: E501
            'hypervisor_type': (str,),  # noqa: E501
            'hypervisor_user_name': (str,),  # noqa: E501
            'hypervisor_version': (str,),  # noqa: E501
            'ipmi_ip': (HciIpAddress,),  # noqa: E501
            'ipmi_username': (str,),  # noqa: E501
            'is_degraded': (bool,),  # noqa: E501
            'is_hardware_virtualized': (bool,),  # noqa: E501
            'is_secure_booted': (bool,),  # noqa: E501
            'key_management_device_to_cert_status': ([HciKeyManagementDeviceToCertStatusInfo], none_type,),  # noqa: E501
            'maintenance_state': (str,),  # noqa: E501
            'memory_capacity_bytes': (int,),  # noqa: E501
            'memory_size_bytes': (int,),  # noqa: E501
            'memory_usage_bytes': (int,),  # noqa: E501
            'node_ext_id': (str,),  # noqa: E501
            'node_status': (str,),  # noqa: E501
            'number_of_cpu_cores': (int,),  # noqa: E501
            'number_of_cpu_sockets': (int,),  # noqa: E501
            'number_of_cpu_threads': (int,),  # noqa: E501
            'reboot_pending': (bool,),  # noqa: E501
            'storage_capacity_bytes': (int,),  # noqa: E501
            'storage_usage_bytes': (int,),  # noqa: E501
            'cluster': (HciClusterRelationship,),  # noqa: E501
            'disks': ([HciDiskRelationship], none_type,),  # noqa: E501
            'gpus': ([HciGpuRelationship], none_type,),  # noqa: E501
            'physical_server': (ComputePhysicalRelationship,),  # noqa: E501
            'registered_device': (AssetDeviceRegistrationRelationship,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'block_model': 'BlockModel',  # noqa: E501
        'block_serial': 'BlockSerial',  # noqa: E501
        'boot_time_usecs': 'BootTimeUsecs',  # noqa: E501
        'cluster_ext_id': 'ClusterExtId',  # noqa: E501
        'cluster_name': 'ClusterName',  # noqa: E501
        'controller_vm_backplane_address': 'ControllerVmBackplaneAddress',  # noqa: E501
        'controller_vm_external_address': 'ControllerVmExternalAddress',  # noqa: E501
        'controller_vm_id': 'ControllerVmId',  # noqa: E501
        'controller_vm_maintanence_mode': 'ControllerVmMaintanenceMode',  # noqa: E501
        'controller_vm_nat_ip': 'ControllerVmNatIp',  # noqa: E501
        'controller_vm_nat_port': 'ControllerVmNatPort',  # noqa: E501
        'controller_vm_rdma_backplane_address': 'ControllerVmRdmaBackplaneAddress',  # noqa: E501
        'controller_vm_server_uuid': 'ControllerVmServerUuid',  # noqa: E501
        'cpu_capacity_hz': 'CpuCapacityHz',  # noqa: E501
        'cpu_frequency_hz': 'CpuFrequencyHz',  # noqa: E501
        'cpu_model': 'CpuModel',  # noqa: E501
        'cpu_usage_hz': 'CpuUsageHz',  # noqa: E501
        'default_vhd_container_uuid': 'DefaultVhdContainerUuid',  # noqa: E501
        'default_vhd_location': 'DefaultVhdLocation',  # noqa: E501
        'default_vm_container_uuid': 'DefaultVmContainerUuid',  # noqa: E501
        'default_vm_location': 'DefaultVmLocation',  # noqa: E501
        'disk_count': 'DiskCount',  # noqa: E501
        'failover_cluster_fqdn': 'FailoverClusterFqdn',  # noqa: E501
        'failover_cluster_node_status': 'FailoverClusterNodeStatus',  # noqa: E501
        'gpu_count': 'GpuCount',  # noqa: E501
        'gpu_driver_version': 'GpuDriverVersion',  # noqa: E501
        'has_csr': 'HasCsr',  # noqa: E501
        'host_name': 'HostName',  # noqa: E501
        'host_type': 'HostType',  # noqa: E501
        'hypervisor_acropolis_connection_state': 'HypervisorAcropolisConnectionState',  # noqa: E501
        'hypervisor_external_address': 'HypervisorExternalAddress',  # noqa: E501
        'hypervisor_number_of_vms': 'HypervisorNumberOfVms',  # noqa: E501
        'hypervisor_state': 'HypervisorState',  # noqa: E501
        'hypervisor_type': 'HypervisorType',  # noqa: E501
        'hypervisor_user_name': 'HypervisorUserName',  # noqa: E501
        'hypervisor_version': 'HypervisorVersion',  # noqa: E501
        'ipmi_ip': 'IpmiIp',  # noqa: E501
        'ipmi_username': 'IpmiUsername',  # noqa: E501
        'is_degraded': 'IsDegraded',  # noqa: E501
        'is_hardware_virtualized': 'IsHardwareVirtualized',  # noqa: E501
        'is_secure_booted': 'IsSecureBooted',  # noqa: E501
        'key_management_device_to_cert_status': 'KeyManagementDeviceToCertStatus',  # noqa: E501
        'maintenance_state': 'MaintenanceState',  # noqa: E501
        'memory_capacity_bytes': 'MemoryCapacityBytes',  # noqa: E501
        'memory_size_bytes': 'MemorySizeBytes',  # noqa: E501
        'memory_usage_bytes': 'MemoryUsageBytes',  # noqa: E501
        'node_ext_id': 'NodeExtId',  # noqa: E501
        'node_status': 'NodeStatus',  # noqa: E501
        'number_of_cpu_cores': 'NumberOfCpuCores',  # noqa: E501
        'number_of_cpu_sockets': 'NumberOfCpuSockets',  # noqa: E501
        'number_of_cpu_threads': 'NumberOfCpuThreads',  # noqa: E501
        'reboot_pending': 'RebootPending',  # noqa: E501
        'storage_capacity_bytes': 'StorageCapacityBytes',  # noqa: E501
        'storage_usage_bytes': 'StorageUsageBytes',  # noqa: E501
        'cluster': 'Cluster',  # noqa: E501
        'disks': 'Disks',  # noqa: E501
        'gpus': 'Gpus',  # noqa: E501
        'physical_server': 'PhysicalServer',  # noqa: E501
        'registered_device': 'RegisteredDevice',  # noqa: E501
    }

    read_only_vars = {
        'block_model',  # noqa: E501
        'block_serial',  # noqa: E501
        'boot_time_usecs',  # noqa: E501
        'cluster_ext_id',  # noqa: E501
        'cluster_name',  # noqa: E501
        'controller_vm_id',  # noqa: E501
        'controller_vm_maintanence_mode',  # noqa: E501
        'controller_vm_nat_port',  # noqa: E501
        'controller_vm_server_uuid',  # noqa: E501
        'cpu_capacity_hz',  # noqa: E501
        'cpu_frequency_hz',  # noqa: E501
        'cpu_model',  # noqa: E501
        'cpu_usage_hz',  # noqa: E501
        'default_vhd_container_uuid',  # noqa: E501
        'default_vhd_location',  # noqa: E501
        'default_vm_container_uuid',  # noqa: E501
        'default_vm_location',  # noqa: E501
        'disk_count',  # noqa: E501
        'failover_cluster_fqdn',  # noqa: E501
        'failover_cluster_node_status',  # noqa: E501
        'gpu_count',  # noqa: E501
        'gpu_driver_version',  # noqa: E501
        'has_csr',  # noqa: E501
        'host_name',  # noqa: E501
        'host_type',  # noqa: E501
        'hypervisor_acropolis_connection_state',  # noqa: E501
        'hypervisor_number_of_vms',  # noqa: E501
        'hypervisor_state',  # noqa: E501
        'hypervisor_type',  # noqa: E501
        'hypervisor_user_name',  # noqa: E501
        'hypervisor_version',  # noqa: E501
        'ipmi_username',  # noqa: E501
        'is_degraded',  # noqa: E501
        'is_hardware_virtualized',  # noqa: E501
        'is_secure_booted',  # noqa: E501
        'maintenance_state',  # noqa: E501
        'memory_capacity_bytes',  # noqa: E501
        'memory_size_bytes',  # noqa: E501
        'memory_usage_bytes',  # noqa: E501
        'node_ext_id',  # noqa: E501
        'node_status',  # noqa: E501
        'number_of_cpu_cores',  # noqa: E501
        'number_of_cpu_sockets',  # noqa: E501
        'number_of_cpu_threads',  # noqa: E501
        'reboot_pending',  # noqa: E501
        'storage_capacity_bytes',  # noqa: E501
        'storage_usage_bytes',  # noqa: E501
        'disks',  # noqa: E501
        'gpus',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """HciNodeAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "hci.Node", must be one of ["hci.Node", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "hci.Node", must be one of ["hci.Node", ]  # noqa: E501
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
            block_model (str): The rackable unit model of the node.. [optional]  # noqa: E501
            block_serial (str): The rackable unit serial number of the node.. [optional]  # noqa: E501
            boot_time_usecs (int): The boot time in microseconds of the node.. [optional]  # noqa: E501
            cluster_ext_id (str): The unique identifier of the cluster.. [optional]  # noqa: E501
            cluster_name (str): The name of the cluster this node belongs to.. [optional]  # noqa: E501
            controller_vm_backplane_address (HciIpAddress): [optional]  # noqa: E501
            controller_vm_external_address (HciIpAddress): [optional]  # noqa: E501
            controller_vm_id (int): The identifier number of the controller VM.. [optional]  # noqa: E501
            controller_vm_maintanence_mode (bool): The maintenance mode status of the controller VM.. [optional]  # noqa: E501
            controller_vm_nat_ip (HciIpAddress): [optional]  # noqa: E501
            controller_vm_nat_port (int): The NAT port of the controller VM.. [optional]  # noqa: E501
            controller_vm_rdma_backplane_address (HciIpAddress): [optional]  # noqa: E501
            controller_vm_server_uuid (str): The Rackable unit UUID of the server.. [optional]  # noqa: E501
            cpu_capacity_hz (int): The CPU capacity in Hz of the node.. [optional]  # noqa: E501
            cpu_frequency_hz (int): The CPU frequency in Hz on the node.. [optional]  # noqa: E501
            cpu_model (str): The CPU model of the node.. [optional]  # noqa: E501
            cpu_usage_hz (int): The CPU usage in Hz of the node.. [optional]  # noqa: E501
            default_vhd_container_uuid (str): The default VHD container UUID of the node.. [optional]  # noqa: E501
            default_vhd_location (str): The default VHD location of the node.. [optional]  # noqa: E501
            default_vm_container_uuid (str): The default VM container UUID of the node.. [optional]  # noqa: E501
            default_vm_location (str): The default VM location of the node.. [optional]  # noqa: E501
            disk_count (int): The number of disks on the node.. [optional]  # noqa: E501
            failover_cluster_fqdn (str): The failover cluster FQDN of the node.. [optional]  # noqa: E501
            failover_cluster_node_status (str): The failover cluster node status of the node.. [optional]  # noqa: E501
            gpu_count (int): The number of GPUs on the node.. [optional]  # noqa: E501
            gpu_driver_version (str): The GPU driver version of the node.. [optional]  # noqa: E501
            has_csr (bool): Certificate signing request status of the node.. [optional]  # noqa: E501
            host_name (str): The name of the host the node is running on.. [optional]  # noqa: E501
            host_type (str): The type of the host, e.g. HYPER_CONVERGED, COMPUTE_ONLY, STORAGE_ONLY.. [optional]  # noqa: E501
            hypervisor_acropolis_connection_state (str): The connection state of the hypervisor, e.g. CONNECTED, DISCONNECTED, NOT_AVAILABLE.. [optional]  # noqa: E501
            hypervisor_external_address (HciIpAddress): [optional]  # noqa: E501
            hypervisor_number_of_vms (int): The number of VMs managed on this node.. [optional]  # noqa: E501
            hypervisor_state (str): The hypervisor state e.g. ACROPOLIS_NORMAL, ENTERING_MAINTENANCE_MODE, ENTERED_MAINTENANCE_MODE, RESERVED_FOR_HA_FAILOVER, ENTERING_MAINTENANCE_MODE_FROM_HA_FAILOVER, RESERVING_FOR_HA_FAILOVER, HA_FAILOVER_SOURCE, HA_FAILOVER_TARGET, HA_HEALING_SOURCE, HA_HEALING_TARGET.. [optional]  # noqa: E501
            hypervisor_type (str): The hypervisor type, e.g. AHV, ESX, HYPERV, XEN, NATIVEHOST etc.. [optional]  # noqa: E501
            hypervisor_user_name (str): The user name of the hypervisor on this node.. [optional]  # noqa: E501
            hypervisor_version (str): The version of the hypervisor on this node.. [optional]  # noqa: E501
            ipmi_ip (HciIpAddress): [optional]  # noqa: E501
            ipmi_username (str): The IPMI user name of the controller.. [optional]  # noqa: E501
            is_degraded (bool): The degraded status of the node.. [optional]  # noqa: E501
            is_hardware_virtualized (bool): The hardware virtualization status of the node.. [optional]  # noqa: E501
            is_secure_booted (bool): The secure boot status of the node.. [optional]  # noqa: E501
            key_management_device_to_cert_status ([HciKeyManagementDeviceToCertStatusInfo], none_type): [optional]  # noqa: E501
            maintenance_state (str): The maintenance state of the node.. [optional]  # noqa: E501
            memory_capacity_bytes (int): The memory capacity in bytes of the node.. [optional]  # noqa: E501
            memory_size_bytes (int): The memory size in bytes of the node.. [optional]  # noqa: E501
            memory_usage_bytes (int): The memory usage in bytes of the node.. [optional]  # noqa: E501
            node_ext_id (str): The unique identifier of the node.. [optional]  # noqa: E501
            node_status (str): The status of the node such as NORMAL, TO_BE_REMOVED, OK_TO_BE_REMOVED, NEW_NODE, TO_BE_PREPROTECTED, PREPROTECTED.. [optional]  # noqa: E501
            number_of_cpu_cores (int): The number of CPU cores on the node.. [optional]  # noqa: E501
            number_of_cpu_sockets (int): The number of sockets on the node.. [optional]  # noqa: E501
            number_of_cpu_threads (int): The number of threads on the node.. [optional]  # noqa: E501
            reboot_pending (bool): The reboot pending status of the node.. [optional]  # noqa: E501
            storage_capacity_bytes (int): The storage capacity in bytes of the node.. [optional]  # noqa: E501
            storage_usage_bytes (int): The storage usage in bytes of the node.. [optional]  # noqa: E501
            cluster (HciClusterRelationship): [optional]  # noqa: E501
            disks ([HciDiskRelationship], none_type): An array of relationships to hciDisk resources.. [optional]  # noqa: E501
            gpus ([HciGpuRelationship], none_type): An array of relationships to hciGpu resources.. [optional]  # noqa: E501
            physical_server (ComputePhysicalRelationship): [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
        """

        class_id = "hci.Node" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "hci.Node")
        object_type = "hci.Node" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "hci.Node")
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
        """HciNodeAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "hci.Node", must be one of ["hci.Node", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "hci.Node", must be one of ["hci.Node", ]  # noqa: E501
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
            block_model (str): The rackable unit model of the node.. [optional]  # noqa: E501
            block_serial (str): The rackable unit serial number of the node.. [optional]  # noqa: E501
            boot_time_usecs (int): The boot time in microseconds of the node.. [optional]  # noqa: E501
            cluster_ext_id (str): The unique identifier of the cluster.. [optional]  # noqa: E501
            cluster_name (str): The name of the cluster this node belongs to.. [optional]  # noqa: E501
            controller_vm_backplane_address (HciIpAddress): [optional]  # noqa: E501
            controller_vm_external_address (HciIpAddress): [optional]  # noqa: E501
            controller_vm_id (int): The identifier number of the controller VM.. [optional]  # noqa: E501
            controller_vm_maintanence_mode (bool): The maintenance mode status of the controller VM.. [optional]  # noqa: E501
            controller_vm_nat_ip (HciIpAddress): [optional]  # noqa: E501
            controller_vm_nat_port (int): The NAT port of the controller VM.. [optional]  # noqa: E501
            controller_vm_rdma_backplane_address (HciIpAddress): [optional]  # noqa: E501
            controller_vm_server_uuid (str): The Rackable unit UUID of the server.. [optional]  # noqa: E501
            cpu_capacity_hz (int): The CPU capacity in Hz of the node.. [optional]  # noqa: E501
            cpu_frequency_hz (int): The CPU frequency in Hz on the node.. [optional]  # noqa: E501
            cpu_model (str): The CPU model of the node.. [optional]  # noqa: E501
            cpu_usage_hz (int): The CPU usage in Hz of the node.. [optional]  # noqa: E501
            default_vhd_container_uuid (str): The default VHD container UUID of the node.. [optional]  # noqa: E501
            default_vhd_location (str): The default VHD location of the node.. [optional]  # noqa: E501
            default_vm_container_uuid (str): The default VM container UUID of the node.. [optional]  # noqa: E501
            default_vm_location (str): The default VM location of the node.. [optional]  # noqa: E501
            disk_count (int): The number of disks on the node.. [optional]  # noqa: E501
            failover_cluster_fqdn (str): The failover cluster FQDN of the node.. [optional]  # noqa: E501
            failover_cluster_node_status (str): The failover cluster node status of the node.. [optional]  # noqa: E501
            gpu_count (int): The number of GPUs on the node.. [optional]  # noqa: E501
            gpu_driver_version (str): The GPU driver version of the node.. [optional]  # noqa: E501
            has_csr (bool): Certificate signing request status of the node.. [optional]  # noqa: E501
            host_name (str): The name of the host the node is running on.. [optional]  # noqa: E501
            host_type (str): The type of the host, e.g. HYPER_CONVERGED, COMPUTE_ONLY, STORAGE_ONLY.. [optional]  # noqa: E501
            hypervisor_acropolis_connection_state (str): The connection state of the hypervisor, e.g. CONNECTED, DISCONNECTED, NOT_AVAILABLE.. [optional]  # noqa: E501
            hypervisor_external_address (HciIpAddress): [optional]  # noqa: E501
            hypervisor_number_of_vms (int): The number of VMs managed on this node.. [optional]  # noqa: E501
            hypervisor_state (str): The hypervisor state e.g. ACROPOLIS_NORMAL, ENTERING_MAINTENANCE_MODE, ENTERED_MAINTENANCE_MODE, RESERVED_FOR_HA_FAILOVER, ENTERING_MAINTENANCE_MODE_FROM_HA_FAILOVER, RESERVING_FOR_HA_FAILOVER, HA_FAILOVER_SOURCE, HA_FAILOVER_TARGET, HA_HEALING_SOURCE, HA_HEALING_TARGET.. [optional]  # noqa: E501
            hypervisor_type (str): The hypervisor type, e.g. AHV, ESX, HYPERV, XEN, NATIVEHOST etc.. [optional]  # noqa: E501
            hypervisor_user_name (str): The user name of the hypervisor on this node.. [optional]  # noqa: E501
            hypervisor_version (str): The version of the hypervisor on this node.. [optional]  # noqa: E501
            ipmi_ip (HciIpAddress): [optional]  # noqa: E501
            ipmi_username (str): The IPMI user name of the controller.. [optional]  # noqa: E501
            is_degraded (bool): The degraded status of the node.. [optional]  # noqa: E501
            is_hardware_virtualized (bool): The hardware virtualization status of the node.. [optional]  # noqa: E501
            is_secure_booted (bool): The secure boot status of the node.. [optional]  # noqa: E501
            key_management_device_to_cert_status ([HciKeyManagementDeviceToCertStatusInfo], none_type): [optional]  # noqa: E501
            maintenance_state (str): The maintenance state of the node.. [optional]  # noqa: E501
            memory_capacity_bytes (int): The memory capacity in bytes of the node.. [optional]  # noqa: E501
            memory_size_bytes (int): The memory size in bytes of the node.. [optional]  # noqa: E501
            memory_usage_bytes (int): The memory usage in bytes of the node.. [optional]  # noqa: E501
            node_ext_id (str): The unique identifier of the node.. [optional]  # noqa: E501
            node_status (str): The status of the node such as NORMAL, TO_BE_REMOVED, OK_TO_BE_REMOVED, NEW_NODE, TO_BE_PREPROTECTED, PREPROTECTED.. [optional]  # noqa: E501
            number_of_cpu_cores (int): The number of CPU cores on the node.. [optional]  # noqa: E501
            number_of_cpu_sockets (int): The number of sockets on the node.. [optional]  # noqa: E501
            number_of_cpu_threads (int): The number of threads on the node.. [optional]  # noqa: E501
            reboot_pending (bool): The reboot pending status of the node.. [optional]  # noqa: E501
            storage_capacity_bytes (int): The storage capacity in bytes of the node.. [optional]  # noqa: E501
            storage_usage_bytes (int): The storage usage in bytes of the node.. [optional]  # noqa: E501
            cluster (HciClusterRelationship): [optional]  # noqa: E501
            disks ([HciDiskRelationship], none_type): An array of relationships to hciDisk resources.. [optional]  # noqa: E501
            gpus ([HciGpuRelationship], none_type): An array of relationships to hciGpu resources.. [optional]  # noqa: E501
            physical_server (ComputePhysicalRelationship): [optional]  # noqa: E501
            registered_device (AssetDeviceRegistrationRelationship): [optional]  # noqa: E501
        """

        class_id = "hci.Node" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "hci.Node")
        object_type = "hci.Node" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "hci.Node")
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