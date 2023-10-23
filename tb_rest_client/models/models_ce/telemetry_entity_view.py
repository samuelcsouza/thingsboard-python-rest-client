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

class TelemetryEntityView(object):
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
        'timeseries': 'list[str]',
        'attributes': 'AttributesEntityView'
    }

    attribute_map = {
        'timeseries': 'timeseries',
        'attributes': 'attributes'
    }

    def __init__(self, timeseries=None, attributes=None):  # noqa: E501
        """TelemetryEntityView - a model defined in Swagger"""  # noqa: E501
        self._timeseries = None
        self._attributes = None
        self.discriminator = None
        self.timeseries = timeseries
        self.attributes = attributes

    @property
    def timeseries(self):
        """Gets the timeseries of this TelemetryEntityView.  # noqa: E501

        List of time-series data keys to expose  # noqa: E501

        :return: The timeseries of this TelemetryEntityView.  # noqa: E501
        :rtype: list[str]
        """
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries):
        """Sets the timeseries of this TelemetryEntityView.

        List of time-series data keys to expose  # noqa: E501

        :param timeseries: The timeseries of this TelemetryEntityView.  # noqa: E501
        :type: list[str]
        """
        if timeseries is None:
            raise ValueError("Invalid value for `timeseries`, must not be `None`")  # noqa: E501

        self._timeseries = timeseries

    @property
    def attributes(self):
        """Gets the attributes of this TelemetryEntityView.  # noqa: E501


        :return: The attributes of this TelemetryEntityView.  # noqa: E501
        :rtype: AttributesEntityView
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TelemetryEntityView.


        :param attributes: The attributes of this TelemetryEntityView.  # noqa: E501
        :type: AttributesEntityView
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

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
        if issubclass(TelemetryEntityView, dict):
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
        if not isinstance(other, TelemetryEntityView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
