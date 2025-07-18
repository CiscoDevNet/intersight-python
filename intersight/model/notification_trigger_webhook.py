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
    from intersight.model.notification_action import NotificationAction
    from intersight.model.notification_trigger_webhook_all_of import NotificationTriggerWebhookAllOf
    globals()['NotificationAction'] = NotificationAction
    globals()['NotificationTriggerWebhookAllOf'] = NotificationTriggerWebhookAllOf


class NotificationTriggerWebhook(ModelComposed):
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
            'NOTIFICATION.TRIGGERWEBHOOK': "notification.TriggerWebhook",
        },
        ('object_type',): {
            'NOTIFICATION.TRIGGERWEBHOOK': "notification.TriggerWebhook",
        },
        ('state',): {
            'INACTIVE': "Inactive",
            'ACTIVE': "Active",
        },
    }

    validations = {
        ('url',): {
            'regex': {
                'pattern': r'^https:\/\/[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:\/?#[\]@!\$&\'\(\)\*\+,;=.]+$',  # noqa: E501
            },
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
            'first_failed_request': (datetime,),  # noqa: E501
            'is_secret_set': (bool,),  # noqa: E501
            'last_network_error': (str,),  # noqa: E501
            'last_response_code': (int,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'url': (str,),  # noqa: E501
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
        'first_failed_request': 'FirstFailedRequest',  # noqa: E501
        'is_secret_set': 'IsSecretSet',  # noqa: E501
        'last_network_error': 'LastNetworkError',  # noqa: E501
        'last_response_code': 'LastResponseCode',  # noqa: E501
        'secret': 'Secret',  # noqa: E501
        'state': 'State',  # noqa: E501
        'url': 'Url',  # noqa: E501
    }

    read_only_vars = {
        'first_failed_request',  # noqa: E501
        'is_secret_set',  # noqa: E501
        'last_network_error',  # noqa: E501
        'last_response_code',  # noqa: E501
        'state',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """NotificationTriggerWebhook - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "notification.TriggerWebhook", must be one of ["notification.TriggerWebhook", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "notification.TriggerWebhook", must be one of ["notification.TriggerWebhook", ]  # noqa: E501
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
            first_failed_request (datetime): Holds the timestamp of the first failed request. The first time the notification is not delivered to the webhook server, the user will have the Warning alarm in the system. Next 48 hours the system still will try to notify the webhook server. If after 48 hours the server is not recovered, the system will mark this webhook as Inactive, and the user will have a critical alarm in the system.. [optional]  # noqa: E501
            is_secret_set (bool): Indicates whether the value of the 'secret' property has been set.. [optional] if omitted the server will use the default value of False  # noqa: E501
            last_network_error (str): Holds the error message for the user of the last response.. [optional]  # noqa: E501
            last_response_code (int): Holds the code of the last response, which helps to debug the issue in case if webhook server is not reachable.. [optional]  # noqa: E501
            secret (str): The secret is used to build the Authorization header, which will be attached to each webhook notification. By this header developers of the webhooks servers can make sure that events are received from the trusted source - Intersight.. [optional]  # noqa: E501
            state (str): State of the action shows whether this action passes the verification or not. If this property holds 'Inactive' value, this action will not be executed. To verify action again, use the Verify property from the MO. * `Inactive` - Inactive state means action didn't pass the verification and it won't be executed. * `Active` - Active state means that action successfully passed the verification and it is ready to be performed.. [optional] if omitted the server will use the default value of "Inactive"  # noqa: E501
            url (str): Payload URL of the recipient app, which is intended to serve the events that happens in Intersight.. [optional]  # noqa: E501
        """

        class_id = "notification.TriggerWebhook" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "notification.TriggerWebhook")
        object_type = "notification.TriggerWebhook" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "notification.TriggerWebhook")
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
        """NotificationTriggerWebhook - a model defined in OpenAPI

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "notification.TriggerWebhook", must be one of ["notification.TriggerWebhook", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "notification.TriggerWebhook", must be one of ["notification.TriggerWebhook", ]  # noqa: E501
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
            first_failed_request (datetime): Holds the timestamp of the first failed request. The first time the notification is not delivered to the webhook server, the user will have the Warning alarm in the system. Next 48 hours the system still will try to notify the webhook server. If after 48 hours the server is not recovered, the system will mark this webhook as Inactive, and the user will have a critical alarm in the system.. [optional]  # noqa: E501
            is_secret_set (bool): Indicates whether the value of the 'secret' property has been set.. [optional] if omitted the server will use the default value of False  # noqa: E501
            last_network_error (str): Holds the error message for the user of the last response.. [optional]  # noqa: E501
            last_response_code (int): Holds the code of the last response, which helps to debug the issue in case if webhook server is not reachable.. [optional]  # noqa: E501
            secret (str): The secret is used to build the Authorization header, which will be attached to each webhook notification. By this header developers of the webhooks servers can make sure that events are received from the trusted source - Intersight.. [optional]  # noqa: E501
            state (str): State of the action shows whether this action passes the verification or not. If this property holds 'Inactive' value, this action will not be executed. To verify action again, use the Verify property from the MO. * `Inactive` - Inactive state means action didn't pass the verification and it won't be executed. * `Active` - Active state means that action successfully passed the verification and it is ready to be performed.. [optional] if omitted the server will use the default value of "Inactive"  # noqa: E501
            url (str): Payload URL of the recipient app, which is intended to serve the events that happens in Intersight.. [optional]  # noqa: E501
        """

        class_id = "notification.TriggerWebhook" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "notification.TriggerWebhook")
        object_type = "notification.TriggerWebhook" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "notification.TriggerWebhook")
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
              NotificationAction,
              NotificationTriggerWebhookAllOf,
          ],
          'oneOf': [
          ],
        }
