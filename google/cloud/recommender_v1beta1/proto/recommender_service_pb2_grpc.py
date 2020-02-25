# Copyright 2019 Google LLC
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

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!

import grpc

from google.cloud.recommender_v1beta1.proto import (
    recommendation_pb2 as google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2,
)
from google.cloud.recommender_v1beta1.proto import (
    recommender_service_pb2 as google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2,
)


class RecommenderStub(object):
    """Provides insights and recommendations for cloud customers for various
  categories like performance optimization, cost savings, reliability, feature
  discovery, etc. Insights and recommendations are generated automatically
  based on analysis of user resources, configuration and monitoring metrics.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.ListRecommendations = channel.unary_unary(
            "/google.cloud.recommender.v1beta1.Recommender/ListRecommendations",
            request_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.ListRecommendationsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.ListRecommendationsResponse.FromString,
        )
        self.GetRecommendation = channel.unary_unary(
            "/google.cloud.recommender.v1beta1.Recommender/GetRecommendation",
            request_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.GetRecommendationRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2.Recommendation.FromString,
        )
        self.MarkRecommendationClaimed = channel.unary_unary(
            "/google.cloud.recommender.v1beta1.Recommender/MarkRecommendationClaimed",
            request_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.MarkRecommendationClaimedRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2.Recommendation.FromString,
        )
        self.MarkRecommendationSucceeded = channel.unary_unary(
            "/google.cloud.recommender.v1beta1.Recommender/MarkRecommendationSucceeded",
            request_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.MarkRecommendationSucceededRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2.Recommendation.FromString,
        )
        self.MarkRecommendationFailed = channel.unary_unary(
            "/google.cloud.recommender.v1beta1.Recommender/MarkRecommendationFailed",
            request_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.MarkRecommendationFailedRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2.Recommendation.FromString,
        )


class RecommenderServicer(object):
    """Provides insights and recommendations for cloud customers for various
  categories like performance optimization, cost savings, reliability, feature
  discovery, etc. Insights and recommendations are generated automatically
  based on analysis of user resources, configuration and monitoring metrics.
  """

    def ListRecommendations(self, request, context):
        """Lists recommendations for a Cloud project. Requires the recommender.*.list
    IAM permission for the specified recommender.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRecommendation(self, request, context):
        """Gets the requested recommendation. Requires the recommender.*.get
    IAM permission for the specified recommender.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MarkRecommendationClaimed(self, request, context):
        """Marks the Recommendation State as Claimed. Users can use this method to
    indicate to the Recommender API that they are starting to apply the
    recommendation themselves. This stops the recommendation content from being
    updated. Associated insights are frozen and placed in the ACCEPTED state.

    MarkRecommendationClaimed can be applied to recommendations in CLAIMED or
    ACTIVE state.

    Requires the recommender.*.update IAM permission for the specified
    recommender.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MarkRecommendationSucceeded(self, request, context):
        """Marks the Recommendation State as Succeeded. Users can use this method to
    indicate to the Recommender API that they have applied the recommendation
    themselves, and the operation was successful. This stops the recommendation
    content from being updated. Associated insights are frozen and placed in
    the ACCEPTED state.

    MarkRecommendationSucceeded can be applied to recommendations in ACTIVE,
    CLAIMED, SUCCEEDED, or FAILED state.

    Requires the recommender.*.update IAM permission for the specified
    recommender.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def MarkRecommendationFailed(self, request, context):
        """Marks the Recommendation State as Failed. Users can use this method to
    indicate to the Recommender API that they have applied the recommendation
    themselves, and the operation failed. This stops the recommendation content
    from being updated. Associated insights are frozen and placed in the
    ACCEPTED state.

    MarkRecommendationFailed can be applied to recommendations in ACTIVE,
    CLAIMED, SUCCEEDED, or FAILED state.

    Requires the recommender.*.update IAM permission for the specified
    recommender.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RecommenderServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListRecommendations": grpc.unary_unary_rpc_method_handler(
            servicer.ListRecommendations,
            request_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.ListRecommendationsRequest.FromString,
            response_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.ListRecommendationsResponse.SerializeToString,
        ),
        "GetRecommendation": grpc.unary_unary_rpc_method_handler(
            servicer.GetRecommendation,
            request_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.GetRecommendationRequest.FromString,
            response_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2.Recommendation.SerializeToString,
        ),
        "MarkRecommendationClaimed": grpc.unary_unary_rpc_method_handler(
            servicer.MarkRecommendationClaimed,
            request_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.MarkRecommendationClaimedRequest.FromString,
            response_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2.Recommendation.SerializeToString,
        ),
        "MarkRecommendationSucceeded": grpc.unary_unary_rpc_method_handler(
            servicer.MarkRecommendationSucceeded,
            request_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.MarkRecommendationSucceededRequest.FromString,
            response_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2.Recommendation.SerializeToString,
        ),
        "MarkRecommendationFailed": grpc.unary_unary_rpc_method_handler(
            servicer.MarkRecommendationFailed,
            request_deserializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommender__service__pb2.MarkRecommendationFailedRequest.FromString,
            response_serializer=google_dot_cloud_dot_recommender__v1beta1_dot_proto_dot_recommendation__pb2.Recommendation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.recommender.v1beta1.Recommender", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
