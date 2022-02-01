# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class User(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'UserId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'email': 'str',
        'name': 'str',
        'authority': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'email': 'email',
        'name': 'name',
        'authority': 'authority',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, customer_id=None, email=None, name=None, authority=None, first_name=None, last_name=None, additional_info=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._email = None
        self._name = None
        self._authority = None
        self._first_name = None
        self._last_name = None
        self._additional_info = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        self.email = email
        if name is not None:
            self.name = name
        self.authority = authority
        self.first_name = first_name
        self.last_name = last_name
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: UserId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: UserId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this User.  # noqa: E501

        Timestamp of the user creation, in milliseconds  # noqa: E501

        :return: The created_time of this User.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this User.

        Timestamp of the user creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this User.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this User.  # noqa: E501


        :return: The tenant_id of this User.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this User.


        :param tenant_id: The tenant_id of this User.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this User.  # noqa: E501


        :return: The customer_id of this User.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this User.


        :param customer_id: The customer_id of this User.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        Email of the user  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        Email of the user  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501

        Duplicates the email of the user, readonly  # noqa: E501

        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

        Duplicates the email of the user, readonly  # noqa: E501

        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def authority(self):
        """Gets the authority of this User.  # noqa: E501

        Authority  # noqa: E501

        :return: The authority of this User.  # noqa: E501
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this User.

        Authority  # noqa: E501

        :param authority: The authority of this User.  # noqa: E501
        :type: str
        """
        if authority is None:
            raise ValueError("Invalid value for `authority`, must not be `None`")  # noqa: E501
        allowed_values = ["CUSTOMER_USER", "REFRESH_TOKEN", "SYS_ADMIN", "TENANT_ADMIN"]  # noqa: E501
        if authority not in allowed_values:
            raise ValueError(
                "Invalid value for `authority` ({0}), must be one of {1}"  # noqa: E501
                .format(authority, allowed_values)
            )

        self._authority = authority

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        First name of the user  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        First name of the user  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        Last name of the user  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        Last name of the user  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def additional_info(self):
        """Gets the additional_info of this User.  # noqa: E501


        :return: The additional_info of this User.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this User.


        :param additional_info: The additional_info of this User.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(User, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
