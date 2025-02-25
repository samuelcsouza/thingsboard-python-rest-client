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

class BackupCodeTwoFaAccountConfig(object):
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
        'codes': 'list[str]',
        'codes_left': 'int',
        'use_by_default': 'bool'
    }

    attribute_map = {
        'codes': 'codes',
        'codes_left': 'codesLeft',
        'use_by_default': 'useByDefault'
    }

    def __init__(self, codes=None, codes_left=None, use_by_default=None):  # noqa: E501
        """BackupCodeTwoFaAccountConfig - a model defined in Swagger"""  # noqa: E501
        self._codes = None
        self._codes_left = None
        self._use_by_default = None
        self.discriminator = None
        if codes is not None:
            self.codes = codes
        if codes_left is not None:
            self.codes_left = codes_left
        if use_by_default is not None:
            self.use_by_default = use_by_default

    @property
    def codes(self):
        """Gets the codes of this BackupCodeTwoFaAccountConfig.  # noqa: E501


        :return: The codes of this BackupCodeTwoFaAccountConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this BackupCodeTwoFaAccountConfig.


        :param codes: The codes of this BackupCodeTwoFaAccountConfig.  # noqa: E501
        :type: list[str]
        """

        self._codes = codes

    @property
    def codes_left(self):
        """Gets the codes_left of this BackupCodeTwoFaAccountConfig.  # noqa: E501


        :return: The codes_left of this BackupCodeTwoFaAccountConfig.  # noqa: E501
        :rtype: int
        """
        return self._codes_left

    @codes_left.setter
    def codes_left(self, codes_left):
        """Sets the codes_left of this BackupCodeTwoFaAccountConfig.


        :param codes_left: The codes_left of this BackupCodeTwoFaAccountConfig.  # noqa: E501
        :type: int
        """

        self._codes_left = codes_left

    @property
    def use_by_default(self):
        """Gets the use_by_default of this BackupCodeTwoFaAccountConfig.  # noqa: E501


        :return: The use_by_default of this BackupCodeTwoFaAccountConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_by_default

    @use_by_default.setter
    def use_by_default(self, use_by_default):
        """Sets the use_by_default of this BackupCodeTwoFaAccountConfig.


        :param use_by_default: The use_by_default of this BackupCodeTwoFaAccountConfig.  # noqa: E501
        :type: bool
        """

        self._use_by_default = use_by_default

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
        if issubclass(BackupCodeTwoFaAccountConfig, dict):
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
        if not isinstance(other, BackupCodeTwoFaAccountConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
