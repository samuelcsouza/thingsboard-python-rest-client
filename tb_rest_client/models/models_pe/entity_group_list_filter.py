# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3PAAS-RC1
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from tb_rest_client.models.models_pe import EntityFilter


class EntityGroupListFilter(EntityFilter):
    """
    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_group_list': 'list[str]',
        'group_type': 'str'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'entity_group_list': 'entityGroupList',
        'group_type': 'groupType'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, entity_group_list=None, group_type=None, *args, **kwargs):  # noqa: E501
        """EntityGroupListFilter - a model defined in Swagger"""  # noqa: E501
        self._entity_group_list = None
        self._group_type = None
        self.discriminator = None
        if entity_group_list is not None:
            self.entity_group_list = entity_group_list
        if group_type is not None:
            self.group_type = group_type
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def entity_group_list(self):
        """Gets the entity_group_list of this EntityGroupListFilter.  # noqa: E501


        :return: The entity_group_list of this EntityGroupListFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._entity_group_list

    @entity_group_list.setter
    def entity_group_list(self, entity_group_list):
        """Sets the entity_group_list of this EntityGroupListFilter.


        :param entity_group_list: The entity_group_list of this EntityGroupListFilter.  # noqa: E501
        :type: list[str]
        """

        self._entity_group_list = entity_group_list

    @property
    def group_type(self):
        """Gets the group_type of this EntityGroupListFilter.  # noqa: E501


        :return: The group_type of this EntityGroupListFilter.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this EntityGroupListFilter.


        :param group_type: The group_type of this EntityGroupListFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "BILLING_CUSTOMER", "BLOB_ENTITY", "CONVERTER", "COUPON", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_GROUP", "ENTITY_VIEW", "GROUP_PERMISSION", "INTEGRATION", "OTA_PACKAGE", "ROLE", "RPC", "RULE_CHAIN", "RULE_NODE", "SCHEDULER_EVENT", "SUBSCRIPTION", "SUBSCRIPTION_PLAN", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `group_type` ({0}), must be one of {1}"  # noqa: E501
                .format(group_type, allowed_values)
            )

        self._group_type = group_type

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
        if issubclass(EntityGroupListFilter, dict):
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
        if not isinstance(other, EntityGroupListFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
