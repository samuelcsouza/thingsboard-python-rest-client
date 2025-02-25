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

class RateLimitsNotificationRuleTriggerConfig(object):
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
        'apis': 'list[str]',
        'trigger_type': 'str'
    }

    attribute_map = {
        'apis': 'apis',
        'trigger_type': 'triggerType'
    }

    def __init__(self, apis=None, trigger_type=None):  # noqa: E501
        """RateLimitsNotificationRuleTriggerConfig - a model defined in Swagger"""  # noqa: E501
        self._apis = None
        self._trigger_type = None
        self.discriminator = None
        if apis is not None:
            self.apis = apis
        if trigger_type is not None:
            self.trigger_type = trigger_type

    @property
    def apis(self):
        """Gets the apis of this RateLimitsNotificationRuleTriggerConfig.  # noqa: E501


        :return: The apis of this RateLimitsNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        """Sets the apis of this RateLimitsNotificationRuleTriggerConfig.


        :param apis: The apis of this RateLimitsNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CASSANDRA_QUERIES", "ENTITY_EXPORT", "ENTITY_IMPORT", "NOTIFICATION_REQUESTS", "NOTIFICATION_REQUESTS_PER_RULE", "PASSWORD_RESET", "REST_REQUESTS_PER_CUSTOMER", "REST_REQUESTS_PER_TENANT", "TRANSPORT_MESSAGES_PER_DEVICE", "TRANSPORT_MESSAGES_PER_TENANT", "TWO_FA_VERIFICATION_CODE_CHECK", "TWO_FA_VERIFICATION_CODE_SEND", "WS_UPDATES_PER_SESSION"]  # noqa: E501
        if not set(apis).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `apis` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(apis) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._apis = apis

    @property
    def trigger_type(self):
        """Gets the trigger_type of this RateLimitsNotificationRuleTriggerConfig.  # noqa: E501


        :return: The trigger_type of this RateLimitsNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this RateLimitsNotificationRuleTriggerConfig.


        :param trigger_type: The trigger_type of this RateLimitsNotificationRuleTriggerConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "ALARM_ASSIGNMENT", "ALARM_COMMENT", "API_USAGE_LIMIT", "DEVICE_ACTIVITY", "ENTITIES_LIMIT", "ENTITY_ACTION", "NEW_PLATFORM_VERSION", "RATE_LIMITS", "RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT"]  # noqa: E501
        if trigger_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

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
        if issubclass(RateLimitsNotificationRuleTriggerConfig, dict):
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
        if not isinstance(other, RateLimitsNotificationRuleTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
