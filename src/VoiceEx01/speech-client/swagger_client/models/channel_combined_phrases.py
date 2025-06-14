# coding: utf-8

"""
    Speech Services API version 2024-11-15

    Speech Services API version 2024-11-15.  # noqa: E501

    OpenAPI spec version: 2024-11-15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ChannelCombinedPhrases(object):
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
        'channel': 'int',
        'text': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'text': 'text'
    }

    def __init__(self, channel=None, text=None, _configuration=None):  # noqa: E501
        """ChannelCombinedPhrases - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._channel = None
        self._text = None
        self.discriminator = None

        if channel is not None:
            self.channel = channel
        self.text = text

    @property
    def channel(self):
        """Gets the channel of this ChannelCombinedPhrases.  # noqa: E501

        The 0-based channel index. Only present if channel separation is enabled.  # noqa: E501

        :return: The channel of this ChannelCombinedPhrases.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelCombinedPhrases.

        The 0-based channel index. Only present if channel separation is enabled.  # noqa: E501

        :param channel: The channel of this ChannelCombinedPhrases.  # noqa: E501
        :type: int
        """

        self._channel = channel

    @property
    def text(self):
        """Gets the text of this ChannelCombinedPhrases.  # noqa: E501

        The transcribed text.  # noqa: E501

        :return: The text of this ChannelCombinedPhrases.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ChannelCombinedPhrases.

        The transcribed text.  # noqa: E501

        :param text: The text of this ChannelCombinedPhrases.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if issubclass(ChannelCombinedPhrases, dict):
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
        if not isinstance(other, ChannelCombinedPhrases):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelCombinedPhrases):
            return True

        return self.to_dict() != other.to_dict()
