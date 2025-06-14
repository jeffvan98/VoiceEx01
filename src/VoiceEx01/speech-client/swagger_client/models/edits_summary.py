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


class EditsSummary(object):
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
        'number_of_edits': 'int',
        'percentage_of_all_edits': 'float'
    }

    attribute_map = {
        'number_of_edits': 'numberOfEdits',
        'percentage_of_all_edits': 'percentageOfAllEdits'
    }

    def __init__(self, number_of_edits=None, percentage_of_all_edits=None, _configuration=None):  # noqa: E501
        """EditsSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._number_of_edits = None
        self._percentage_of_all_edits = None
        self.discriminator = None

        if number_of_edits is not None:
            self.number_of_edits = number_of_edits
        if percentage_of_all_edits is not None:
            self.percentage_of_all_edits = percentage_of_all_edits

    @property
    def number_of_edits(self):
        """Gets the number_of_edits of this EditsSummary.  # noqa: E501

        The optional number of edits for a given type of error of the recognized transcription in comparison with the human transcription.  # noqa: E501

        :return: The number_of_edits of this EditsSummary.  # noqa: E501
        :rtype: int
        """
        return self._number_of_edits

    @number_of_edits.setter
    def number_of_edits(self, number_of_edits):
        """Sets the number_of_edits of this EditsSummary.

        The optional number of edits for a given type of error of the recognized transcription in comparison with the human transcription.  # noqa: E501

        :param number_of_edits: The number_of_edits of this EditsSummary.  # noqa: E501
        :type: int
        """

        self._number_of_edits = number_of_edits

    @property
    def percentage_of_all_edits(self):
        """Gets the percentage_of_all_edits of this EditsSummary.  # noqa: E501

        The optional percentage of edits for a given type of error of the recognized transcription in comparison with the human transcription.  # noqa: E501

        :return: The percentage_of_all_edits of this EditsSummary.  # noqa: E501
        :rtype: float
        """
        return self._percentage_of_all_edits

    @percentage_of_all_edits.setter
    def percentage_of_all_edits(self, percentage_of_all_edits):
        """Sets the percentage_of_all_edits of this EditsSummary.

        The optional percentage of edits for a given type of error of the recognized transcription in comparison with the human transcription.  # noqa: E501

        :param percentage_of_all_edits: The percentage_of_all_edits of this EditsSummary.  # noqa: E501
        :type: float
        """

        self._percentage_of_all_edits = percentage_of_all_edits

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
        if issubclass(EditsSummary, dict):
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
        if not isinstance(other, EditsSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EditsSummary):
            return True

        return self.to_dict() != other.to_dict()
