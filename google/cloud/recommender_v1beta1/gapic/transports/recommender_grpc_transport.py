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
    def list_insights(self):
        """Return the gRPC stub for :meth:`RecommenderClient.list_insights`.

        # gRPC Transcoding

        gRPC Transcoding is a feature for mapping between a gRPC method and one
        or more HTTP REST endpoints. It allows developers to build a single API
        service that supports both gRPC APIs and REST APIs. Many systems,
        including `Google APIs <https://github.com/googleapis/googleapis>`__,
        `Cloud Endpoints <https://cloud.google.com/endpoints>`__, `gRPC
        Gateway <https://github.com/grpc-ecosystem/grpc-gateway>`__, and
        `Envoy <https://github.com/envoyproxy/envoy>`__ proxy support this
        feature and use it for large scale production services.

        ``HttpRule`` defines the schema of the gRPC/REST mapping. The mapping
        specifies how different portions of the gRPC request message are mapped
        to the URL path, URL query parameters, and HTTP request body. It also
        controls how the gRPC response message is mapped to the HTTP response
        body. ``HttpRule`` is typically specified as an ``google.api.http``
        annotation on the gRPC method.

        Each mapping specifies a URL path template and an HTTP method. The path
        template may refer to one or more fields in the gRPC request message, as
        long as each field is a non-repeated field with a primitive
        (non-message) type. The path template controls how fields of the request
        message are mapped to the URL path.

        Example:

        ::

            service Messaging {
              rpc GetMessage(GetMessageRequest) returns (Message) {
                option (google.api.http) = {
                    get: "/v1/{name=messages/*}"
                };
              }
            }
            message GetMessageRequest {
              string name = 1; // Mapped to URL path.
            }
            message Message {
              string text = 1; // The resource content.
            }

        This enables an HTTP REST to gRPC mapping as below:

        HTTP \| gRPC -----|----- ``GET /v1/messages/123456`` \|
        ``GetMessage(name: "messages/123456")``

        Any fields in the request message which are not bound by the path
        template automatically become HTTP query parameters if there is no HTTP
        request body. For example:

        ::

            service Messaging {
              rpc GetMessage(GetMessageRequest) returns (Message) {
                option (google.api.http) = {
                    get:"/v1/messages/{message_id}"
                };
              }
            }
            message GetMessageRequest {
              message SubMessage {
                string subfield = 1;
              }
              string message_id = 1; // Mapped to URL path.
              int64 revision = 2;    // Mapped to URL query parameter `revision`.
              SubMessage sub = 3;    // Mapped to URL query parameter `sub.subfield`.
            }

        This enables a HTTP JSON to RPC mapping as below:

        HTTP \| gRPC -----|-----
        ``GET /v1/messages/123456?revision=2&sub.subfield=foo`` \|
        ``GetMessage(message_id: "123456" revision: 2 sub: SubMessage(subfield: "foo"))``

        Note that fields which are mapped to URL query parameters must have a
        primitive type or a repeated primitive type or a non-repeated message
        type. In the case of a repeated type, the parameter can be repeated in
        the URL as ``...?param=A&param=B``. In the case of a message type, each
        field of the message is mapped to a separate parameter, such as
        ``...?foo.a=A&foo.b=B&foo.c=C``.

        For HTTP methods that allow a request body, the ``body`` field specifies
        the mapping. Consider a REST update method on the message resource
        collection:

        ::

            service Messaging {
              rpc UpdateMessage(UpdateMessageRequest) returns (Message) {
                option (google.api.http) = {
                  patch: "/v1/messages/{message_id}"
                  body: "message"
                };
              }
            }
            message UpdateMessageRequest {
              string message_id = 1; // mapped to the URL
              Message message = 2;   // mapped to the body
            }

        The following HTTP JSON to RPC mapping is enabled, where the
        representation of the JSON in the request body is determined by protos
        JSON encoding:

        HTTP \| gRPC -----|----- ``PATCH /v1/messages/123456 { "text": "Hi!" }``
        \| ``UpdateMessage(message_id: "123456" message { text: "Hi!" })``

        The special name ``*`` can be used in the body mapping to define that
        every field not bound by the path template should be mapped to the
        request body. This enables the following alternative definition of the
        update method:

        ::

            service Messaging {
              rpc UpdateMessage(Message) returns (Message) {
                option (google.api.http) = {
                  patch: "/v1/messages/{message_id}"
                  body: "*"
                };
              }
            }
            message Message {
              string message_id = 1;
              string text = 2;
            }

        The following HTTP JSON to RPC mapping is enabled:

        HTTP \| gRPC -----|----- ``PATCH /v1/messages/123456 { "text": "Hi!" }``
        \| ``UpdateMessage(message_id: "123456" text: "Hi!")``

        Note that when using ``*`` in the body mapping, it is not possible to
        have HTTP parameters, as all fields not bound by the path end in the
        body. This makes this option more rarely used in practice when defining
        REST APIs. The common usage of ``*`` is in custom methods which don't
        use the URL at all for transferring data.

        It is possible to define multiple HTTP methods for one RPC by using the
        ``additional_bindings`` option. Example:

        ::

            service Messaging {
              rpc GetMessage(GetMessageRequest) returns (Message) {
                option (google.api.http) = {
                  get: "/v1/messages/{message_id}"
                  additional_bindings {
                    get: "/v1/users/{user_id}/messages/{message_id}"
                  }
                };
              }
            }
            message GetMessageRequest {
              string message_id = 1;
              string user_id = 2;
            }

        This enables the following two alternative HTTP JSON to RPC mappings:

        HTTP \| gRPC -----|----- ``GET /v1/messages/123456`` \|
        ``GetMessage(message_id: "123456")``
        ``GET /v1/users/me/messages/123456`` \|
        ``GetMessage(user_id: "me" message_id: "123456")``

        ## Rules for HTTP mapping

        1. Leaf request fields (recursive expansion nested messages in the
           request message) are classified into three categories:

           -  Fields referred by the path template. They are passed via the URL
              path.
           -  Fields referred by the ``HttpRule.body``. They are passed via the
              HTTP request body.
           -  All other fields are passed via the URL query parameters, and the
              parameter name is the field path in the request message. A
              repeated field can be represented as multiple query parameters
              under the same name.

        2. If ``HttpRule.body`` is "*", there is no URL query parameter, all
           fields are passed via URL path and HTTP request body.
        3. If ``HttpRule.body`` is omitted, there is no HTTP request body, all
           fields are passed via URL path and URL query parameters.

        Path template syntax
        ~~~~~~~~~~~~~~~~~~~~

        ::

            Template = "/" Segments [ Verb ] ;
            Segments = Segment { "/" Segment } ;
            Segment  = "*" | "**" | LITERAL | Variable ;
            Variable = "{" FieldPath [ "=" Segments ] "}" ;
            FieldPath = IDENT { "." IDENT } ;
            Verb     = ":" LITERAL ;

        The syntax ``*`` matches a single URL path segment. The syntax ``**``
        matches zero or more URL path segments, which must be the last part of
        the URL path except the ``Verb``.

        The syntax ``Variable`` matches part of the URL path as specified by its
        template. A variable template must not contain other variables. If a
        variable matches a single path segment, its template may be omitted,
        e.g. ``{var}`` is equivalent to ``{var=*}``.

        The syntax ``LITERAL`` matches literal text in the URL path. If the
        ``LITERAL`` contains any reserved character, such characters should be
        percent-encoded before the matching.

        If a variable contains exactly one path segment, such as ``"{var}"`` or
        ``"{var=*}"``, when such a variable is expanded into a URL path on the
        client side, all characters except ``[-_.~0-9a-zA-Z]`` are
        percent-encoded. The server side does the reverse decoding. Such
        variables show up in the `Discovery
        Document <https://developers.google.com/discovery/v1/reference/apis>`__
        as ``{var}``.

        If a variable contains multiple path segments, such as ``"{var=foo/*}"``
        or ``"{var=**}"``, when such a variable is expanded into a URL path on
        the client side, all characters except ``[-_.~/0-9a-zA-Z]`` are
        percent-encoded. The server side does the reverse decoding, except "%2F"
        and "%2f" are left unchanged. Such variables show up in the `Discovery
        Document <https://developers.google.com/discovery/v1/reference/apis>`__
        as ``{+var}``.

        ## Using gRPC API Service Configuration

        gRPC API Service Configuration (service config) is a configuration
        language for configuring a gRPC service to become a user-facing product.
        The service config is simply the YAML representation of the
        ``google.api.Service`` proto message.

        As an alternative to annotating your proto file, you can configure gRPC
        transcoding in your service config YAML files. You do this by specifying
        a ``HttpRule`` that maps the gRPC method to a REST endpoint, achieving
        the same effect as the proto annotation. This can be particularly useful
        if you have a proto that is reused in multiple services. Note that any
        transcoding specified in the service config will override any matching
        transcoding configuration in the proto.

        Example:

        ::

            http:
              rules:
                # Selects a gRPC method and applies HttpRule to it.
                - selector: example.v1.Messaging.GetMessage
                  get: /v1/messages/{message_id}/{sub.subfield}

        ## Special notes

        When gRPC Transcoding is used to map a gRPC to JSON REST endpoints, the
        proto to JSON conversion must follow the `proto3
        specification <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.

        While the single segment variable follows the semantics of `RFC
        6570 <https://tools.ietf.org/html/rfc6570>`__ Section 3.2.2 Simple
        String Expansion, the multi segment variable **does not** follow RFC
        6570 Section 3.2.3 Reserved Expansion. The reason is that the Reserved
        Expansion does not expand special characters like ``?`` and ``#``, which
        would lead to invalid URLs. As the result, gRPC Transcoding uses a
        custom encoding for multi segment variables.

        The path variables **must not** refer to any repeated or mapped field,
        because client libraries are not capable of handling such variable
        expansion.

        The path variables **must not** capture the leading "/" character. The
        reason is that the most common use case "{var}" does not capture the
        leading "/" character. For consistency, all path variables must share
        the same behavior.

        Repeated message fields must not be mapped to URL query parameters,
        because no client library can support such complicated mapping.

        If an API needs to use a JSON array for request or response body, it can
        map the request or response body to a repeated field. However, some gRPC
        Transcoding implementations may not support this feature.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].ListInsights

    @property
    def get_insight(self):
        """Return the gRPC stub for :meth:`RecommenderClient.get_insight`.

        Optional. If present, retrieves the next batch of results from the
        preceding call to this method. ``page_token`` must be the value of
        ``next_page_token`` from the previous response. The values of other
        method parameters must be identical to those in the previous call.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].GetInsight

    @property
    def mark_insight_accepted(self):
        """Return the gRPC stub for :meth:`RecommenderClient.mark_insight_accepted`.

        Selects a method to which this rule applies.

        Refer to ``selector`` for syntax details.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].MarkInsightAccepted

    @property
    def list_recommendations(self):
        """Return the gRPC stub for :meth:`RecommenderClient.list_recommendations`.

        Can be set with action 'copy' or 'move' to indicate the source field
        within resource or source_resource, ignored if provided for other
        operation types.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].ListRecommendations

    @property
    def get_recommendation(self):
        """Return the gRPC stub for :meth:`RecommenderClient.get_recommendation`.

        The resource type that the annotated field references.

        Example:

        ::

            message Subscription {
              string topic = 2 [(google.api.resource_reference) = {
                type: "pubsub.googleapis.com/Topic"
              }];
            }

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].GetRecommendation

    @property
    def mark_recommendation_claimed(self):
        """Return the gRPC stub for :meth:`RecommenderClient.mark_recommendation_claimed`.

        Optional. Filter expression to restrict the insights returned.
        Supported filter fields: state Eg: \`state:"DISMISSED" or state:"ACTIVE"

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].MarkRecommendationClaimed

    @property
    def mark_recommendation_succeeded(self):
        """Return the gRPC stub for :meth:`RecommenderClient.mark_recommendation_succeeded`.

        Value for the ``path`` field. Will be set for
        actions:'add'/'replace'. Maybe set for action: 'test'. Either this or
        ``value_matcher`` will be set for 'test' operation. An exact match must
        be performed.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].MarkRecommendationSucceeded

    @property
    def mark_recommendation_failed(self):
        """Return the gRPC stub for :meth:`RecommenderClient.mark_recommendation_failed`.

        Request for the ``MarkRecommendationFailed`` Method.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["recommender_stub"].MarkRecommendationFailed
