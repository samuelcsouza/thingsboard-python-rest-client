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

class SelfRegistrationParams(object):
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
        'admin_settings_id': 'str',
        'sign_up_text_message': 'str',
        'captcha_site_key': 'str',
        'captcha_version': 'str',
        'captcha_action': 'str',
        'show_privacy_policy': 'bool',
        'show_terms_of_use': 'bool',
        'domain_name': 'str',
        'captcha_secret_key': 'str',
        'privacy_policy': 'str',
        'terms_of_use': 'str',
        'notification_email': 'str',
        'default_dashboard_id': 'str',
        'default_dashboard_fullscreen': 'bool',
        'permissions': 'list[GroupPermission]',
        'pkg_name': 'str',
        'app_secret': 'str',
        'app_scheme': 'str',
        'app_host': 'str'
    }

    attribute_map = {
        'admin_settings_id': 'adminSettingsId',
        'sign_up_text_message': 'signUpTextMessage',
        'captcha_site_key': 'captchaSiteKey',
        'captcha_version': 'captchaVersion',
        'captcha_action': 'captchaAction',
        'show_privacy_policy': 'showPrivacyPolicy',
        'show_terms_of_use': 'showTermsOfUse',
        'domain_name': 'domainName',
        'captcha_secret_key': 'captchaSecretKey',
        'privacy_policy': 'privacyPolicy',
        'terms_of_use': 'termsOfUse',
        'notification_email': 'notificationEmail',
        'default_dashboard_id': 'defaultDashboardId',
        'default_dashboard_fullscreen': 'defaultDashboardFullscreen',
        'permissions': 'permissions',
        'pkg_name': 'pkgName',
        'app_secret': 'appSecret',
        'app_scheme': 'appScheme',
        'app_host': 'appHost'
    }

    def __init__(self, admin_settings_id=None, sign_up_text_message=None, captcha_site_key=None, captcha_version=None, captcha_action=None, show_privacy_policy=None, show_terms_of_use=None, domain_name=None, captcha_secret_key=None, privacy_policy=None, terms_of_use=None, notification_email=None, default_dashboard_id=None, default_dashboard_fullscreen=None, permissions=None, pkg_name=None, app_secret=None, app_scheme=None, app_host=None):  # noqa: E501
        """SelfRegistrationParams - a model defined in Swagger"""  # noqa: E501
        self._admin_settings_id = None
        self._sign_up_text_message = None
        self._captcha_site_key = None
        self._captcha_version = None
        self._captcha_action = None
        self._show_privacy_policy = None
        self._show_terms_of_use = None
        self._domain_name = None
        self._captcha_secret_key = None
        self._privacy_policy = None
        self._terms_of_use = None
        self._notification_email = None
        self._default_dashboard_id = None
        self._default_dashboard_fullscreen = None
        self._permissions = None
        self._pkg_name = None
        self._app_secret = None
        self._app_scheme = None
        self._app_host = None
        self.discriminator = None
        if admin_settings_id is not None:
            self.admin_settings_id = admin_settings_id
        if sign_up_text_message is not None:
            self.sign_up_text_message = sign_up_text_message
        if captcha_site_key is not None:
            self.captcha_site_key = captcha_site_key
        if captcha_version is not None:
            self.captcha_version = captcha_version
        if captcha_action is not None:
            self.captcha_action = captcha_action
        if show_privacy_policy is not None:
            self.show_privacy_policy = show_privacy_policy
        if show_terms_of_use is not None:
            self.show_terms_of_use = show_terms_of_use
        if domain_name is not None:
            self.domain_name = domain_name
        if captcha_secret_key is not None:
            self.captcha_secret_key = captcha_secret_key
        if privacy_policy is not None:
            self.privacy_policy = privacy_policy
        if terms_of_use is not None:
            self.terms_of_use = terms_of_use
        if notification_email is not None:
            self.notification_email = notification_email
        if default_dashboard_id is not None:
            self.default_dashboard_id = default_dashboard_id
        if default_dashboard_fullscreen is not None:
            self.default_dashboard_fullscreen = default_dashboard_fullscreen
        if permissions is not None:
            self.permissions = permissions
        if pkg_name is not None:
            self.pkg_name = pkg_name
        if app_secret is not None:
            self.app_secret = app_secret
        if app_scheme is not None:
            self.app_scheme = app_scheme
        if app_host is not None:
            self.app_host = app_host

    @property
    def admin_settings_id(self):
        """Gets the admin_settings_id of this SelfRegistrationParams.  # noqa: E501


        :return: The admin_settings_id of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._admin_settings_id

    @admin_settings_id.setter
    def admin_settings_id(self, admin_settings_id):
        """Sets the admin_settings_id of this SelfRegistrationParams.


        :param admin_settings_id: The admin_settings_id of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._admin_settings_id = admin_settings_id

    @property
    def sign_up_text_message(self):
        """Gets the sign_up_text_message of this SelfRegistrationParams.  # noqa: E501


        :return: The sign_up_text_message of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._sign_up_text_message

    @sign_up_text_message.setter
    def sign_up_text_message(self, sign_up_text_message):
        """Sets the sign_up_text_message of this SelfRegistrationParams.


        :param sign_up_text_message: The sign_up_text_message of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._sign_up_text_message = sign_up_text_message

    @property
    def captcha_site_key(self):
        """Gets the captcha_site_key of this SelfRegistrationParams.  # noqa: E501


        :return: The captcha_site_key of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._captcha_site_key

    @captcha_site_key.setter
    def captcha_site_key(self, captcha_site_key):
        """Sets the captcha_site_key of this SelfRegistrationParams.


        :param captcha_site_key: The captcha_site_key of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._captcha_site_key = captcha_site_key

    @property
    def captcha_version(self):
        """Gets the captcha_version of this SelfRegistrationParams.  # noqa: E501


        :return: The captcha_version of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._captcha_version

    @captcha_version.setter
    def captcha_version(self, captcha_version):
        """Sets the captcha_version of this SelfRegistrationParams.


        :param captcha_version: The captcha_version of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._captcha_version = captcha_version

    @property
    def captcha_action(self):
        """Gets the captcha_action of this SelfRegistrationParams.  # noqa: E501


        :return: The captcha_action of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._captcha_action

    @captcha_action.setter
    def captcha_action(self, captcha_action):
        """Sets the captcha_action of this SelfRegistrationParams.


        :param captcha_action: The captcha_action of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._captcha_action = captcha_action

    @property
    def show_privacy_policy(self):
        """Gets the show_privacy_policy of this SelfRegistrationParams.  # noqa: E501


        :return: The show_privacy_policy of this SelfRegistrationParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_privacy_policy

    @show_privacy_policy.setter
    def show_privacy_policy(self, show_privacy_policy):
        """Sets the show_privacy_policy of this SelfRegistrationParams.


        :param show_privacy_policy: The show_privacy_policy of this SelfRegistrationParams.  # noqa: E501
        :type: bool
        """

        self._show_privacy_policy = show_privacy_policy

    @property
    def show_terms_of_use(self):
        """Gets the show_terms_of_use of this SelfRegistrationParams.  # noqa: E501


        :return: The show_terms_of_use of this SelfRegistrationParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_terms_of_use

    @show_terms_of_use.setter
    def show_terms_of_use(self, show_terms_of_use):
        """Sets the show_terms_of_use of this SelfRegistrationParams.


        :param show_terms_of_use: The show_terms_of_use of this SelfRegistrationParams.  # noqa: E501
        :type: bool
        """

        self._show_terms_of_use = show_terms_of_use

    @property
    def domain_name(self):
        """Gets the domain_name of this SelfRegistrationParams.  # noqa: E501


        :return: The domain_name of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this SelfRegistrationParams.


        :param domain_name: The domain_name of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def captcha_secret_key(self):
        """Gets the captcha_secret_key of this SelfRegistrationParams.  # noqa: E501


        :return: The captcha_secret_key of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._captcha_secret_key

    @captcha_secret_key.setter
    def captcha_secret_key(self, captcha_secret_key):
        """Sets the captcha_secret_key of this SelfRegistrationParams.


        :param captcha_secret_key: The captcha_secret_key of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._captcha_secret_key = captcha_secret_key

    @property
    def privacy_policy(self):
        """Gets the privacy_policy of this SelfRegistrationParams.  # noqa: E501


        :return: The privacy_policy of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._privacy_policy

    @privacy_policy.setter
    def privacy_policy(self, privacy_policy):
        """Sets the privacy_policy of this SelfRegistrationParams.


        :param privacy_policy: The privacy_policy of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._privacy_policy = privacy_policy

    @property
    def terms_of_use(self):
        """Gets the terms_of_use of this SelfRegistrationParams.  # noqa: E501


        :return: The terms_of_use of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._terms_of_use

    @terms_of_use.setter
    def terms_of_use(self, terms_of_use):
        """Sets the terms_of_use of this SelfRegistrationParams.


        :param terms_of_use: The terms_of_use of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._terms_of_use = terms_of_use

    @property
    def notification_email(self):
        """Gets the notification_email of this SelfRegistrationParams.  # noqa: E501


        :return: The notification_email of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._notification_email

    @notification_email.setter
    def notification_email(self, notification_email):
        """Sets the notification_email of this SelfRegistrationParams.


        :param notification_email: The notification_email of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._notification_email = notification_email

    @property
    def default_dashboard_id(self):
        """Gets the default_dashboard_id of this SelfRegistrationParams.  # noqa: E501


        :return: The default_dashboard_id of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._default_dashboard_id

    @default_dashboard_id.setter
    def default_dashboard_id(self, default_dashboard_id):
        """Sets the default_dashboard_id of this SelfRegistrationParams.


        :param default_dashboard_id: The default_dashboard_id of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._default_dashboard_id = default_dashboard_id

    @property
    def default_dashboard_fullscreen(self):
        """Gets the default_dashboard_fullscreen of this SelfRegistrationParams.  # noqa: E501


        :return: The default_dashboard_fullscreen of this SelfRegistrationParams.  # noqa: E501
        :rtype: bool
        """
        return self._default_dashboard_fullscreen

    @default_dashboard_fullscreen.setter
    def default_dashboard_fullscreen(self, default_dashboard_fullscreen):
        """Sets the default_dashboard_fullscreen of this SelfRegistrationParams.


        :param default_dashboard_fullscreen: The default_dashboard_fullscreen of this SelfRegistrationParams.  # noqa: E501
        :type: bool
        """

        self._default_dashboard_fullscreen = default_dashboard_fullscreen

    @property
    def permissions(self):
        """Gets the permissions of this SelfRegistrationParams.  # noqa: E501


        :return: The permissions of this SelfRegistrationParams.  # noqa: E501
        :rtype: list[GroupPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this SelfRegistrationParams.


        :param permissions: The permissions of this SelfRegistrationParams.  # noqa: E501
        :type: list[GroupPermission]
        """

        self._permissions = permissions

    @property
    def pkg_name(self):
        """Gets the pkg_name of this SelfRegistrationParams.  # noqa: E501


        :return: The pkg_name of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._pkg_name

    @pkg_name.setter
    def pkg_name(self, pkg_name):
        """Sets the pkg_name of this SelfRegistrationParams.


        :param pkg_name: The pkg_name of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._pkg_name = pkg_name

    @property
    def app_secret(self):
        """Gets the app_secret of this SelfRegistrationParams.  # noqa: E501


        :return: The app_secret of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this SelfRegistrationParams.


        :param app_secret: The app_secret of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._app_secret = app_secret

    @property
    def app_scheme(self):
        """Gets the app_scheme of this SelfRegistrationParams.  # noqa: E501


        :return: The app_scheme of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._app_scheme

    @app_scheme.setter
    def app_scheme(self, app_scheme):
        """Sets the app_scheme of this SelfRegistrationParams.


        :param app_scheme: The app_scheme of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._app_scheme = app_scheme

    @property
    def app_host(self):
        """Gets the app_host of this SelfRegistrationParams.  # noqa: E501


        :return: The app_host of this SelfRegistrationParams.  # noqa: E501
        :rtype: str
        """
        return self._app_host

    @app_host.setter
    def app_host(self, app_host):
        """Sets the app_host of this SelfRegistrationParams.


        :param app_host: The app_host of this SelfRegistrationParams.  # noqa: E501
        :type: str
        """

        self._app_host = app_host

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
        if issubclass(SelfRegistrationParams, dict):
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
        if not isinstance(other, SelfRegistrationParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
