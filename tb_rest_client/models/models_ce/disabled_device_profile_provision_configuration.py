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
from tb_rest_client.models.models_ce.device_profile_provision_configuration import DeviceProfileProvisionConfiguration  # noqa: F401,E501

class DisabledDeviceProfileProvisionConfiguration(DeviceProfileProvisionConfiguration):
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
        'provision_device_secret': 'str'
    }
    if hasattr(DeviceProfileProvisionConfiguration, "swagger_types"):
        swagger_types.update(DeviceProfileProvisionConfiguration.swagger_types)

    attribute_map = {
        'provision_device_secret': 'provisionDeviceSecret'
    }
    if hasattr(DeviceProfileProvisionConfiguration, "attribute_map"):
        attribute_map.update(DeviceProfileProvisionConfiguration.attribute_map)

    def __init__(self, provision_device_secret=None, *args, **kwargs):  # noqa: E501
        """DisabledDeviceProfileProvisionConfiguration - a model defined in Swagger"""  # noqa: E501
        self._provision_device_secret = None
        self.discriminator = None
        if provision_device_secret is not None:
            self.provision_device_secret = provision_device_secret
        DeviceProfileProvisionConfiguration.__init__(self, *args, **kwargs)

    @property
    def provision_device_secret(self):
        """Gets the provision_device_secret of this DisabledDeviceProfileProvisionConfiguration.  # noqa: E501


        :return: The provision_device_secret of this DisabledDeviceProfileProvisionConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._provision_device_secret

    @provision_device_secret.setter
    def provision_device_secret(self, provision_device_secret):
        """Sets the provision_device_secret of this DisabledDeviceProfileProvisionConfiguration.


        :param provision_device_secret: The provision_device_secret of this DisabledDeviceProfileProvisionConfiguration.  # noqa: E501
        :type: str
        """

        self._provision_device_secret = provision_device_secret

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
        if issubclass(DisabledDeviceProfileProvisionConfiguration, dict):
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
        if not isinstance(other, DisabledDeviceProfileProvisionConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
