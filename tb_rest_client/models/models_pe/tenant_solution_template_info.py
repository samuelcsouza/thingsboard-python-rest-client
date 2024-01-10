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

class TenantSolutionTemplateInfo(object):
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
        'id': 'str',
        'title': 'str',
        'level': 'str',
        'install_timeout_ms': 'int',
        'tenant_telemetry_keys': 'list[str]',
        'tenant_attribute_keys': 'list[str]',
        'preview_image_url': 'str',
        'short_description': 'str',
        'installed': 'bool',
        'video_preview_image_url': 'str',
        'preview_mp4_url': 'str',
        'preview_webm_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'level': 'level',
        'install_timeout_ms': 'installTimeoutMs',
        'tenant_telemetry_keys': 'tenantTelemetryKeys',
        'tenant_attribute_keys': 'tenantAttributeKeys',
        'preview_image_url': 'previewImageUrl',
        'short_description': 'shortDescription',
        'installed': 'installed',
        'video_preview_image_url': 'videoPreviewImageUrl',
        'preview_mp4_url': 'previewMp4Url',
        'preview_webm_url': 'previewWebmUrl'
    }

    def __init__(self, id=None, title=None, level=None, install_timeout_ms=None, tenant_telemetry_keys=None, tenant_attribute_keys=None, preview_image_url=None, short_description=None, installed=None, video_preview_image_url=None, preview_mp4_url=None, preview_webm_url=None):  # noqa: E501
        """TenantSolutionTemplateInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._level = None
        self._install_timeout_ms = None
        self._tenant_telemetry_keys = None
        self._tenant_attribute_keys = None
        self._preview_image_url = None
        self._short_description = None
        self._installed = None
        self._video_preview_image_url = None
        self._preview_mp4_url = None
        self._preview_webm_url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if level is not None:
            self.level = level
        if install_timeout_ms is not None:
            self.install_timeout_ms = install_timeout_ms
        if tenant_telemetry_keys is not None:
            self.tenant_telemetry_keys = tenant_telemetry_keys
        if tenant_attribute_keys is not None:
            self.tenant_attribute_keys = tenant_attribute_keys
        if preview_image_url is not None:
            self.preview_image_url = preview_image_url
        if short_description is not None:
            self.short_description = short_description
        if installed is not None:
            self.installed = installed
        if video_preview_image_url is not None:
            self.video_preview_image_url = video_preview_image_url
        if preview_mp4_url is not None:
            self.preview_mp4_url = preview_mp4_url
        if preview_webm_url is not None:
            self.preview_webm_url = preview_webm_url

    @property
    def id(self):
        """Gets the id of this TenantSolutionTemplateInfo.  # noqa: E501

        ID of the solution template  # noqa: E501

        :return: The id of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantSolutionTemplateInfo.

        ID of the solution template  # noqa: E501

        :param id: The id of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this TenantSolutionTemplateInfo.  # noqa: E501

        Template Title  # noqa: E501

        :return: The title of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TenantSolutionTemplateInfo.

        Template Title  # noqa: E501

        :param title: The title of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def level(self):
        """Gets the level of this TenantSolutionTemplateInfo.  # noqa: E501

        Level of the subscription that is required to unlock the template  # noqa: E501

        :return: The level of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this TenantSolutionTemplateInfo.

        Level of the subscription that is required to unlock the template  # noqa: E501

        :param level: The level of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["MAKER", "PROTOTYPE", "STARTUP"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                .format(level, allowed_values)
            )

        self._level = level

    @property
    def install_timeout_ms(self):
        """Gets the install_timeout_ms of this TenantSolutionTemplateInfo.  # noqa: E501

        Timeout for the installation UI to wait while template is installing  # noqa: E501

        :return: The install_timeout_ms of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: int
        """
        return self._install_timeout_ms

    @install_timeout_ms.setter
    def install_timeout_ms(self, install_timeout_ms):
        """Sets the install_timeout_ms of this TenantSolutionTemplateInfo.

        Timeout for the installation UI to wait while template is installing  # noqa: E501

        :param install_timeout_ms: The install_timeout_ms of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: int
        """

        self._install_timeout_ms = install_timeout_ms

    @property
    def tenant_telemetry_keys(self):
        """Gets the tenant_telemetry_keys of this TenantSolutionTemplateInfo.  # noqa: E501

        What keys to delete during template uninstall  # noqa: E501

        :return: The tenant_telemetry_keys of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant_telemetry_keys

    @tenant_telemetry_keys.setter
    def tenant_telemetry_keys(self, tenant_telemetry_keys):
        """Sets the tenant_telemetry_keys of this TenantSolutionTemplateInfo.

        What keys to delete during template uninstall  # noqa: E501

        :param tenant_telemetry_keys: The tenant_telemetry_keys of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: list[str]
        """

        self._tenant_telemetry_keys = tenant_telemetry_keys

    @property
    def tenant_attribute_keys(self):
        """Gets the tenant_attribute_keys of this TenantSolutionTemplateInfo.  # noqa: E501

        What attributes to delete during template uninstall  # noqa: E501

        :return: The tenant_attribute_keys of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant_attribute_keys

    @tenant_attribute_keys.setter
    def tenant_attribute_keys(self, tenant_attribute_keys):
        """Sets the tenant_attribute_keys of this TenantSolutionTemplateInfo.

        What attributes to delete during template uninstall  # noqa: E501

        :param tenant_attribute_keys: The tenant_attribute_keys of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: list[str]
        """

        self._tenant_attribute_keys = tenant_attribute_keys

    @property
    def preview_image_url(self):
        """Gets the preview_image_url of this TenantSolutionTemplateInfo.  # noqa: E501

        URL of the preview image  # noqa: E501

        :return: The preview_image_url of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._preview_image_url

    @preview_image_url.setter
    def preview_image_url(self, preview_image_url):
        """Sets the preview_image_url of this TenantSolutionTemplateInfo.

        URL of the preview image  # noqa: E501

        :param preview_image_url: The preview_image_url of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: str
        """

        self._preview_image_url = preview_image_url

    @property
    def short_description(self):
        """Gets the short_description of this TenantSolutionTemplateInfo.  # noqa: E501

        Short description to display on template card  # noqa: E501

        :return: The short_description of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this TenantSolutionTemplateInfo.

        Short description to display on template card  # noqa: E501

        :param short_description: The short_description of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def installed(self):
        """Gets the installed of this TenantSolutionTemplateInfo.  # noqa: E501

        Indicates that template is already installed for the current tenant  # noqa: E501

        :return: The installed of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: bool
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        """Sets the installed of this TenantSolutionTemplateInfo.

        Indicates that template is already installed for the current tenant  # noqa: E501

        :param installed: The installed of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: bool
        """

        self._installed = installed

    @property
    def video_preview_image_url(self):
        """Gets the video_preview_image_url of this TenantSolutionTemplateInfo.  # noqa: E501

        Video preview image URL  # noqa: E501

        :return: The video_preview_image_url of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._video_preview_image_url

    @video_preview_image_url.setter
    def video_preview_image_url(self, video_preview_image_url):
        """Sets the video_preview_image_url of this TenantSolutionTemplateInfo.

        Video preview image URL  # noqa: E501

        :param video_preview_image_url: The video_preview_image_url of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: str
        """

        self._video_preview_image_url = video_preview_image_url

    @property
    def preview_mp4_url(self):
        """Gets the preview_mp4_url of this TenantSolutionTemplateInfo.  # noqa: E501

        Video MP4 URL  # noqa: E501

        :return: The preview_mp4_url of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._preview_mp4_url

    @preview_mp4_url.setter
    def preview_mp4_url(self, preview_mp4_url):
        """Sets the preview_mp4_url of this TenantSolutionTemplateInfo.

        Video MP4 URL  # noqa: E501

        :param preview_mp4_url: The preview_mp4_url of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: str
        """

        self._preview_mp4_url = preview_mp4_url

    @property
    def preview_webm_url(self):
        """Gets the preview_webm_url of this TenantSolutionTemplateInfo.  # noqa: E501

        Video WEBM URL  # noqa: E501

        :return: The preview_webm_url of this TenantSolutionTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._preview_webm_url

    @preview_webm_url.setter
    def preview_webm_url(self, preview_webm_url):
        """Sets the preview_webm_url of this TenantSolutionTemplateInfo.

        Video WEBM URL  # noqa: E501

        :param preview_webm_url: The preview_webm_url of this TenantSolutionTemplateInfo.  # noqa: E501
        :type: str
        """

        self._preview_webm_url = preview_webm_url

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
        if issubclass(TenantSolutionTemplateInfo, dict):
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
        if not isinstance(other, TenantSolutionTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
