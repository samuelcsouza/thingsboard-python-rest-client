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
from tb_rest_client.models.models_ce.device_transport_configuration import DeviceTransportConfiguration  # noqa: F401,E501

class SnmpDeviceTransportConfiguration(DeviceTransportConfiguration):
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
        'authentication_passphrase': 'str',
        'authentication_protocol': 'str',
        'community': 'str',
        'context_name': 'str',
        'engine_id': 'str',
        'host': 'str',
        'port': 'int',
        'privacy_passphrase': 'str',
        'privacy_protocol': 'str',
        'protocol_version': 'str',
        'security_name': 'str',
        'username': 'str'
    }
    if hasattr(DeviceTransportConfiguration, "swagger_types"):
        swagger_types.update(DeviceTransportConfiguration.swagger_types)

    attribute_map = {
        'authentication_passphrase': 'authenticationPassphrase',
        'authentication_protocol': 'authenticationProtocol',
        'community': 'community',
        'context_name': 'contextName',
        'engine_id': 'engineId',
        'host': 'host',
        'port': 'port',
        'privacy_passphrase': 'privacyPassphrase',
        'privacy_protocol': 'privacyProtocol',
        'protocol_version': 'protocolVersion',
        'security_name': 'securityName',
        'username': 'username'
    }
    if hasattr(DeviceTransportConfiguration, "attribute_map"):
        attribute_map.update(DeviceTransportConfiguration.attribute_map)

    def __init__(self, authentication_passphrase=None, authentication_protocol=None, community=None, context_name=None, engine_id=None, host=None, port=None, privacy_passphrase=None, privacy_protocol=None, protocol_version=None, security_name=None, username=None, *args, **kwargs):  # noqa: E501
        """SnmpDeviceTransportConfiguration - a model defined in Swagger"""  # noqa: E501
        self._authentication_passphrase = None
        self._authentication_protocol = None
        self._community = None
        self._context_name = None
        self._engine_id = None
        self._host = None
        self._port = None
        self._privacy_passphrase = None
        self._privacy_protocol = None
        self._protocol_version = None
        self._security_name = None
        self._username = None
        self.discriminator = None
        if authentication_passphrase is not None:
            self.authentication_passphrase = authentication_passphrase
        if authentication_protocol is not None:
            self.authentication_protocol = authentication_protocol
        if community is not None:
            self.community = community
        if context_name is not None:
            self.context_name = context_name
        if engine_id is not None:
            self.engine_id = engine_id
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if privacy_passphrase is not None:
            self.privacy_passphrase = privacy_passphrase
        if privacy_protocol is not None:
            self.privacy_protocol = privacy_protocol
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if security_name is not None:
            self.security_name = security_name
        if username is not None:
            self.username = username
        DeviceTransportConfiguration.__init__(self, *args, **kwargs)

    @property
    def authentication_passphrase(self):
        """Gets the authentication_passphrase of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The authentication_passphrase of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._authentication_passphrase

    @authentication_passphrase.setter
    def authentication_passphrase(self, authentication_passphrase):
        """Sets the authentication_passphrase of this SnmpDeviceTransportConfiguration.


        :param authentication_passphrase: The authentication_passphrase of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._authentication_passphrase = authentication_passphrase

    @property
    def authentication_protocol(self):
        """Gets the authentication_protocol of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The authentication_protocol of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._authentication_protocol

    @authentication_protocol.setter
    def authentication_protocol(self, authentication_protocol):
        """Sets the authentication_protocol of this SnmpDeviceTransportConfiguration.


        :param authentication_protocol: The authentication_protocol of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["MD5", "SHA_1", "SHA_224", "SHA_256", "SHA_384", "SHA_512"]  # noqa: E501
        if authentication_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_protocol, allowed_values)
            )

        self._authentication_protocol = authentication_protocol

    @property
    def community(self):
        """Gets the community of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The community of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this SnmpDeviceTransportConfiguration.


        :param community: The community of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._community = community

    @property
    def context_name(self):
        """Gets the context_name of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The context_name of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._context_name

    @context_name.setter
    def context_name(self, context_name):
        """Sets the context_name of this SnmpDeviceTransportConfiguration.


        :param context_name: The context_name of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._context_name = context_name

    @property
    def engine_id(self):
        """Gets the engine_id of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The engine_id of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this SnmpDeviceTransportConfiguration.


        :param engine_id: The engine_id of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._engine_id = engine_id

    @property
    def host(self):
        """Gets the host of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The host of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SnmpDeviceTransportConfiguration.


        :param host: The host of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The port of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SnmpDeviceTransportConfiguration.


        :param port: The port of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def privacy_passphrase(self):
        """Gets the privacy_passphrase of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The privacy_passphrase of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._privacy_passphrase

    @privacy_passphrase.setter
    def privacy_passphrase(self, privacy_passphrase):
        """Sets the privacy_passphrase of this SnmpDeviceTransportConfiguration.


        :param privacy_passphrase: The privacy_passphrase of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._privacy_passphrase = privacy_passphrase

    @property
    def privacy_protocol(self):
        """Gets the privacy_protocol of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The privacy_protocol of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._privacy_protocol

    @privacy_protocol.setter
    def privacy_protocol(self, privacy_protocol):
        """Sets the privacy_protocol of this SnmpDeviceTransportConfiguration.


        :param privacy_protocol: The privacy_protocol of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["AES_128", "AES_192", "AES_256", "DES"]  # noqa: E501
        if privacy_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `privacy_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(privacy_protocol, allowed_values)
            )

        self._privacy_protocol = privacy_protocol

    @property
    def protocol_version(self):
        """Gets the protocol_version of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The protocol_version of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this SnmpDeviceTransportConfiguration.


        :param protocol_version: The protocol_version of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["V1", "V2C", "V3"]  # noqa: E501
        if protocol_version not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol_version` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol_version, allowed_values)
            )

        self._protocol_version = protocol_version

    @property
    def security_name(self):
        """Gets the security_name of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The security_name of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._security_name

    @security_name.setter
    def security_name(self, security_name):
        """Sets the security_name of this SnmpDeviceTransportConfiguration.


        :param security_name: The security_name of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._security_name = security_name

    @property
    def username(self):
        """Gets the username of this SnmpDeviceTransportConfiguration.  # noqa: E501


        :return: The username of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SnmpDeviceTransportConfiguration.


        :param username: The username of this SnmpDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(SnmpDeviceTransportConfiguration, dict):
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
        if not isinstance(other, SnmpDeviceTransportConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
