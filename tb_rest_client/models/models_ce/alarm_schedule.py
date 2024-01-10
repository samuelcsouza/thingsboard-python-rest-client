# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.2
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

class AlarmSchedule(object):
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
        'dynamic_value': 'DynamicValuestring',
        'type': 'str'
    }

    attribute_map = {
        'dynamic_value': 'dynamicValue',
        'type': 'type'
    }

    def __init__(self, dynamic_value=None, type=None):  # noqa: E501
        """AlarmSchedule - a model defined in Swagger"""  # noqa: E501
        self._dynamic_value = None
        self._type = None
        self.discriminator = None
        if dynamic_value is not None:
            self.dynamic_value = dynamic_value
        if type is not None:
            self.type = type

    @property
    def dynamic_value(self):
        """Gets the dynamic_value of this AlarmSchedule.  # noqa: E501


        :return: The dynamic_value of this AlarmSchedule.  # noqa: E501
        :rtype: DynamicValuestring
        """
        return self._dynamic_value

    @dynamic_value.setter
    def dynamic_value(self, dynamic_value):
        """Sets the dynamic_value of this AlarmSchedule.


        :param dynamic_value: The dynamic_value of this AlarmSchedule.  # noqa: E501
        :type: DynamicValuestring
        """

        self._dynamic_value = dynamic_value

    @property
    def type(self):
        """Gets the type of this AlarmSchedule.  # noqa: E501


        :return: The type of this AlarmSchedule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlarmSchedule.


        :param type: The type of this AlarmSchedule.  # noqa: E501
        :type: str
        """
        allowed_values = ["ANY_TIME", "CUSTOM", "SPECIFIC_TIME"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(AlarmSchedule, dict):
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
        if not isinstance(other, AlarmSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
