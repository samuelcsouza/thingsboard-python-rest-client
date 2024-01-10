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
from tb_rest_client.models.models_pe.entity_filter import EntityFilter  # noqa: F401,E501

class EntitiesByGroupNameFilter(EntityFilter):
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
        'entity_group_name_filter': 'str',
        'group_type': 'str',
        'owner_id': 'EntityId'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'entity_group_name_filter': 'entityGroupNameFilter',
        'group_type': 'groupType',
        'owner_id': 'ownerId'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, entity_group_name_filter=None, group_type=None, owner_id=None, *args, **kwargs):  # noqa: E501
        """EntitiesByGroupNameFilter - a model defined in Swagger"""  # noqa: E501
        self._entity_group_name_filter = None
        self._group_type = None
        self._owner_id = None
        self.discriminator = None
        if entity_group_name_filter is not None:
            self.entity_group_name_filter = entity_group_name_filter
        if group_type is not None:
            self.group_type = group_type
        if owner_id is not None:
            self.owner_id = owner_id
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def entity_group_name_filter(self):
        """Gets the entity_group_name_filter of this EntitiesByGroupNameFilter.  # noqa: E501


        :return: The entity_group_name_filter of this EntitiesByGroupNameFilter.  # noqa: E501
        :rtype: str
        """
        return self._entity_group_name_filter

    @entity_group_name_filter.setter
    def entity_group_name_filter(self, entity_group_name_filter):
        """Sets the entity_group_name_filter of this EntitiesByGroupNameFilter.


        :param entity_group_name_filter: The entity_group_name_filter of this EntitiesByGroupNameFilter.  # noqa: E501
        :type: str
        """

        self._entity_group_name_filter = entity_group_name_filter

    @property
    def group_type(self):
        """Gets the group_type of this EntitiesByGroupNameFilter.  # noqa: E501


        :return: The group_type of this EntitiesByGroupNameFilter.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this EntitiesByGroupNameFilter.


        :param group_type: The group_type of this EntitiesByGroupNameFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "ASSET_PROFILE", "BLOB_ENTITY", "CONVERTER", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_GROUP", "ENTITY_VIEW", "GROUP_PERMISSION", "INTEGRATION", "NOTIFICATION", "NOTIFICATION_REQUEST", "NOTIFICATION_RULE", "NOTIFICATION_TARGET", "NOTIFICATION_TEMPLATE", "OTA_PACKAGE", "QUEUE", "ROLE", "RPC", "RULE_CHAIN", "RULE_NODE", "SCHEDULER_EVENT", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `group_type` ({0}), must be one of {1}"  # noqa: E501
                .format(group_type, allowed_values)
            )

        self._group_type = group_type

    @property
    def owner_id(self):
        """Gets the owner_id of this EntitiesByGroupNameFilter.  # noqa: E501


        :return: The owner_id of this EntitiesByGroupNameFilter.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this EntitiesByGroupNameFilter.


        :param owner_id: The owner_id of this EntitiesByGroupNameFilter.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

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
        if issubclass(EntitiesByGroupNameFilter, dict):
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
        if not isinstance(other, EntitiesByGroupNameFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
