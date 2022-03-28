# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.cloud.recommender_v1beta1.types import insight
from google.cloud.recommender_v1beta1.types import (
    insight_type_config as gcr_insight_type_config,
)
from google.cloud.recommender_v1beta1.types import recommendation
from google.cloud.recommender_v1beta1.types import (
    recommender_config as gcr_recommender_config,
)
from google.protobuf import field_mask_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.recommender.v1beta1",
    manifest={
        "ListInsightsRequest",
        "ListInsightsResponse",
        "GetInsightRequest",
        "MarkInsightAcceptedRequest",
        "ListRecommendationsRequest",
        "ListRecommendationsResponse",
        "GetRecommendationRequest",
        "MarkRecommendationClaimedRequest",
        "MarkRecommendationSucceededRequest",
        "MarkRecommendationFailedRequest",
        "GetRecommenderConfigRequest",
        "UpdateRecommenderConfigRequest",
        "GetInsightTypeConfigRequest",
        "UpdateInsightTypeConfigRequest",
    },
)


class ListInsightsRequest(proto.Message):
    r"""Request for the ``ListInsights`` method.

    Attributes:
        parent (str):
            Required. The container resource on which to execute the
            request. Acceptable formats:

            -  ``projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

            -  ``projects/[PROJECT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

            -  ``billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

            -  ``folders/[FOLDER_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

            -  ``organizations/[ORGANIZATION_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

            LOCATION here refers to GCP Locations:
            https://cloud.google.com/about/locations/ INSIGHT_TYPE_ID
            refers to supported insight types:
            https://cloud.google.com/recommender/docs/insights/insight-types.
        page_size (int):
            Optional. The maximum number of results to
            return from this request.  Non-positive values
            are ignored. If not specified, the server will
            determine the number of results to return.
        page_token (str):
            Optional. If present, retrieves the next batch of results
            from the preceding call to this method. ``page_token`` must
            be the value of ``next_page_token`` from the previous
            response. The values of other method parameters must be
            identical to those in the previous call.
        filter (str):
            Optional. Filter expression to restrict the insights
            returned. Supported filter fields:

            -  ``stateInfo.state``

            -  ``insightSubtype``

            -  ``severity``

            Examples:

            -  ``stateInfo.state = ACTIVE OR stateInfo.state = DISMISSED``

            -  ``insightSubtype = PERMISSIONS_USAGE``

            -  ``severity = CRITICAL OR severity = HIGH``

            -  ``stateInfo.state = ACTIVE AND (severity = CRITICAL OR severity = HIGH)``

            (These expressions are based on the filter language
            described at https://google.aip.dev/160)
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )
    filter = proto.Field(
        proto.STRING,
        number=4,
    )


class ListInsightsResponse(proto.Message):
    r"""Response to the ``ListInsights`` method.

    Attributes:
        insights (Sequence[google.cloud.recommender_v1beta1.types.Insight]):
            The set of insights for the ``parent`` resource.
        next_page_token (str):
            A token that can be used to request the next
            page of results. This field is empty if there
            are no additional results.
    """

    @property
    def raw_page(self):
        return self

    insights = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=insight.Insight,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInsightRequest(proto.Message):
    r"""Request to the ``GetInsight`` method.

    Attributes:
        name (str):
            Required. Name of the insight.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class MarkInsightAcceptedRequest(proto.Message):
    r"""Request for the ``MarkInsightAccepted`` method.

    Attributes:
        name (str):
            Required. Name of the insight.
        state_metadata (Sequence[google.cloud.recommender_v1beta1.types.MarkInsightAcceptedRequest.StateMetadataEntry]):
            Optional. State properties user wish to include with this
            state. Full replace of the current state_metadata.
        etag (str):
            Required. Fingerprint of the Insight.
            Provides optimistic locking.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    state_metadata = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    etag = proto.Field(
        proto.STRING,
        number=3,
    )


class ListRecommendationsRequest(proto.Message):
    r"""Request for the ``ListRecommendations`` method.

    Attributes:
        parent (str):
            Required. The container resource on which to execute the
            request. Acceptable formats:

            -  ``projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]``

            -  ``projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]``

            -  ``billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]``

            -  ``folders/[FOLDER_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]``

            -  ``organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]``

            LOCATION here refers to GCP Locations:
            https://cloud.google.com/about/locations/ RECOMMENDER_ID
            refers to supported recommenders:
            https://cloud.google.com/recommender/docs/recommenders.
        page_size (int):
            Optional. The maximum number of results to
            return from this request.  Non-positive values
            are ignored. If not specified, the server will
            determine the number of results to return.
        page_token (str):
            Optional. If present, retrieves the next batch of results
            from the preceding call to this method. ``page_token`` must
            be the value of ``next_page_token`` from the previous
            response. The values of other method parameters must be
            identical to those in the previous call.
        filter (str):
            Filter expression to restrict the recommendations returned.
            Supported filter fields:

            -  ``state_info.state``

            -  ``recommenderSubtype``

            -  ``priority``

            Examples:

            -  ``stateInfo.state = ACTIVE OR stateInfo.state = DISMISSED``

            -  ``recommenderSubtype = REMOVE_ROLE OR recommenderSubtype = REPLACE_ROLE``

            -  ``priority = P1 OR priority = P2``

            -  ``stateInfo.state = ACTIVE AND (priority = P1 OR priority = P2)``

            (These expressions are based on the filter language
            described at https://google.aip.dev/160)
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )
    filter = proto.Field(
        proto.STRING,
        number=5,
    )


class ListRecommendationsResponse(proto.Message):
    r"""Response to the ``ListRecommendations`` method.

    Attributes:
        recommendations (Sequence[google.cloud.recommender_v1beta1.types.Recommendation]):
            The set of recommendations for the ``parent`` resource.
        next_page_token (str):
            A token that can be used to request the next
            page of results. This field is empty if there
            are no additional results.
    """

    @property
    def raw_page(self):
        return self

    recommendations = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=recommendation.Recommendation,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class GetRecommendationRequest(proto.Message):
    r"""Request to the ``GetRecommendation`` method.

    Attributes:
        name (str):
            Required. Name of the recommendation.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class MarkRecommendationClaimedRequest(proto.Message):
    r"""Request for the ``MarkRecommendationClaimed`` Method.

    Attributes:
        name (str):
            Required. Name of the recommendation.
        state_metadata (Sequence[google.cloud.recommender_v1beta1.types.MarkRecommendationClaimedRequest.StateMetadataEntry]):
            State properties to include with this state. Overwrites any
            existing ``state_metadata``. Keys must match the regex
            ``/^[a-z0-9][a-z0-9_.-]{0,62}$/``. Values must match the
            regex ``/^[a-zA-Z0-9_./-]{0,255}$/``.
        etag (str):
            Required. Fingerprint of the Recommendation.
            Provides optimistic locking.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    state_metadata = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    etag = proto.Field(
        proto.STRING,
        number=3,
    )


class MarkRecommendationSucceededRequest(proto.Message):
    r"""Request for the ``MarkRecommendationSucceeded`` Method.

    Attributes:
        name (str):
            Required. Name of the recommendation.
        state_metadata (Sequence[google.cloud.recommender_v1beta1.types.MarkRecommendationSucceededRequest.StateMetadataEntry]):
            State properties to include with this state. Overwrites any
            existing ``state_metadata``. Keys must match the regex
            ``/^[a-z0-9][a-z0-9_.-]{0,62}$/``. Values must match the
            regex ``/^[a-zA-Z0-9_./-]{0,255}$/``.
        etag (str):
            Required. Fingerprint of the Recommendation.
            Provides optimistic locking.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    state_metadata = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    etag = proto.Field(
        proto.STRING,
        number=3,
    )


class MarkRecommendationFailedRequest(proto.Message):
    r"""Request for the ``MarkRecommendationFailed`` Method.

    Attributes:
        name (str):
            Required. Name of the recommendation.
        state_metadata (Sequence[google.cloud.recommender_v1beta1.types.MarkRecommendationFailedRequest.StateMetadataEntry]):
            State properties to include with this state. Overwrites any
            existing ``state_metadata``. Keys must match the regex
            ``/^[a-z0-9][a-z0-9_.-]{0,62}$/``. Values must match the
            regex ``/^[a-zA-Z0-9_./-]{0,255}$/``.
        etag (str):
            Required. Fingerprint of the Recommendation.
            Provides optimistic locking.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    state_metadata = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    etag = proto.Field(
        proto.STRING,
        number=3,
    )


class GetRecommenderConfigRequest(proto.Message):
    r"""Request for the GetRecommenderConfig\` method.

    Attributes:
        name (str):
            Required. Name of the Recommendation Config to get.

            Acceptable formats:

            -  ``projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config``

            -  ``projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config``

            -  ``organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config``
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRecommenderConfigRequest(proto.Message):
    r"""Request for the ``UpdateRecommenderConfig`` method.

    Attributes:
        recommender_config (google.cloud.recommender_v1beta1.types.RecommenderConfig):
            Required. The RecommenderConfig to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
        validate_only (bool):
            If true, validate the request and preview the
            change, but do not actually update it.
    """

    recommender_config = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_recommender_config.RecommenderConfig,
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetInsightTypeConfigRequest(proto.Message):
    r"""Request for the GetInsightTypeConfig\` method.

    Attributes:
        name (str):
            Required. Name of the InsightTypeConfig to get.

            Acceptable formats:

            -  ``projects/[PROJECT_NUMBER]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config``

            -  ``projects/[PROJECT_ID]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config``

            -  ``organizations/[ORGANIZATION_ID]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config``
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateInsightTypeConfigRequest(proto.Message):
    r"""Request for the ``UpdateInsightTypeConfig`` method.

    Attributes:
        insight_type_config (google.cloud.recommender_v1beta1.types.InsightTypeConfig):
            Required. The InsightTypeConfig to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
        validate_only (bool):
            If true, validate the request and preview the
            change, but do not actually update it.
    """

    insight_type_config = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_insight_type_config.InsightTypeConfig,
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
