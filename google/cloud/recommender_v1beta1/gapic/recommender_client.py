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

"""Accesses the google.cloud.recommender.v1beta1 Recommender API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.recommender_v1beta1.gapic import enums
from google.cloud.recommender_v1beta1.gapic import recommender_client_config
from google.cloud.recommender_v1beta1.gapic.transports import recommender_grpc_transport
from google.cloud.recommender_v1beta1.proto import recommendation_pb2
from google.cloud.recommender_v1beta1.proto import recommender_service_pb2
from google.cloud.recommender_v1beta1.proto import recommender_service_pb2_grpc


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-recommender"
).version


class RecommenderClient(object):
    """
    Provides insights and recommendations for cloud customers for various
    categories like performance optimization, cost savings, reliability, feature
    discovery, etc. Insights and recommendations are generated automatically
    based on analysis of user resources, configuration and monitoring metrics.
    """

    SERVICE_ADDRESS = "recommender.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.recommender.v1beta1.Recommender"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RecommenderClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def recommendation_path(cls, project, location, recommender, recommendation):
        """Return a fully-qualified recommendation string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/recommenders/{recommender}/recommendations/{recommendation}",
            project=project,
            location=location,
            recommender=recommender,
            recommendation=recommendation,
        )

    @classmethod
    def recommender_path(cls, project, location, recommender):
        """Return a fully-qualified recommender string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/recommenders/{recommender}",
            project=project,
            location=location,
            recommender=recommender,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.RecommenderGrpcTransport,
                    Callable[[~.Credentials, type], ~.RecommenderGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = recommender_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=recommender_grpc_transport.RecommenderGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = recommender_grpc_transport.RecommenderGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_recommendations(
        self,
        parent,
        page_size=None,
        filter_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Value for the ``path`` field. Will be set for
        actions:'add'/'replace'. Maybe set for action: 'test'. Either this or
        ``value_matcher`` will be set for 'test' operation. An exact match must
        be performed.

        Example:
            >>> from google.cloud import recommender_v1beta1
            >>>
            >>> client = recommender_v1beta1.RecommenderClient()
            >>>
            >>> parent = client.recommender_path('[PROJECT]', '[LOCATION]', '[RECOMMENDER]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_recommendations(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_recommendations(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): State properties to include with this state. Overwrites any existing
                ``state_metadata``. Keys must match the regex
                ``/^[a-z0-9][a-z0-9_.-]{0,62}$/``. Values must match the regex
                ``/^[a-zA-Z0-9_./-]{0,255}$/``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            filter_ (str): ``ListValue`` is a wrapper around a repeated field of values.

                The JSON representation for ``ListValue`` is JSON array.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.recommender_v1beta1.types.Recommendation` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_recommendations" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_recommendations"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_recommendations,
                default_retry=self._method_configs["ListRecommendations"].retry,
                default_timeout=self._method_configs["ListRecommendations"].timeout,
                client_info=self._client_info,
            )

        request = recommender_service_pb2.ListRecommendationsRequest(
            parent=parent, page_size=page_size, filter=filter_
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_recommendations"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="recommendations",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_recommendation(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The resource type of a child collection that the annotated field
        references. This is useful for annotating the ``parent`` field that
        doesn't have a fixed resource type.

        Example:

        message ListLogEntriesRequest { string parent = 1
        [(google.api.resource_reference) = { child_type:
        "logging.googleapis.com/LogEntry" }; }

        Example:
            >>> from google.cloud import recommender_v1beta1
            >>>
            >>> client = recommender_v1beta1.RecommenderClient()
            >>>
            >>> name = client.recommendation_path('[PROJECT]', '[LOCATION]', '[RECOMMENDER]', '[RECOMMENDATION]')
            >>>
            >>> response = client.get_recommendation(name)

        Args:
            name (str): Required. Name of the recommendation.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.recommender_v1beta1.types.Recommendation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_recommendation" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_recommendation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_recommendation,
                default_retry=self._method_configs["GetRecommendation"].retry,
                default_timeout=self._method_configs["GetRecommendation"].timeout,
                client_info=self._client_info,
            )

        request = recommender_service_pb2.GetRecommendationRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_recommendation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def mark_recommendation_claimed(
        self,
        name,
        etag,
        state_metadata=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Denotes a field as required. This indicates that the field **must**
        be provided as part of the request, and failure to do so will cause an
        error (usually ``INVALID_ARGUMENT``).

        Example:
            >>> from google.cloud import recommender_v1beta1
            >>>
            >>> client = recommender_v1beta1.RecommenderClient()
            >>>
            >>> name = client.recommendation_path('[PROJECT]', '[LOCATION]', '[RECOMMENDER]', '[RECOMMENDATION]')
            >>>
            >>> # TODO: Initialize `etag`:
            >>> etag = ''
            >>>
            >>> response = client.mark_recommendation_claimed(name, etag)

        Args:
            name (str): Required. Name of the recommendation.
            etag (str): Required. Fingerprint of the Recommendation. Provides optimistic locking.
            state_metadata (dict[str -> str]): The custom pattern is used for specifying an HTTP method that is not
                included in the ``pattern`` field, such as HEAD, or "*" to leave the
                HTTP method unspecified for this rule. The wild-card rule is useful for
                services that provide content to Web (HTML) clients.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.recommender_v1beta1.types.Recommendation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "mark_recommendation_claimed" not in self._inner_api_calls:
            self._inner_api_calls[
                "mark_recommendation_claimed"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.mark_recommendation_claimed,
                default_retry=self._method_configs["MarkRecommendationClaimed"].retry,
                default_timeout=self._method_configs[
                    "MarkRecommendationClaimed"
                ].timeout,
                client_info=self._client_info,
            )

        request = recommender_service_pb2.MarkRecommendationClaimedRequest(
            name=name, etag=etag, state_metadata=state_metadata
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["mark_recommendation_claimed"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def mark_recommendation_succeeded(
        self,
        name,
        etag,
        state_metadata=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import recommender_v1beta1
            >>>
            >>> client = recommender_v1beta1.RecommenderClient()
            >>>
            >>> name = client.recommendation_path('[PROJECT]', '[LOCATION]', '[RECOMMENDER]', '[RECOMMENDATION]')
            >>>
            >>> # TODO: Initialize `etag`:
            >>> etag = ''
            >>>
            >>> response = client.mark_recommendation_succeeded(name, etag)

        Args:
            name (str): Required. Name of the recommendation.
            etag (str): Required. Fingerprint of the Recommendation. Provides optimistic locking.
            state_metadata (dict[str -> str]): The name of the request field whose value is mapped to the HTTP
                request body, or ``*`` for mapping all request fields not captured by
                the path pattern to the HTTP body, or omitted for not having any HTTP
                request body.

                NOTE: the referred field must be present at the top-level of the request
                message type.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.recommender_v1beta1.types.Recommendation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "mark_recommendation_succeeded" not in self._inner_api_calls:
            self._inner_api_calls[
                "mark_recommendation_succeeded"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.mark_recommendation_succeeded,
                default_retry=self._method_configs["MarkRecommendationSucceeded"].retry,
                default_timeout=self._method_configs[
                    "MarkRecommendationSucceeded"
                ].timeout,
                client_info=self._client_info,
            )

        request = recommender_service_pb2.MarkRecommendationSucceededRequest(
            name=name, etag=etag, state_metadata=state_metadata
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["mark_recommendation_succeeded"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def mark_recommendation_failed(
        self,
        name,
        etag,
        state_metadata=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Can be set for action 'test' for advanced matching for the value of
        'path' field. Either this or ``value`` will be set for 'test' operation.

        Example:
            >>> from google.cloud import recommender_v1beta1
            >>>
            >>> client = recommender_v1beta1.RecommenderClient()
            >>>
            >>> name = client.recommendation_path('[PROJECT]', '[LOCATION]', '[RECOMMENDER]', '[RECOMMENDATION]')
            >>>
            >>> # TODO: Initialize `etag`:
            >>> etag = ''
            >>>
            >>> response = client.mark_recommendation_failed(name, etag)

        Args:
            name (str): Required. Name of the recommendation.
            etag (str): Required. Fingerprint of the Recommendation. Provides optimistic locking.
            state_metadata (dict[str -> str]): State properties to include with this state. Overwrites any existing
                ``state_metadata``. Keys must match the regex
                ``/^[a-z0-9][a-z0-9_.-]{0,62}$/``. Values must match the regex
                ``/^[a-zA-Z0-9_./-]{0,255}$/``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.recommender_v1beta1.types.Recommendation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "mark_recommendation_failed" not in self._inner_api_calls:
            self._inner_api_calls[
                "mark_recommendation_failed"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.mark_recommendation_failed,
                default_retry=self._method_configs["MarkRecommendationFailed"].retry,
                default_timeout=self._method_configs[
                    "MarkRecommendationFailed"
                ].timeout,
                client_info=self._client_info,
            )

        request = recommender_service_pb2.MarkRecommendationFailedRequest(
            name=name, etag=etag, state_metadata=state_metadata
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["mark_recommendation_failed"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
