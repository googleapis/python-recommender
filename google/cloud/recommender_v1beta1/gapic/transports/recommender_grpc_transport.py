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


import google.api_core.grpc_helpers

from google.cloud.recommender_v1beta1.proto import recommender_service_pb2_grpc


class RecommenderGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.recommender.v1beta1 Recommender API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self, channel=None, credentials=None, address="recommender.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "recommender_stub": recommender_service_pb2_grpc.RecommenderStub(channel)
        }

    @classmethod
    def create_channel(
        cls, address="recommender.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def list_recommendations(self):
        """Return the gRPC stub for :meth:`RecommenderClient.list_recommendations`.

        Value for the ``path`` field. Will be set for
        actions:'add'/'replace'. Maybe set for action: 'test'. Either this or
        ``value_matcher`` will be set for 'test' operation. An exact match must
        be performed.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].ListRecommendations

    @property
    def get_recommendation(self):
        """Return the gRPC stub for :meth:`RecommenderClient.get_recommendation`.

        The resource type of a child collection that the annotated field
        references. This is useful for annotating the ``parent`` field that
        doesn't have a fixed resource type.

        Example:

        message ListLogEntriesRequest { string parent = 1
        [(google.api.resource_reference) = { child_type:
        "logging.googleapis.com/LogEntry" }; }

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].GetRecommendation

    @property
    def mark_recommendation_claimed(self):
        """Return the gRPC stub for :meth:`RecommenderClient.mark_recommendation_claimed`.

        Denotes a field as required. This indicates that the field **must**
        be provided as part of the request, and failure to do so will cause an
        error (usually ``INVALID_ARGUMENT``).

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].MarkRecommendationClaimed

    @property
    def mark_recommendation_succeeded(self):
        """Return the gRPC stub for :meth:`RecommenderClient.mark_recommendation_succeeded`.

        If this SourceCodeInfo represents a complete declaration, these are
        any comments appearing before and after the declaration which appear to
        be attached to the declaration.

        A series of line comments appearing on consecutive lines, with no other
        tokens appearing on those lines, will be treated as a single comment.

        leading_detached_comments will keep paragraphs of comments that appear
        before (but not connected to) the current element. Each paragraph,
        separated by empty lines, will be one comment element in the repeated
        field.

        Only the comment content is provided; comment markers (e.g. //) are
        stripped out. For block comments, leading whitespace and an asterisk
        will be stripped from the beginning of each line other than the first.
        Newlines are included in the output.

        Examples:

        optional int32 foo = 1; // Comment attached to foo. // Comment attached
        to bar. optional int32 bar = 2;

        optional string baz = 3; // Comment attached to baz. // Another line
        attached to baz.

        // Comment attached to qux. // // Another line attached to qux. optional
        double qux = 4;

        // Detached comment for corge. This is not leading or trailing comments
        // to qux or corge because there are blank lines separating it from //
        both.

        // Detached comment for corge paragraph 2.

        optional string corge = 5; /\* Block comment attached \* to corge.
        Leading asterisks \* will be removed. */ /* Block comment attached to \*
        grault. \*/ optional int32 grault = 6;

        // ignored detached comments.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].MarkRecommendationSucceeded

    @property
    def mark_recommendation_failed(self):
        """Return the gRPC stub for :meth:`RecommenderClient.mark_recommendation_failed`.

        Can be set for action 'test' for advanced matching for the value of
        'path' field. Either this or ``value`` will be set for 'test' operation.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].MarkRecommendationFailed
