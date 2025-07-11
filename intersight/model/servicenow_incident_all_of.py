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



class ServicenowIncidentAllOf(ModelNormal):
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
            'SERVICENOW.INCIDENT': "servicenow.Incident",
        },
        ('object_type',): {
            'SERVICENOW.INCIDENT': "servicenow.Incident",
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
        return {
            'class_id': (str,),  # noqa: E501
            'object_type': (str,),  # noqa: E501
            'approval': (str,),  # noqa: E501
            'category': (str,),  # noqa: E501
            'comments': (str,),  # noqa: E501
            'created_by': (str,),  # noqa: E501
            'created_on': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'due_date': (str,),  # noqa: E501
            'expected_start': (str,),  # noqa: E501
            'impact': (str,),  # noqa: E501
            'incident_state': (str,),  # noqa: E501
            'opened_by': (str,),  # noqa: E501
            'priority': (str,),  # noqa: E501
            'risk': (str,),  # noqa: E501
            'severity': (str,),  # noqa: E501
            'short_description': (str,),  # noqa: E501
            'sys_id': (str,),  # noqa: E501
            'task_effective_number': (str,),  # noqa: E501
            'updated_by': (str,),  # noqa: E501
            'urgency': (str,),  # noqa: E501
            'work_end': (str,),  # noqa: E501
            'work_start': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'approval': 'Approval',  # noqa: E501
        'category': 'Category',  # noqa: E501
        'comments': 'Comments',  # noqa: E501
        'created_by': 'CreatedBy',  # noqa: E501
        'created_on': 'CreatedOn',  # noqa: E501
        'description': 'Description',  # noqa: E501
        'due_date': 'DueDate',  # noqa: E501
        'expected_start': 'ExpectedStart',  # noqa: E501
        'impact': 'Impact',  # noqa: E501
        'incident_state': 'IncidentState',  # noqa: E501
        'opened_by': 'OpenedBy',  # noqa: E501
        'priority': 'Priority',  # noqa: E501
        'risk': 'Risk',  # noqa: E501
        'severity': 'Severity',  # noqa: E501
        'short_description': 'ShortDescription',  # noqa: E501
        'sys_id': 'SysId',  # noqa: E501
        'task_effective_number': 'TaskEffectiveNumber',  # noqa: E501
        'updated_by': 'UpdatedBy',  # noqa: E501
        'urgency': 'Urgency',  # noqa: E501
        'work_end': 'WorkEnd',  # noqa: E501
        'work_start': 'WorkStart',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ServicenowIncidentAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "servicenow.Incident", must be one of ["servicenow.Incident", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "servicenow.Incident", must be one of ["servicenow.Incident", ]  # noqa: E501
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
            approval (str): The approver property of Incident.. [optional]  # noqa: E501
            category (str): Category property for Incident.. [optional]  # noqa: E501
            comments (str): Comments property on Incident.. [optional]  # noqa: E501
            created_by (str): Creator property of Incident.. [optional]  # noqa: E501
            created_on (str): Incident create date property.. [optional]  # noqa: E501
            description (str): Description for Incident.. [optional]  # noqa: E501
            due_date (str): Due date property for Incident.. [optional]  # noqa: E501
            expected_start (str): Expected start date for Incident.. [optional]  # noqa: E501
            impact (str): Impact property for Incident.. [optional]  # noqa: E501
            incident_state (str): State property of the Incident.. [optional]  # noqa: E501
            opened_by (str): Assigned to value for Incident.. [optional]  # noqa: E501
            priority (str): Priority property for Incident.. [optional]  # noqa: E501
            risk (str): The risk property for Incident.. [optional]  # noqa: E501
            severity (str): Severity property of the Incident.. [optional]  # noqa: E501
            short_description (str): Short Description for Incident.. [optional]  # noqa: E501
            sys_id (str): System Id property for Incident.. [optional]  # noqa: E501
            task_effective_number (str): Task Effective Number for Incident.. [optional]  # noqa: E501
            updated_by (str): Last update by on Incident.. [optional]  # noqa: E501
            urgency (str): Urgency property of the Incident.. [optional]  # noqa: E501
            work_end (str): Work end date for Incident.. [optional]  # noqa: E501
            work_start (str): Work start date for Incident.. [optional]  # noqa: E501
        """

        class_id = "servicenow.Incident" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "servicenow.Incident")
        object_type = "servicenow.Incident" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "servicenow.Incident")
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
        """ServicenowIncidentAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "servicenow.Incident", must be one of ["servicenow.Incident", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "servicenow.Incident", must be one of ["servicenow.Incident", ]  # noqa: E501
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
            approval (str): The approver property of Incident.. [optional]  # noqa: E501
            category (str): Category property for Incident.. [optional]  # noqa: E501
            comments (str): Comments property on Incident.. [optional]  # noqa: E501
            created_by (str): Creator property of Incident.. [optional]  # noqa: E501
            created_on (str): Incident create date property.. [optional]  # noqa: E501
            description (str): Description for Incident.. [optional]  # noqa: E501
            due_date (str): Due date property for Incident.. [optional]  # noqa: E501
            expected_start (str): Expected start date for Incident.. [optional]  # noqa: E501
            impact (str): Impact property for Incident.. [optional]  # noqa: E501
            incident_state (str): State property of the Incident.. [optional]  # noqa: E501
            opened_by (str): Assigned to value for Incident.. [optional]  # noqa: E501
            priority (str): Priority property for Incident.. [optional]  # noqa: E501
            risk (str): The risk property for Incident.. [optional]  # noqa: E501
            severity (str): Severity property of the Incident.. [optional]  # noqa: E501
            short_description (str): Short Description for Incident.. [optional]  # noqa: E501
            sys_id (str): System Id property for Incident.. [optional]  # noqa: E501
            task_effective_number (str): Task Effective Number for Incident.. [optional]  # noqa: E501
            updated_by (str): Last update by on Incident.. [optional]  # noqa: E501
            urgency (str): Urgency property of the Incident.. [optional]  # noqa: E501
            work_end (str): Work end date for Incident.. [optional]  # noqa: E501
            work_start (str): Work start date for Incident.. [optional]  # noqa: E501
        """

        class_id = "servicenow.Incident" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "servicenow.Incident")
        object_type = "servicenow.Incident" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "servicenow.Incident")
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
