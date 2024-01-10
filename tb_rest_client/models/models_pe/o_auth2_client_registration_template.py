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

class OAuth2ClientRegistrationTemplate(object):
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
        'access_token_uri': 'str',
        'additional_info': 'JsonNode',
        'authorization_uri': 'str',
        'client_authentication_method': 'str',
        'comment': 'str',
        'created_time': 'int',
        'help_link': 'str',
        'id': 'OAuth2ClientRegistrationTemplateId',
        'jwk_set_uri': 'str',
        'login_button_icon': 'str',
        'login_button_label': 'str',
        'mapper_config': 'OAuth2MapperConfig',
        'name': 'str',
        'provider_id': 'str',
        'scope': 'list[str]',
        'user_info_uri': 'str',
        'user_name_attribute_name': 'str'
    }

    attribute_map = {
        'access_token_uri': 'accessTokenUri',
        'additional_info': 'additionalInfo',
        'authorization_uri': 'authorizationUri',
        'client_authentication_method': 'clientAuthenticationMethod',
        'comment': 'comment',
        'created_time': 'createdTime',
        'help_link': 'helpLink',
        'id': 'id',
        'jwk_set_uri': 'jwkSetUri',
        'login_button_icon': 'loginButtonIcon',
        'login_button_label': 'loginButtonLabel',
        'mapper_config': 'mapperConfig',
        'name': 'name',
        'provider_id': 'providerId',
        'scope': 'scope',
        'user_info_uri': 'userInfoUri',
        'user_name_attribute_name': 'userNameAttributeName'
    }

    def __init__(self, access_token_uri=None, additional_info=None, authorization_uri=None, client_authentication_method=None, comment=None, created_time=None, help_link=None, id=None, jwk_set_uri=None, login_button_icon=None, login_button_label=None, mapper_config=None, name=None, provider_id=None, scope=None, user_info_uri=None, user_name_attribute_name=None):  # noqa: E501
        """OAuth2ClientRegistrationTemplate - a model defined in Swagger"""  # noqa: E501
        self._access_token_uri = None
        self._additional_info = None
        self._authorization_uri = None
        self._client_authentication_method = None
        self._comment = None
        self._created_time = None
        self._help_link = None
        self._id = None
        self._jwk_set_uri = None
        self._login_button_icon = None
        self._login_button_label = None
        self._mapper_config = None
        self._name = None
        self._provider_id = None
        self._scope = None
        self._user_info_uri = None
        self._user_name_attribute_name = None
        self.discriminator = None
        if access_token_uri is not None:
            self.access_token_uri = access_token_uri
        if additional_info is not None:
            self.additional_info = additional_info
        if authorization_uri is not None:
            self.authorization_uri = authorization_uri
        if client_authentication_method is not None:
            self.client_authentication_method = client_authentication_method
        if comment is not None:
            self.comment = comment
        if created_time is not None:
            self.created_time = created_time
        if help_link is not None:
            self.help_link = help_link
        if id is not None:
            self.id = id
        if jwk_set_uri is not None:
            self.jwk_set_uri = jwk_set_uri
        if login_button_icon is not None:
            self.login_button_icon = login_button_icon
        if login_button_label is not None:
            self.login_button_label = login_button_label
        if mapper_config is not None:
            self.mapper_config = mapper_config
        if name is not None:
            self.name = name
        self.provider_id = provider_id
        if scope is not None:
            self.scope = scope
        if user_info_uri is not None:
            self.user_info_uri = user_info_uri
        if user_name_attribute_name is not None:
            self.user_name_attribute_name = user_name_attribute_name

    @property
    def access_token_uri(self):
        """Gets the access_token_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default access token URI of the OAuth2 provider  # noqa: E501

        :return: The access_token_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._access_token_uri

    @access_token_uri.setter
    def access_token_uri(self, access_token_uri):
        """Sets the access_token_uri of this OAuth2ClientRegistrationTemplate.

        Default access token URI of the OAuth2 provider  # noqa: E501

        :param access_token_uri: The access_token_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._access_token_uri = access_token_uri

    @property
    def additional_info(self):
        """Gets the additional_info of this OAuth2ClientRegistrationTemplate.  # noqa: E501


        :return: The additional_info of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this OAuth2ClientRegistrationTemplate.


        :param additional_info: The additional_info of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def authorization_uri(self):
        """Gets the authorization_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default authorization URI of the OAuth2 provider  # noqa: E501

        :return: The authorization_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._authorization_uri

    @authorization_uri.setter
    def authorization_uri(self, authorization_uri):
        """Sets the authorization_uri of this OAuth2ClientRegistrationTemplate.

        Default authorization URI of the OAuth2 provider  # noqa: E501

        :param authorization_uri: The authorization_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._authorization_uri = authorization_uri

    @property
    def client_authentication_method(self):
        """Gets the client_authentication_method of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default client authentication method to use: 'BASIC' or 'POST'  # noqa: E501

        :return: The client_authentication_method of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._client_authentication_method

    @client_authentication_method.setter
    def client_authentication_method(self, client_authentication_method):
        """Sets the client_authentication_method of this OAuth2ClientRegistrationTemplate.

        Default client authentication method to use: 'BASIC' or 'POST'  # noqa: E501

        :param client_authentication_method: The client_authentication_method of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._client_authentication_method = client_authentication_method

    @property
    def comment(self):
        """Gets the comment of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Comment for OAuth2 provider  # noqa: E501

        :return: The comment of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this OAuth2ClientRegistrationTemplate.

        Comment for OAuth2 provider  # noqa: E501

        :param comment: The comment of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created_time(self):
        """Gets the created_time of this OAuth2ClientRegistrationTemplate.  # noqa: E501


        :return: The created_time of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this OAuth2ClientRegistrationTemplate.


        :param created_time: The created_time of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def help_link(self):
        """Gets the help_link of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Help link for OAuth2 provider  # noqa: E501

        :return: The help_link of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._help_link

    @help_link.setter
    def help_link(self, help_link):
        """Sets the help_link of this OAuth2ClientRegistrationTemplate.

        Help link for OAuth2 provider  # noqa: E501

        :param help_link: The help_link of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._help_link = help_link

    @property
    def id(self):
        """Gets the id of this OAuth2ClientRegistrationTemplate.  # noqa: E501


        :return: The id of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: OAuth2ClientRegistrationTemplateId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuth2ClientRegistrationTemplate.


        :param id: The id of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: OAuth2ClientRegistrationTemplateId
        """

        self._id = id

    @property
    def jwk_set_uri(self):
        """Gets the jwk_set_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default JSON Web Key URI of the OAuth2 provider  # noqa: E501

        :return: The jwk_set_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._jwk_set_uri

    @jwk_set_uri.setter
    def jwk_set_uri(self, jwk_set_uri):
        """Sets the jwk_set_uri of this OAuth2ClientRegistrationTemplate.

        Default JSON Web Key URI of the OAuth2 provider  # noqa: E501

        :param jwk_set_uri: The jwk_set_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._jwk_set_uri = jwk_set_uri

    @property
    def login_button_icon(self):
        """Gets the login_button_icon of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default log in button icon for OAuth2 provider  # noqa: E501

        :return: The login_button_icon of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._login_button_icon

    @login_button_icon.setter
    def login_button_icon(self, login_button_icon):
        """Sets the login_button_icon of this OAuth2ClientRegistrationTemplate.

        Default log in button icon for OAuth2 provider  # noqa: E501

        :param login_button_icon: The login_button_icon of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._login_button_icon = login_button_icon

    @property
    def login_button_label(self):
        """Gets the login_button_label of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default OAuth2 provider label  # noqa: E501

        :return: The login_button_label of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._login_button_label

    @login_button_label.setter
    def login_button_label(self, login_button_label):
        """Sets the login_button_label of this OAuth2ClientRegistrationTemplate.

        Default OAuth2 provider label  # noqa: E501

        :param login_button_label: The login_button_label of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._login_button_label = login_button_label

    @property
    def mapper_config(self):
        """Gets the mapper_config of this OAuth2ClientRegistrationTemplate.  # noqa: E501


        :return: The mapper_config of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: OAuth2MapperConfig
        """
        return self._mapper_config

    @mapper_config.setter
    def mapper_config(self, mapper_config):
        """Sets the mapper_config of this OAuth2ClientRegistrationTemplate.


        :param mapper_config: The mapper_config of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: OAuth2MapperConfig
        """

        self._mapper_config = mapper_config

    @property
    def name(self):
        """Gets the name of this OAuth2ClientRegistrationTemplate.  # noqa: E501


        :return: The name of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuth2ClientRegistrationTemplate.


        :param name: The name of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def provider_id(self):
        """Gets the provider_id of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        OAuth2 provider identifier (e.g. its name)  # noqa: E501

        :return: The provider_id of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this OAuth2ClientRegistrationTemplate.

        OAuth2 provider identifier (e.g. its name)  # noqa: E501

        :param provider_id: The provider_id of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def scope(self):
        """Gets the scope of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default OAuth scopes that will be requested from OAuth2 platform  # noqa: E501

        :return: The scope of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OAuth2ClientRegistrationTemplate.

        Default OAuth scopes that will be requested from OAuth2 platform  # noqa: E501

        :param scope: The scope of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: list[str]
        """

        self._scope = scope

    @property
    def user_info_uri(self):
        """Gets the user_info_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default user info URI of the OAuth2 provider  # noqa: E501

        :return: The user_info_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._user_info_uri

    @user_info_uri.setter
    def user_info_uri(self, user_info_uri):
        """Sets the user_info_uri of this OAuth2ClientRegistrationTemplate.

        Default user info URI of the OAuth2 provider  # noqa: E501

        :param user_info_uri: The user_info_uri of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._user_info_uri = user_info_uri

    @property
    def user_name_attribute_name(self):
        """Gets the user_name_attribute_name of this OAuth2ClientRegistrationTemplate.  # noqa: E501

        Default name of the username attribute in OAuth2 provider log in response  # noqa: E501

        :return: The user_name_attribute_name of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._user_name_attribute_name

    @user_name_attribute_name.setter
    def user_name_attribute_name(self, user_name_attribute_name):
        """Sets the user_name_attribute_name of this OAuth2ClientRegistrationTemplate.

        Default name of the username attribute in OAuth2 provider log in response  # noqa: E501

        :param user_name_attribute_name: The user_name_attribute_name of this OAuth2ClientRegistrationTemplate.  # noqa: E501
        :type: str
        """

        self._user_name_attribute_name = user_name_attribute_name

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
        if issubclass(OAuth2ClientRegistrationTemplate, dict):
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
        if not isinstance(other, OAuth2ClientRegistrationTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
