# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2023. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pprint
import re  # noqa: F401

import six

class WidgetType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'WidgetTypeId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'fqn': 'str',
        'name': 'str',
        'deprecated': 'bool',
        'descriptor': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'fqn': 'fqn',
        'name': 'name',
        'deprecated': 'deprecated',
        'descriptor': 'descriptor'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, fqn=None, name=None, deprecated=None, descriptor=None):  # noqa: E501
        """WidgetType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._fqn = None
        self._name = None
        self._deprecated = None
        self._descriptor = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if fqn is not None:
            self.fqn = fqn
        if name is not None:
            self.name = name
        if deprecated is not None:
            self.deprecated = deprecated
        if descriptor is not None:
            self.descriptor = descriptor

    @property
    def id(self):
        """Gets the id of this WidgetType.  # noqa: E501


        :return: The id of this WidgetType.  # noqa: E501
        :rtype: WidgetTypeId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WidgetType.


        :param id: The id of this WidgetType.  # noqa: E501
        :type: WidgetTypeId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this WidgetType.  # noqa: E501

        Timestamp of the Widget Type creation, in milliseconds  # noqa: E501

        :return: The created_time of this WidgetType.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this WidgetType.

        Timestamp of the Widget Type creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this WidgetType.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this WidgetType.  # noqa: E501


        :return: The tenant_id of this WidgetType.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this WidgetType.


        :param tenant_id: The tenant_id of this WidgetType.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def fqn(self):
        """Gets the fqn of this WidgetType.  # noqa: E501

        Unique FQN that is used in dashboards as a reference widget type  # noqa: E501

        :return: The fqn of this WidgetType.  # noqa: E501
        :rtype: str
        """
        return self._fqn

    @fqn.setter
    def fqn(self, fqn):
        """Sets the fqn of this WidgetType.

        Unique FQN that is used in dashboards as a reference widget type  # noqa: E501

        :param fqn: The fqn of this WidgetType.  # noqa: E501
        :type: str
        """

        self._fqn = fqn

    @property
    def name(self):
        """Gets the name of this WidgetType.  # noqa: E501

        Widget name used in search and UI  # noqa: E501

        :return: The name of this WidgetType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WidgetType.

        Widget name used in search and UI  # noqa: E501

        :param name: The name of this WidgetType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def deprecated(self):
        """Gets the deprecated of this WidgetType.  # noqa: E501

        Whether widget type is deprecated.  # noqa: E501

        :return: The deprecated of this WidgetType.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this WidgetType.

        Whether widget type is deprecated.  # noqa: E501

        :param deprecated: The deprecated of this WidgetType.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def descriptor(self):
        """Gets the descriptor of this WidgetType.  # noqa: E501


        :return: The descriptor of this WidgetType.  # noqa: E501
        :rtype: JsonNode
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor):
        """Sets the descriptor of this WidgetType.


        :param descriptor: The descriptor of this WidgetType.  # noqa: E501
        :type: JsonNode
        """

        self._descriptor = descriptor

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
        if issubclass(WidgetType, dict):
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
        if not isinstance(other, WidgetType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
