# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class NullValue(enum.IntEnum):
    """
    ``NullValue`` is a singleton enumeration to represent the null value
    for the ``Value`` type union.

    The JSON representation for ``NullValue`` is JSON ``null``.

    Attributes:
      NULL_VALUE (int): Null value.
    """

    NULL_VALUE = 0


class Impact(object):
    class Category(enum.IntEnum):
        """
        The category of the impact.

        Attributes:
          CATEGORY_UNSPECIFIED (int): Default unspecified category. Don't use directly.
          COST (int): Indicates a potential increase or decrease in cost.
          SECURITY (int): Indicates a potential increase or decrease in security.
          PERFORMANCE (int): Indicates a potential increase or decrease in performance.
          MANAGEABILITY (int): Indicates a potential increase or decrease in manageability.
        """

        CATEGORY_UNSPECIFIED = 0
        COST = 1
        SECURITY = 2
        PERFORMANCE = 3
        MANAGEABILITY = 4


class Insight(object):
    class Category(enum.IntEnum):
        """
        Insight category.

        Attributes:
          CATEGORY_UNSPECIFIED (int): Unspecified category.
          COST (int): The insight is related to cost.
          SECURITY (int): The insight is related to security.
          PERFORMANCE (int): The insight is related to performance.
          MANAGEABILITY (int): This insight is related to manageability.
        """

        CATEGORY_UNSPECIFIED = 0
        COST = 1
        SECURITY = 2
        PERFORMANCE = 3
        MANAGEABILITY = 4


class InsightStateInfo(object):
    class State(enum.IntEnum):
        """
        Represents insight state.

        Attributes:
          STATE_UNSPECIFIED (int): Unspecified state.
          ACTIVE (int): Insight is active. Content for ACTIVE insights can be updated by Google.
          ACTIVE insights can be marked DISMISSED OR ACCEPTED.
          ACCEPTED (int): Some action has been taken based on this insight. Insights become
          accepted when a recommendation derived from the insight has been marked
          CLAIMED, SUCCEEDED, or FAILED. ACTIVE insights can also be marked
          ACCEPTED explicitly. Content for ACCEPTED insights is immutable. ACCEPTED
          insights can only be marked ACCEPTED (which may update state metadata).
          DISMISSED (int): Insight is dismissed. Content for DISMISSED insights can be updated by
          Google. DISMISSED insights can be marked as ACTIVE.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        ACCEPTED = 2
        DISMISSED = 3


class RecommendationStateInfo(object):
    class State(enum.IntEnum):
        """
        Represents Recommendation State.

        Attributes:
          STATE_UNSPECIFIED (int): Default state. Don't use directly.
          ACTIVE (int): Recommendation is active and can be applied. Recommendations content can
          be updated by Google.

          ACTIVE recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED.
          CLAIMED (int): Recommendation is in claimed state. Recommendations content is
          immutable and cannot be updated by Google.

          CLAIMED recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED.
          SUCCEEDED (int): Recommendation is in succeeded state. Recommendations content is
          immutable and cannot be updated by Google.

          SUCCEEDED recommendations can be marked as SUCCEEDED, or FAILED.
          FAILED (int): Recommendation is in failed state. Recommendations content is immutable
          and cannot be updated by Google.

          FAILED recommendations can be marked as SUCCEEDED, or FAILED.
          DISMISSED (int): Recommendation is in dismissed state. Recommendation content can be
          updated by Google.

          DISMISSED recommendations can be marked as ACTIVE.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CLAIMED = 6
        SUCCEEDED = 3
        FAILED = 4
        DISMISSED = 5
