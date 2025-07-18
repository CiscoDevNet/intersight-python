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
    from intersight.model.iam_api_key_relationship import IamApiKeyRelationship
    from intersight.model.iam_app_registration_relationship import IamAppRegistrationRelationship
    from intersight.model.iam_idp_reference_relationship import IamIdpReferenceRelationship
    from intersight.model.iam_idp_relationship import IamIdpRelationship
    from intersight.model.iam_local_user_password_relationship import IamLocalUserPasswordRelationship
    from intersight.model.iam_o_auth_token_relationship import IamOAuthTokenRelationship
    from intersight.model.iam_permission_relationship import IamPermissionRelationship
    from intersight.model.iam_session_relationship import IamSessionRelationship
    globals()['IamApiKeyRelationship'] = IamApiKeyRelationship
    globals()['IamAppRegistrationRelationship'] = IamAppRegistrationRelationship
    globals()['IamIdpReferenceRelationship'] = IamIdpReferenceRelationship
    globals()['IamIdpRelationship'] = IamIdpRelationship
    globals()['IamLocalUserPasswordRelationship'] = IamLocalUserPasswordRelationship
    globals()['IamOAuthTokenRelationship'] = IamOAuthTokenRelationship
    globals()['IamPermissionRelationship'] = IamPermissionRelationship
    globals()['IamSessionRelationship'] = IamSessionRelationship


class IamUserAllOf(ModelNormal):
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
            'IAM.USER': "iam.User",
        },
        ('object_type',): {
            'IAM.USER': "iam.User",
        },
    }

    validations = {
        ('email',): {
            'regex': {
                'pattern': r'^$|^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$',  # noqa: E501
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
            'client_ip_address': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_login_time': (datetime,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'last_role_modified_time': (datetime,),  # noqa: E501
            'locked_until': (datetime,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'user_id_or_email': (str,),  # noqa: E501
            'user_type': (str,),  # noqa: E501
            'user_unique_identifier': (str,),  # noqa: E501
            'api_keys': ([IamApiKeyRelationship], none_type,),  # noqa: E501
            'app_registrations': ([IamAppRegistrationRelationship], none_type,),  # noqa: E501
            'idp': (IamIdpRelationship,),  # noqa: E501
            'idpreference': (IamIdpReferenceRelationship,),  # noqa: E501
            'local_user_password': (IamLocalUserPasswordRelationship,),  # noqa: E501
            'oauth_tokens': ([IamOAuthTokenRelationship], none_type,),  # noqa: E501
            'permissions': ([IamPermissionRelationship], none_type,),  # noqa: E501
            'sessions': ([IamSessionRelationship], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_id': 'ClassId',  # noqa: E501
        'object_type': 'ObjectType',  # noqa: E501
        'client_ip_address': 'ClientIpAddress',  # noqa: E501
        'email': 'Email',  # noqa: E501
        'first_name': 'FirstName',  # noqa: E501
        'last_login_time': 'LastLoginTime',  # noqa: E501
        'last_name': 'LastName',  # noqa: E501
        'last_role_modified_time': 'LastRoleModifiedTime',  # noqa: E501
        'locked_until': 'LockedUntil',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'user_id_or_email': 'UserIdOrEmail',  # noqa: E501
        'user_type': 'UserType',  # noqa: E501
        'user_unique_identifier': 'UserUniqueIdentifier',  # noqa: E501
        'api_keys': 'ApiKeys',  # noqa: E501
        'app_registrations': 'AppRegistrations',  # noqa: E501
        'idp': 'Idp',  # noqa: E501
        'idpreference': 'Idpreference',  # noqa: E501
        'local_user_password': 'LocalUserPassword',  # noqa: E501
        'oauth_tokens': 'OauthTokens',  # noqa: E501
        'permissions': 'Permissions',  # noqa: E501
        'sessions': 'Sessions',  # noqa: E501
    }

    read_only_vars = {
        'client_ip_address',  # noqa: E501
        'last_login_time',  # noqa: E501
        'last_role_modified_time',  # noqa: E501
        'locked_until',  # noqa: E501
        'name',  # noqa: E501
        'user_type',  # noqa: E501
        'user_unique_identifier',  # noqa: E501
        'api_keys',  # noqa: E501
        'app_registrations',  # noqa: E501
        'oauth_tokens',  # noqa: E501
        'sessions',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IamUserAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "iam.User", must be one of ["iam.User", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "iam.User", must be one of ["iam.User", ]  # noqa: E501
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
            client_ip_address (str): IP address from which the user last logged in to Intersight.. [optional]  # noqa: E501
            email (str): Email of the user. Remote users are added to Intersight using the email configured in the IdP.. [optional]  # noqa: E501
            first_name (str): First name of the user. For remote users, this field is populated from the IdP attributes received after authentication.. [optional]  # noqa: E501
            last_login_time (datetime): Last successful login time for user.. [optional]  # noqa: E501
            last_name (str): Last name of the user. For remote users, this field is populated from the IdP attributes received after authentication.. [optional]  # noqa: E501
            last_role_modified_time (datetime): Last role modification time for user.. [optional]  # noqa: E501
            locked_until (datetime): Time until which the user account will be locked out.. [optional]  # noqa: E501
            name (str): Name of the user. For remote users, it is the value as configured in the IdP.. [optional]  # noqa: E501
            user_id_or_email (str): UserID or email of the user. For remote users, it is the value as configured in the IDP.. [optional]  # noqa: E501
            user_type (str): Type of the User. If a user is added manually by specifying the email address, or has logged in using groups, based on the IdP attributes received during authentication. If added manually, the user type will be static, otherwise dynamic.. [optional]  # noqa: E501
            user_unique_identifier (str): Unique id of the user used by the identity provider to store the user.. [optional]  # noqa: E501
            api_keys ([IamApiKeyRelationship], none_type): An array of relationships to iamApiKey resources.. [optional]  # noqa: E501
            app_registrations ([IamAppRegistrationRelationship], none_type): An array of relationships to iamAppRegistration resources.. [optional]  # noqa: E501
            idp (IamIdpRelationship): [optional]  # noqa: E501
            idpreference (IamIdpReferenceRelationship): [optional]  # noqa: E501
            local_user_password (IamLocalUserPasswordRelationship): [optional]  # noqa: E501
            oauth_tokens ([IamOAuthTokenRelationship], none_type): An array of relationships to iamOAuthToken resources.. [optional]  # noqa: E501
            permissions ([IamPermissionRelationship], none_type): An array of relationships to iamPermission resources.. [optional]  # noqa: E501
            sessions ([IamSessionRelationship], none_type): An array of relationships to iamSession resources.. [optional]  # noqa: E501
        """

        class_id = "iam.User" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "iam.User")
        object_type = "iam.User" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "iam.User")
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
        """IamUserAllOf - a model defined in OpenAPI

        Args:

        Keyword Args:
            class_id (str): The fully-qualified name of the instantiated, concrete type. This property is used as a discriminator to identify the type of the payload when marshaling and unmarshaling data.. defaults to "iam.User", must be one of ["iam.User", ]  # noqa: E501
            object_type (str): The fully-qualified name of the instantiated, concrete type. The value should be the same as the 'ClassId' property.. defaults to "iam.User", must be one of ["iam.User", ]  # noqa: E501
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
            client_ip_address (str): IP address from which the user last logged in to Intersight.. [optional]  # noqa: E501
            email (str): Email of the user. Remote users are added to Intersight using the email configured in the IdP.. [optional]  # noqa: E501
            first_name (str): First name of the user. For remote users, this field is populated from the IdP attributes received after authentication.. [optional]  # noqa: E501
            last_login_time (datetime): Last successful login time for user.. [optional]  # noqa: E501
            last_name (str): Last name of the user. For remote users, this field is populated from the IdP attributes received after authentication.. [optional]  # noqa: E501
            last_role_modified_time (datetime): Last role modification time for user.. [optional]  # noqa: E501
            locked_until (datetime): Time until which the user account will be locked out.. [optional]  # noqa: E501
            name (str): Name of the user. For remote users, it is the value as configured in the IdP.. [optional]  # noqa: E501
            user_id_or_email (str): UserID or email of the user. For remote users, it is the value as configured in the IDP.. [optional]  # noqa: E501
            user_type (str): Type of the User. If a user is added manually by specifying the email address, or has logged in using groups, based on the IdP attributes received during authentication. If added manually, the user type will be static, otherwise dynamic.. [optional]  # noqa: E501
            user_unique_identifier (str): Unique id of the user used by the identity provider to store the user.. [optional]  # noqa: E501
            api_keys ([IamApiKeyRelationship], none_type): An array of relationships to iamApiKey resources.. [optional]  # noqa: E501
            app_registrations ([IamAppRegistrationRelationship], none_type): An array of relationships to iamAppRegistration resources.. [optional]  # noqa: E501
            idp (IamIdpRelationship): [optional]  # noqa: E501
            idpreference (IamIdpReferenceRelationship): [optional]  # noqa: E501
            local_user_password (IamLocalUserPasswordRelationship): [optional]  # noqa: E501
            oauth_tokens ([IamOAuthTokenRelationship], none_type): An array of relationships to iamOAuthToken resources.. [optional]  # noqa: E501
            permissions ([IamPermissionRelationship], none_type): An array of relationships to iamPermission resources.. [optional]  # noqa: E501
            sessions ([IamSessionRelationship], none_type): An array of relationships to iamSession resources.. [optional]  # noqa: E501
        """

        class_id = "iam.User" if len(kwargs.get('class_id','').strip()) == 0 else kwargs.get('class_id', "iam.User")
        object_type = "iam.User" if len(kwargs.get('object_type','').strip()) == 0 else kwargs.get('object_type', "iam.User")
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
