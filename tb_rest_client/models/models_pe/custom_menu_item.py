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

class CustomMenuItem(object):
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
        'name': 'str',
        'icon_url': 'str',
        'material_icon': 'str',
        'iframe_url': 'str',
        'dashboard_id': 'str',
        'hide_dashboard_toolbar': 'bool',
        'set_access_token': 'bool',
        'child_menu_items': 'list[CustomMenuItem]'
    }

    attribute_map = {
        'name': 'name',
        'icon_url': 'iconUrl',
        'material_icon': 'materialIcon',
        'iframe_url': 'iframeUrl',
        'dashboard_id': 'dashboardId',
        'hide_dashboard_toolbar': 'hideDashboardToolbar',
        'set_access_token': 'setAccessToken',
        'child_menu_items': 'childMenuItems'
    }

    def __init__(self, name=None, icon_url=None, material_icon=None, iframe_url=None, dashboard_id=None, hide_dashboard_toolbar=None, set_access_token=None, child_menu_items=None):  # noqa: E501
        """CustomMenuItem - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._icon_url = None
        self._material_icon = None
        self._iframe_url = None
        self._dashboard_id = None
        self._hide_dashboard_toolbar = None
        self._set_access_token = None
        self._child_menu_items = None
        self.discriminator = None
        self.name = name
        if icon_url is not None:
            self.icon_url = icon_url
        if material_icon is not None:
            self.material_icon = material_icon
        if iframe_url is not None:
            self.iframe_url = iframe_url
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if hide_dashboard_toolbar is not None:
            self.hide_dashboard_toolbar = hide_dashboard_toolbar
        if set_access_token is not None:
            self.set_access_token = set_access_token
        if child_menu_items is not None:
            self.child_menu_items = child_menu_items

    @property
    def name(self):
        """Gets the name of this CustomMenuItem.  # noqa: E501

        Name of the menu item  # noqa: E501

        :return: The name of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomMenuItem.

        Name of the menu item  # noqa: E501

        :param name: The name of this CustomMenuItem.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def icon_url(self):
        """Gets the icon_url of this CustomMenuItem.  # noqa: E501

        URL of the menu item icon. Overrides 'materialIcon'  # noqa: E501

        :return: The icon_url of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this CustomMenuItem.

        URL of the menu item icon. Overrides 'materialIcon'  # noqa: E501

        :param icon_url: The icon_url of this CustomMenuItem.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def material_icon(self):
        """Gets the material_icon of this CustomMenuItem.  # noqa: E501

        Material icon name. See [Material Icons](https://fonts.google.com/icons?selected=Material+Icons) for examples  # noqa: E501

        :return: The material_icon of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._material_icon

    @material_icon.setter
    def material_icon(self, material_icon):
        """Sets the material_icon of this CustomMenuItem.

        Material icon name. See [Material Icons](https://fonts.google.com/icons?selected=Material+Icons) for examples  # noqa: E501

        :param material_icon: The material_icon of this CustomMenuItem.  # noqa: E501
        :type: str
        """

        self._material_icon = material_icon

    @property
    def iframe_url(self):
        """Gets the iframe_url of this CustomMenuItem.  # noqa: E501

        URL to open in the iframe, when user clicks the menu item  # noqa: E501

        :return: The iframe_url of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._iframe_url

    @iframe_url.setter
    def iframe_url(self, iframe_url):
        """Sets the iframe_url of this CustomMenuItem.

        URL to open in the iframe, when user clicks the menu item  # noqa: E501

        :param iframe_url: The iframe_url of this CustomMenuItem.  # noqa: E501
        :type: str
        """

        self._iframe_url = iframe_url

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this CustomMenuItem.  # noqa: E501

        Id of the Dashboard to open, when user clicks the menu item  # noqa: E501

        :return: The dashboard_id of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this CustomMenuItem.

        Id of the Dashboard to open, when user clicks the menu item  # noqa: E501

        :param dashboard_id: The dashboard_id of this CustomMenuItem.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def hide_dashboard_toolbar(self):
        """Gets the hide_dashboard_toolbar of this CustomMenuItem.  # noqa: E501

        Hide the dashboard toolbar  # noqa: E501

        :return: The hide_dashboard_toolbar of this CustomMenuItem.  # noqa: E501
        :rtype: bool
        """
        return self._hide_dashboard_toolbar

    @hide_dashboard_toolbar.setter
    def hide_dashboard_toolbar(self, hide_dashboard_toolbar):
        """Sets the hide_dashboard_toolbar of this CustomMenuItem.

        Hide the dashboard toolbar  # noqa: E501

        :param hide_dashboard_toolbar: The hide_dashboard_toolbar of this CustomMenuItem.  # noqa: E501
        :type: bool
        """

        self._hide_dashboard_toolbar = hide_dashboard_toolbar

    @property
    def set_access_token(self):
        """Gets the set_access_token of this CustomMenuItem.  # noqa: E501

        Set the access token of the current user to a new dashboard  # noqa: E501

        :return: The set_access_token of this CustomMenuItem.  # noqa: E501
        :rtype: bool
        """
        return self._set_access_token

    @set_access_token.setter
    def set_access_token(self, set_access_token):
        """Sets the set_access_token of this CustomMenuItem.

        Set the access token of the current user to a new dashboard  # noqa: E501

        :param set_access_token: The set_access_token of this CustomMenuItem.  # noqa: E501
        :type: bool
        """

        self._set_access_token = set_access_token

    @property
    def child_menu_items(self):
        """Gets the child_menu_items of this CustomMenuItem.  # noqa: E501

        List of child menu items  # noqa: E501

        :return: The child_menu_items of this CustomMenuItem.  # noqa: E501
        :rtype: list[CustomMenuItem]
        """
        return self._child_menu_items

    @child_menu_items.setter
    def child_menu_items(self, child_menu_items):
        """Sets the child_menu_items of this CustomMenuItem.

        List of child menu items  # noqa: E501

        :param child_menu_items: The child_menu_items of this CustomMenuItem.  # noqa: E501
        :type: list[CustomMenuItem]
        """

        self._child_menu_items = child_menu_items

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
        if issubclass(CustomMenuItem, dict):
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
        if not isinstance(other, CustomMenuItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
