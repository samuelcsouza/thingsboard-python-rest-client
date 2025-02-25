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

class Notification(object):
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
        'additional_config': 'JsonNode',
        'created_time': 'int',
        'id': 'NotificationId',
        'info': 'NotificationInfo',
        'recipient_id': 'UserId',
        'request_id': 'NotificationRequestId',
        'status': 'str',
        'subject': 'str',
        'text': 'str',
        'type': 'str'
    }

    attribute_map = {
        'additional_config': 'additionalConfig',
        'created_time': 'createdTime',
        'id': 'id',
        'info': 'info',
        'recipient_id': 'recipientId',
        'request_id': 'requestId',
        'status': 'status',
        'subject': 'subject',
        'text': 'text',
        'type': 'type'
    }

    def __init__(self, additional_config=None, created_time=None, id=None, info=None, recipient_id=None, request_id=None, status=None, subject=None, text=None, type=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501
        self._additional_config = None
        self._created_time = None
        self._id = None
        self._info = None
        self._recipient_id = None
        self._request_id = None
        self._status = None
        self._subject = None
        self._text = None
        self._type = None
        self.discriminator = None
        if additional_config is not None:
            self.additional_config = additional_config
        if created_time is not None:
            self.created_time = created_time
        if id is not None:
            self.id = id
        if info is not None:
            self.info = info
        if recipient_id is not None:
            self.recipient_id = recipient_id
        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status
        if subject is not None:
            self.subject = subject
        if text is not None:
            self.text = text
        if type is not None:
            self.type = type

    @property
    def additional_config(self):
        """Gets the additional_config of this Notification.  # noqa: E501


        :return: The additional_config of this Notification.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_config

    @additional_config.setter
    def additional_config(self, additional_config):
        """Sets the additional_config of this Notification.


        :param additional_config: The additional_config of this Notification.  # noqa: E501
        :type: JsonNode
        """

        self._additional_config = additional_config

    @property
    def created_time(self):
        """Gets the created_time of this Notification.  # noqa: E501


        :return: The created_time of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Notification.


        :param created_time: The created_time of this Notification.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def id(self):
        """Gets the id of this Notification.  # noqa: E501


        :return: The id of this Notification.  # noqa: E501
        :rtype: NotificationId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Notification.


        :param id: The id of this Notification.  # noqa: E501
        :type: NotificationId
        """

        self._id = id

    @property
    def info(self):
        """Gets the info of this Notification.  # noqa: E501


        :return: The info of this Notification.  # noqa: E501
        :rtype: NotificationInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Notification.


        :param info: The info of this Notification.  # noqa: E501
        :type: NotificationInfo
        """

        self._info = info

    @property
    def recipient_id(self):
        """Gets the recipient_id of this Notification.  # noqa: E501


        :return: The recipient_id of this Notification.  # noqa: E501
        :rtype: UserId
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this Notification.


        :param recipient_id: The recipient_id of this Notification.  # noqa: E501
        :type: UserId
        """

        self._recipient_id = recipient_id

    @property
    def request_id(self):
        """Gets the request_id of this Notification.  # noqa: E501


        :return: The request_id of this Notification.  # noqa: E501
        :rtype: NotificationRequestId
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this Notification.


        :param request_id: The request_id of this Notification.  # noqa: E501
        :type: NotificationRequestId
        """

        self._request_id = request_id

    @property
    def status(self):
        """Gets the status of this Notification.  # noqa: E501


        :return: The status of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Notification.


        :param status: The status of this Notification.  # noqa: E501
        :type: str
        """
        allowed_values = ["READ", "SENT"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def subject(self):
        """Gets the subject of this Notification.  # noqa: E501


        :return: The subject of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Notification.


        :param subject: The subject of this Notification.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def text(self):
        """Gets the text of this Notification.  # noqa: E501


        :return: The text of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Notification.


        :param text: The text of this Notification.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def type(self):
        """Gets the type of this Notification.  # noqa: E501


        :return: The type of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Notification.


        :param type: The type of this Notification.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "ALARM_ASSIGNMENT", "ALARM_COMMENT", "API_USAGE_LIMIT", "DEVICE_ACTIVITY", "ENTITIES_LIMIT", "ENTITY_ACTION", "GENERAL", "NEW_PLATFORM_VERSION", "RATE_LIMITS", "RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT", "RULE_NODE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(Notification, dict):
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
