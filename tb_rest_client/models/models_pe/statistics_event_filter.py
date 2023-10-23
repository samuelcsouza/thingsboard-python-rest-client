# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.0PE-SNAPSHOT
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
from tb_rest_client.models.models_pe.event_filter import EventFilter  # noqa: F401,E501

class StatisticsEventFilter(EventFilter):
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
        'not_empty': 'bool',
        'event_type': 'str',
        'server': 'str',
        'min_messages_processed': 'int',
        'max_messages_processed': 'int',
        'min_errors_occurred': 'int',
        'max_errors_occurred': 'int'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'not_empty': 'notEmpty',
        'event_type': 'eventType',
        'server': 'server',
        'min_messages_processed': 'minMessagesProcessed',
        'max_messages_processed': 'maxMessagesProcessed',
        'min_errors_occurred': 'minErrorsOccurred',
        'max_errors_occurred': 'maxErrorsOccurred'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, not_empty=None, event_type=None, server=None, min_messages_processed=None, max_messages_processed=None, min_errors_occurred=None, max_errors_occurred=None, *args, **kwargs):  # noqa: E501
        """StatisticsEventFilter - a model defined in Swagger"""  # noqa: E501
        self._not_empty = None
        self._event_type = None
        self._server = None
        self._min_messages_processed = None
        self._max_messages_processed = None
        self._min_errors_occurred = None
        self._max_errors_occurred = None
        self.discriminator = None
        if not_empty is not None:
            self.not_empty = not_empty
        self.event_type = event_type
        if server is not None:
            self.server = server
        if min_messages_processed is not None:
            self.min_messages_processed = min_messages_processed
        if max_messages_processed is not None:
            self.max_messages_processed = max_messages_processed
        if min_errors_occurred is not None:
            self.min_errors_occurred = min_errors_occurred
        if max_errors_occurred is not None:
            self.max_errors_occurred = max_errors_occurred
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def not_empty(self):
        """Gets the not_empty of this StatisticsEventFilter.  # noqa: E501


        :return: The not_empty of this StatisticsEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._not_empty

    @not_empty.setter
    def not_empty(self, not_empty):
        """Sets the not_empty of this StatisticsEventFilter.


        :param not_empty: The not_empty of this StatisticsEventFilter.  # noqa: E501
        :type: bool
        """

        self._not_empty = not_empty

    @property
    def event_type(self):
        """Gets the event_type of this StatisticsEventFilter.  # noqa: E501

        String value representing the event type  # noqa: E501

        :return: The event_type of this StatisticsEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this StatisticsEventFilter.

        String value representing the event type  # noqa: E501

        :param event_type: The event_type of this StatisticsEventFilter.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DEBUG_CONVERTER", "DEBUG_INTEGRATION", "DEBUG_RULE_CHAIN", "DEBUG_RULE_NODE", "ERROR", "LC_EVENT", "RAW_DATA", "STATS"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def server(self):
        """Gets the server of this StatisticsEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this StatisticsEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this StatisticsEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this StatisticsEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def min_messages_processed(self):
        """Gets the min_messages_processed of this StatisticsEventFilter.  # noqa: E501

        The minimum number of successfully processed messages  # noqa: E501

        :return: The min_messages_processed of this StatisticsEventFilter.  # noqa: E501
        :rtype: int
        """
        return self._min_messages_processed

    @min_messages_processed.setter
    def min_messages_processed(self, min_messages_processed):
        """Sets the min_messages_processed of this StatisticsEventFilter.

        The minimum number of successfully processed messages  # noqa: E501

        :param min_messages_processed: The min_messages_processed of this StatisticsEventFilter.  # noqa: E501
        :type: int
        """

        self._min_messages_processed = min_messages_processed

    @property
    def max_messages_processed(self):
        """Gets the max_messages_processed of this StatisticsEventFilter.  # noqa: E501

        The maximum number of successfully processed messages  # noqa: E501

        :return: The max_messages_processed of this StatisticsEventFilter.  # noqa: E501
        :rtype: int
        """
        return self._max_messages_processed

    @max_messages_processed.setter
    def max_messages_processed(self, max_messages_processed):
        """Sets the max_messages_processed of this StatisticsEventFilter.

        The maximum number of successfully processed messages  # noqa: E501

        :param max_messages_processed: The max_messages_processed of this StatisticsEventFilter.  # noqa: E501
        :type: int
        """

        self._max_messages_processed = max_messages_processed

    @property
    def min_errors_occurred(self):
        """Gets the min_errors_occurred of this StatisticsEventFilter.  # noqa: E501

        The minimum number of errors occurred during messages processing  # noqa: E501

        :return: The min_errors_occurred of this StatisticsEventFilter.  # noqa: E501
        :rtype: int
        """
        return self._min_errors_occurred

    @min_errors_occurred.setter
    def min_errors_occurred(self, min_errors_occurred):
        """Sets the min_errors_occurred of this StatisticsEventFilter.

        The minimum number of errors occurred during messages processing  # noqa: E501

        :param min_errors_occurred: The min_errors_occurred of this StatisticsEventFilter.  # noqa: E501
        :type: int
        """

        self._min_errors_occurred = min_errors_occurred

    @property
    def max_errors_occurred(self):
        """Gets the max_errors_occurred of this StatisticsEventFilter.  # noqa: E501

        The maximum number of errors occurred during messages processing  # noqa: E501

        :return: The max_errors_occurred of this StatisticsEventFilter.  # noqa: E501
        :rtype: int
        """
        return self._max_errors_occurred

    @max_errors_occurred.setter
    def max_errors_occurred(self, max_errors_occurred):
        """Sets the max_errors_occurred of this StatisticsEventFilter.

        The maximum number of errors occurred during messages processing  # noqa: E501

        :param max_errors_occurred: The max_errors_occurred of this StatisticsEventFilter.  # noqa: E501
        :type: int
        """

        self._max_errors_occurred = max_errors_occurred

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
        if issubclass(StatisticsEventFilter, dict):
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
        if not isinstance(other, StatisticsEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
