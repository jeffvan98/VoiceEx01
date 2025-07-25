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


class UploadedBlocks(object):
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
        'committed_blocks': 'list[ResponseBlock]',
        'uncommitted_blocks': 'list[ResponseBlock]'
    }

    attribute_map = {
        'committed_blocks': 'committedBlocks',
        'uncommitted_blocks': 'uncommittedBlocks'
    }

    def __init__(self, committed_blocks=None, uncommitted_blocks=None, _configuration=None):  # noqa: E501
        """UploadedBlocks - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._committed_blocks = None
        self._uncommitted_blocks = None
        self.discriminator = None

        if committed_blocks is not None:
            self.committed_blocks = committed_blocks
        if uncommitted_blocks is not None:
            self.uncommitted_blocks = uncommitted_blocks

    @property
    def committed_blocks(self):
        """Gets the committed_blocks of this UploadedBlocks.  # noqa: E501

        The block description of blocks already committed.  # noqa: E501

        :return: The committed_blocks of this UploadedBlocks.  # noqa: E501
        :rtype: list[ResponseBlock]
        """
        return self._committed_blocks

    @committed_blocks.setter
    def committed_blocks(self, committed_blocks):
        """Sets the committed_blocks of this UploadedBlocks.

        The block description of blocks already committed.  # noqa: E501

        :param committed_blocks: The committed_blocks of this UploadedBlocks.  # noqa: E501
        :type: list[ResponseBlock]
        """

        self._committed_blocks = committed_blocks

    @property
    def uncommitted_blocks(self):
        """Gets the uncommitted_blocks of this UploadedBlocks.  # noqa: E501

        The block description of blocks not committed to the blob.  # noqa: E501

        :return: The uncommitted_blocks of this UploadedBlocks.  # noqa: E501
        :rtype: list[ResponseBlock]
        """
        return self._uncommitted_blocks

    @uncommitted_blocks.setter
    def uncommitted_blocks(self, uncommitted_blocks):
        """Sets the uncommitted_blocks of this UploadedBlocks.

        The block description of blocks not committed to the blob.  # noqa: E501

        :param uncommitted_blocks: The uncommitted_blocks of this UploadedBlocks.  # noqa: E501
        :type: list[ResponseBlock]
        """

        self._uncommitted_blocks = uncommitted_blocks

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
        if issubclass(UploadedBlocks, dict):
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
        if not isinstance(other, UploadedBlocks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadedBlocks):
            return True

        return self.to_dict() != other.to_dict()
