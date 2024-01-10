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
from tb_rest_client.models.models_ce.transport_payload_type_configuration import TransportPayloadTypeConfiguration  # noqa: F401,E501

class ProtoTransportPayloadConfiguration(TransportPayloadTypeConfiguration):
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
        'device_attributes_proto_schema': 'str',
        'device_rpc_request_proto_schema': 'str',
        'device_rpc_response_proto_schema': 'str',
        'device_telemetry_proto_schema': 'str',
        'enable_compatibility_with_json_payload_format': 'bool',
        'use_json_payload_format_for_default_downlink_topics': 'bool'
    }
    if hasattr(TransportPayloadTypeConfiguration, "swagger_types"):
        swagger_types.update(TransportPayloadTypeConfiguration.swagger_types)

    attribute_map = {
        'device_attributes_proto_schema': 'deviceAttributesProtoSchema',
        'device_rpc_request_proto_schema': 'deviceRpcRequestProtoSchema',
        'device_rpc_response_proto_schema': 'deviceRpcResponseProtoSchema',
        'device_telemetry_proto_schema': 'deviceTelemetryProtoSchema',
        'enable_compatibility_with_json_payload_format': 'enableCompatibilityWithJsonPayloadFormat',
        'use_json_payload_format_for_default_downlink_topics': 'useJsonPayloadFormatForDefaultDownlinkTopics'
    }
    if hasattr(TransportPayloadTypeConfiguration, "attribute_map"):
        attribute_map.update(TransportPayloadTypeConfiguration.attribute_map)

    def __init__(self, device_attributes_proto_schema=None, device_rpc_request_proto_schema=None, device_rpc_response_proto_schema=None, device_telemetry_proto_schema=None, enable_compatibility_with_json_payload_format=None, use_json_payload_format_for_default_downlink_topics=None, *args, **kwargs):  # noqa: E501
        """ProtoTransportPayloadConfiguration - a model defined in Swagger"""  # noqa: E501
        self._device_attributes_proto_schema = None
        self._device_rpc_request_proto_schema = None
        self._device_rpc_response_proto_schema = None
        self._device_telemetry_proto_schema = None
        self._enable_compatibility_with_json_payload_format = None
        self._use_json_payload_format_for_default_downlink_topics = None
        self.discriminator = None
        if device_attributes_proto_schema is not None:
            self.device_attributes_proto_schema = device_attributes_proto_schema
        if device_rpc_request_proto_schema is not None:
            self.device_rpc_request_proto_schema = device_rpc_request_proto_schema
        if device_rpc_response_proto_schema is not None:
            self.device_rpc_response_proto_schema = device_rpc_response_proto_schema
        if device_telemetry_proto_schema is not None:
            self.device_telemetry_proto_schema = device_telemetry_proto_schema
        if enable_compatibility_with_json_payload_format is not None:
            self.enable_compatibility_with_json_payload_format = enable_compatibility_with_json_payload_format
        if use_json_payload_format_for_default_downlink_topics is not None:
            self.use_json_payload_format_for_default_downlink_topics = use_json_payload_format_for_default_downlink_topics
        TransportPayloadTypeConfiguration.__init__(self, *args, **kwargs)

    @property
    def device_attributes_proto_schema(self):
        """Gets the device_attributes_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501


        :return: The device_attributes_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_attributes_proto_schema

    @device_attributes_proto_schema.setter
    def device_attributes_proto_schema(self, device_attributes_proto_schema):
        """Sets the device_attributes_proto_schema of this ProtoTransportPayloadConfiguration.


        :param device_attributes_proto_schema: The device_attributes_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :type: str
        """

        self._device_attributes_proto_schema = device_attributes_proto_schema

    @property
    def device_rpc_request_proto_schema(self):
        """Gets the device_rpc_request_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501


        :return: The device_rpc_request_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_rpc_request_proto_schema

    @device_rpc_request_proto_schema.setter
    def device_rpc_request_proto_schema(self, device_rpc_request_proto_schema):
        """Sets the device_rpc_request_proto_schema of this ProtoTransportPayloadConfiguration.


        :param device_rpc_request_proto_schema: The device_rpc_request_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :type: str
        """

        self._device_rpc_request_proto_schema = device_rpc_request_proto_schema

    @property
    def device_rpc_response_proto_schema(self):
        """Gets the device_rpc_response_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501


        :return: The device_rpc_response_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_rpc_response_proto_schema

    @device_rpc_response_proto_schema.setter
    def device_rpc_response_proto_schema(self, device_rpc_response_proto_schema):
        """Sets the device_rpc_response_proto_schema of this ProtoTransportPayloadConfiguration.


        :param device_rpc_response_proto_schema: The device_rpc_response_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :type: str
        """

        self._device_rpc_response_proto_schema = device_rpc_response_proto_schema

    @property
    def device_telemetry_proto_schema(self):
        """Gets the device_telemetry_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501


        :return: The device_telemetry_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_telemetry_proto_schema

    @device_telemetry_proto_schema.setter
    def device_telemetry_proto_schema(self, device_telemetry_proto_schema):
        """Sets the device_telemetry_proto_schema of this ProtoTransportPayloadConfiguration.


        :param device_telemetry_proto_schema: The device_telemetry_proto_schema of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :type: str
        """

        self._device_telemetry_proto_schema = device_telemetry_proto_schema

    @property
    def enable_compatibility_with_json_payload_format(self):
        """Gets the enable_compatibility_with_json_payload_format of this ProtoTransportPayloadConfiguration.  # noqa: E501


        :return: The enable_compatibility_with_json_payload_format of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_compatibility_with_json_payload_format

    @enable_compatibility_with_json_payload_format.setter
    def enable_compatibility_with_json_payload_format(self, enable_compatibility_with_json_payload_format):
        """Sets the enable_compatibility_with_json_payload_format of this ProtoTransportPayloadConfiguration.


        :param enable_compatibility_with_json_payload_format: The enable_compatibility_with_json_payload_format of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_compatibility_with_json_payload_format = enable_compatibility_with_json_payload_format

    @property
    def use_json_payload_format_for_default_downlink_topics(self):
        """Gets the use_json_payload_format_for_default_downlink_topics of this ProtoTransportPayloadConfiguration.  # noqa: E501


        :return: The use_json_payload_format_for_default_downlink_topics of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_json_payload_format_for_default_downlink_topics

    @use_json_payload_format_for_default_downlink_topics.setter
    def use_json_payload_format_for_default_downlink_topics(self, use_json_payload_format_for_default_downlink_topics):
        """Sets the use_json_payload_format_for_default_downlink_topics of this ProtoTransportPayloadConfiguration.


        :param use_json_payload_format_for_default_downlink_topics: The use_json_payload_format_for_default_downlink_topics of this ProtoTransportPayloadConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_json_payload_format_for_default_downlink_topics = use_json_payload_format_for_default_downlink_topics

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
        if issubclass(ProtoTransportPayloadConfiguration, dict):
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
        if not isinstance(other, ProtoTransportPayloadConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
