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

class BulkImportResultDevice(object):
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
        'created': 'AtomicInteger',
        'errors': 'AtomicInteger',
        'errors_list': 'list[str]',
        'updated': 'AtomicInteger'
    }

    attribute_map = {
        'created': 'created',
        'errors': 'errors',
        'errors_list': 'errorsList',
        'updated': 'updated'
    }

    def __init__(self, created=None, errors=None, errors_list=None, updated=None):  # noqa: E501
        """BulkImportResultDevice - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._errors = None
        self._errors_list = None
        self._updated = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if errors is not None:
            self.errors = errors
        if errors_list is not None:
            self.errors_list = errors_list
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this BulkImportResultDevice.  # noqa: E501


        :return: The created of this BulkImportResultDevice.  # noqa: E501
        :rtype: AtomicInteger
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BulkImportResultDevice.


        :param created: The created of this BulkImportResultDevice.  # noqa: E501
        :type: AtomicInteger
        """

        self._created = created

    @property
    def errors(self):
        """Gets the errors of this BulkImportResultDevice.  # noqa: E501


        :return: The errors of this BulkImportResultDevice.  # noqa: E501
        :rtype: AtomicInteger
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BulkImportResultDevice.


        :param errors: The errors of this BulkImportResultDevice.  # noqa: E501
        :type: AtomicInteger
        """

        self._errors = errors

    @property
    def errors_list(self):
        """Gets the errors_list of this BulkImportResultDevice.  # noqa: E501


        :return: The errors_list of this BulkImportResultDevice.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors_list

    @errors_list.setter
    def errors_list(self, errors_list):
        """Sets the errors_list of this BulkImportResultDevice.


        :param errors_list: The errors_list of this BulkImportResultDevice.  # noqa: E501
        :type: list[str]
        """

        self._errors_list = errors_list

    @property
    def updated(self):
        """Gets the updated of this BulkImportResultDevice.  # noqa: E501


        :return: The updated of this BulkImportResultDevice.  # noqa: E501
        :rtype: AtomicInteger
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this BulkImportResultDevice.


        :param updated: The updated of this BulkImportResultDevice.  # noqa: E501
        :type: AtomicInteger
        """

        self._updated = updated

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
        if issubclass(BulkImportResultDevice, dict):
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
        if not isinstance(other, BulkImportResultDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
