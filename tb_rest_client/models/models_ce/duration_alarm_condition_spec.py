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
from tb_rest_client.models.models_ce.alarm_condition_spec import AlarmConditionSpec  # noqa: F401,E501

class DurationAlarmConditionSpec(AlarmConditionSpec):
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
        'predicate': 'FilterPredicateValuelong',
        'unit': 'str'
    }
    if hasattr(AlarmConditionSpec, "swagger_types"):
        swagger_types.update(AlarmConditionSpec.swagger_types)

    attribute_map = {
        'predicate': 'predicate',
        'unit': 'unit'
    }
    if hasattr(AlarmConditionSpec, "attribute_map"):
        attribute_map.update(AlarmConditionSpec.attribute_map)

    def __init__(self, predicate=None, unit=None, *args, **kwargs):  # noqa: E501
        """DurationAlarmConditionSpec - a model defined in Swagger"""  # noqa: E501
        self._predicate = None
        self._unit = None
        self.discriminator = None
        if predicate is not None:
            self.predicate = predicate
        if unit is not None:
            self.unit = unit
        AlarmConditionSpec.__init__(self, *args, **kwargs)

    @property
    def predicate(self):
        """Gets the predicate of this DurationAlarmConditionSpec.  # noqa: E501


        :return: The predicate of this DurationAlarmConditionSpec.  # noqa: E501
        :rtype: FilterPredicateValuelong
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this DurationAlarmConditionSpec.


        :param predicate: The predicate of this DurationAlarmConditionSpec.  # noqa: E501
        :type: FilterPredicateValuelong
        """

        self._predicate = predicate

    @property
    def unit(self):
        """Gets the unit of this DurationAlarmConditionSpec.  # noqa: E501


        :return: The unit of this DurationAlarmConditionSpec.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DurationAlarmConditionSpec.


        :param unit: The unit of this DurationAlarmConditionSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAYS", "HOURS", "MICROSECONDS", "MILLISECONDS", "MINUTES", "NANOSECONDS", "SECONDS"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

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
        if issubclass(DurationAlarmConditionSpec, dict):
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
        if not isinstance(other, DurationAlarmConditionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
