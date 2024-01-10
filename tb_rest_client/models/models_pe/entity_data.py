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

class EntityData(object):
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
        'agg_latest': 'dict(str, ComparisonTsValue)',
        'entity_id': 'EntityId',
        'latest': 'dict(str, object)',
        'read_attrs': 'bool',
        'read_ts': 'bool',
        'timeseries': 'dict(str, list[TsValue])'
    }

    attribute_map = {
        'agg_latest': 'aggLatest',
        'entity_id': 'entityId',
        'latest': 'latest',
        'read_attrs': 'readAttrs',
        'read_ts': 'readTs',
        'timeseries': 'timeseries'
    }

    def __init__(self, agg_latest=None, entity_id=None, latest=None, read_attrs=None, read_ts=None, timeseries=None):  # noqa: E501
        """EntityData - a model defined in Swagger"""  # noqa: E501
        self._agg_latest = None
        self._entity_id = None
        self._latest = None
        self._read_attrs = None
        self._read_ts = None
        self._timeseries = None
        self.discriminator = None
        if agg_latest is not None:
            self.agg_latest = agg_latest
        if entity_id is not None:
            self.entity_id = entity_id
        if latest is not None:
            self.latest = latest
        if read_attrs is not None:
            self.read_attrs = read_attrs
        if read_ts is not None:
            self.read_ts = read_ts
        if timeseries is not None:
            self.timeseries = timeseries

    @property
    def agg_latest(self):
        """Gets the agg_latest of this EntityData.  # noqa: E501


        :return: The agg_latest of this EntityData.  # noqa: E501
        :rtype: dict(str, ComparisonTsValue)
        """
        return self._agg_latest

    @agg_latest.setter
    def agg_latest(self, agg_latest):
        """Sets the agg_latest of this EntityData.


        :param agg_latest: The agg_latest of this EntityData.  # noqa: E501
        :type: dict(str, ComparisonTsValue)
        """

        self._agg_latest = agg_latest

    @property
    def entity_id(self):
        """Gets the entity_id of this EntityData.  # noqa: E501


        :return: The entity_id of this EntityData.  # noqa: E501
        :rtype: EntityId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EntityData.


        :param entity_id: The entity_id of this EntityData.  # noqa: E501
        :type: EntityId
        """

        self._entity_id = entity_id

    @property
    def latest(self):
        """Gets the latest of this EntityData.  # noqa: E501


        :return: The latest of this EntityData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this EntityData.


        :param latest: The latest of this EntityData.  # noqa: E501
        :type: dict(str, object)
        """

        self._latest = latest

    @property
    def read_attrs(self):
        """Gets the read_attrs of this EntityData.  # noqa: E501


        :return: The read_attrs of this EntityData.  # noqa: E501
        :rtype: bool
        """
        return self._read_attrs

    @read_attrs.setter
    def read_attrs(self, read_attrs):
        """Sets the read_attrs of this EntityData.


        :param read_attrs: The read_attrs of this EntityData.  # noqa: E501
        :type: bool
        """

        self._read_attrs = read_attrs

    @property
    def read_ts(self):
        """Gets the read_ts of this EntityData.  # noqa: E501


        :return: The read_ts of this EntityData.  # noqa: E501
        :rtype: bool
        """
        return self._read_ts

    @read_ts.setter
    def read_ts(self, read_ts):
        """Sets the read_ts of this EntityData.


        :param read_ts: The read_ts of this EntityData.  # noqa: E501
        :type: bool
        """

        self._read_ts = read_ts

    @property
    def timeseries(self):
        """Gets the timeseries of this EntityData.  # noqa: E501


        :return: The timeseries of this EntityData.  # noqa: E501
        :rtype: dict(str, list[TsValue])
        """
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries):
        """Sets the timeseries of this EntityData.


        :param timeseries: The timeseries of this EntityData.  # noqa: E501
        :type: dict(str, list[TsValue])
        """

        self._timeseries = timeseries

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
        if issubclass(EntityData, dict):
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
        if not isinstance(other, EntityData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
