# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.2PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2024. ThingsBoard
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

class EventInfo(object):
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
        'id': 'EventId',
        'tenant_id': 'TenantId',
        'type': 'str',
        'uid': 'str',
        'entity_id': 'EntityId',
        'body': 'JsonNode',
        'created_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenantId',
        'type': 'type',
        'uid': 'uid',
        'entity_id': 'entityId',
        'body': 'body',
        'created_time': 'createdTime'
    }

    def __init__(self, id=None, tenant_id=None, type=None, uid=None, entity_id=None, body=None, created_time=None):  # noqa: E501
        """EventInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._tenant_id = None
        self._type = None
        self._uid = None
        self._entity_id = None
        self._body = None
        self._created_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid
        if entity_id is not None:
            self.entity_id = entity_id
        if body is not None:
            self.body = body
        if created_time is not None:
            self.created_time = created_time

    @property
    def id(self):
        """Gets the id of this EventInfo.  # noqa: E501


        :return: The id of this EventInfo.  # noqa: E501
        :rtype: EventId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventInfo.


        :param id: The id of this EventInfo.  # noqa: E501
        :type: EventId
        """

        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EventInfo.  # noqa: E501


        :return: The tenant_id of this EventInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EventInfo.


        :param tenant_id: The tenant_id of this EventInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this EventInfo.  # noqa: E501

        Event type  # noqa: E501

        :return: The type of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventInfo.

        Event type  # noqa: E501

        :param type: The type of this EventInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this EventInfo.  # noqa: E501

        string  # noqa: E501

        :return: The uid of this EventInfo.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this EventInfo.

        string  # noqa: E501

        :param uid: The uid of this EventInfo.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def entity_id(self):
        """Gets the entity_id of this EventInfo.  # noqa: E501


        :return: The entity_id of this EventInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EventInfo.


        :param entity_id: The entity_id of this EventInfo.  # noqa: E501
        :type: EntityId
        """

        self._entity_id = entity_id

    @property
    def body(self):
        """Gets the body of this EventInfo.  # noqa: E501


        :return: The body of this EventInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EventInfo.


        :param body: The body of this EventInfo.  # noqa: E501
        :type: JsonNode
        """

        self._body = body

    @property
    def created_time(self):
        """Gets the created_time of this EventInfo.  # noqa: E501

        Timestamp of the event creation, in milliseconds  # noqa: E501

        :return: The created_time of this EventInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EventInfo.

        Timestamp of the event creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this EventInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

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
        if issubclass(EventInfo, dict):
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
        if not isinstance(other, EventInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
