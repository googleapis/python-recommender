# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.recommender_v1beta1.services.recommender import pagers
from google.cloud.recommender_v1beta1.types import insight
from google.cloud.recommender_v1beta1.types import insight_type_config
from google.cloud.recommender_v1beta1.types import (
    insight_type_config as gcr_insight_type_config,
)
from google.cloud.recommender_v1beta1.types import recommendation
from google.cloud.recommender_v1beta1.types import recommender_config
from google.cloud.recommender_v1beta1.types import (
    recommender_config as gcr_recommender_config,
)
from google.cloud.recommender_v1beta1.types import recommender_service
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import RecommenderTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import RecommenderGrpcAsyncIOTransport
from .client import RecommenderClient


class RecommenderAsyncClient:
    """Provides insights and recommendations for cloud customers for
    various categories like performance optimization, cost savings,
    reliability, feature discovery, etc. Insights and
    recommendations are generated automatically based on analysis of
    user resources, configuration and monitoring metrics.
    """

    _client: RecommenderClient

    DEFAULT_ENDPOINT = RecommenderClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = RecommenderClient.DEFAULT_MTLS_ENDPOINT

    insight_path = staticmethod(RecommenderClient.insight_path)
    parse_insight_path = staticmethod(RecommenderClient.parse_insight_path)
    insight_type_path = staticmethod(RecommenderClient.insight_type_path)
    parse_insight_type_path = staticmethod(RecommenderClient.parse_insight_type_path)
    insight_type_config_path = staticmethod(RecommenderClient.insight_type_config_path)
    parse_insight_type_config_path = staticmethod(
        RecommenderClient.parse_insight_type_config_path
    )
    recommendation_path = staticmethod(RecommenderClient.recommendation_path)
    parse_recommendation_path = staticmethod(
        RecommenderClient.parse_recommendation_path
    )
    recommender_path = staticmethod(RecommenderClient.recommender_path)
    parse_recommender_path = staticmethod(RecommenderClient.parse_recommender_path)
    recommender_config_path = staticmethod(RecommenderClient.recommender_config_path)
    parse_recommender_config_path = staticmethod(
        RecommenderClient.parse_recommender_config_path
    )
    common_billing_account_path = staticmethod(
        RecommenderClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        RecommenderClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(RecommenderClient.common_folder_path)
    parse_common_folder_path = staticmethod(RecommenderClient.parse_common_folder_path)
    common_organization_path = staticmethod(RecommenderClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        RecommenderClient.parse_common_organization_path
    )
    common_project_path = staticmethod(RecommenderClient.common_project_path)
    parse_common_project_path = staticmethod(
        RecommenderClient.parse_common_project_path
    )
    common_location_path = staticmethod(RecommenderClient.common_location_path)
    parse_common_location_path = staticmethod(
        RecommenderClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RecommenderAsyncClient: The constructed client.
        """
        return RecommenderClient.from_service_account_info.__func__(RecommenderAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RecommenderAsyncClient: The constructed client.
        """
        return RecommenderClient.from_service_account_file.__func__(RecommenderAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return RecommenderClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> RecommenderTransport:
        """Returns the transport used by the client instance.

        Returns:
            RecommenderTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(RecommenderClient).get_transport_class, type(RecommenderClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, RecommenderTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the recommender client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.RecommenderTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = RecommenderClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_insights(
        self,
        request: Union[recommender_service.ListInsightsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListInsightsAsyncPager:
        r"""Lists insights for the specified Cloud Resource. Requires the
        recommender.*.list IAM permission for the specified insight
        type.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_list_insights():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.ListInsightsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_insights(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.ListInsightsRequest, dict]):
                The request object. Request for the `ListInsights`
                method.
            parent (:class:`str`):
                Required. The container resource on which to execute the
                request. Acceptable formats:

                -  ``projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

                -  ``projects/[PROJECT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

                -  ``billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

                -  ``folders/[FOLDER_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

                -  ``organizations/[ORGANIZATION_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]``

                LOCATION here refers to GCP Locations:
                https://cloud.google.com/about/locations/
                INSIGHT_TYPE_ID refers to supported insight types:
                https://cloud.google.com/recommender/docs/insights/insight-types.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.services.recommender.pagers.ListInsightsAsyncPager:
                Response to the ListInsights method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.ListInsightsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_insights,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListInsightsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_insight(
        self,
        request: Union[recommender_service.GetInsightRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> insight.Insight:
        r"""Gets the requested insight. Requires the recommender.*.get IAM
        permission for the specified insight type.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_get_insight():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.GetInsightRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_insight(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.GetInsightRequest, dict]):
                The request object. Request to the `GetInsight` method.
            name (:class:`str`):
                Required. Name of the insight.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.Insight:
                An insight along with the information
                used to derive the insight. The insight
                may have associated recomendations as
                well.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.GetInsightRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_insight,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def mark_insight_accepted(
        self,
        request: Union[recommender_service.MarkInsightAcceptedRequest, dict] = None,
        *,
        name: str = None,
        state_metadata: Sequence[
            recommender_service.MarkInsightAcceptedRequest.StateMetadataEntry
        ] = None,
        etag: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> insight.Insight:
        r"""Marks the Insight State as Accepted. Users can use this method
        to indicate to the Recommender API that they have applied some
        action based on the insight. This stops the insight content from
        being updated.

        MarkInsightAccepted can be applied to insights in ACTIVE state.
        Requires the recommender.*.update IAM permission for the
        specified insight.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_mark_insight_accepted():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.MarkInsightAcceptedRequest(
                    name="name_value",
                    etag="etag_value",
                )

                # Make the request
                response = client.mark_insight_accepted(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.MarkInsightAcceptedRequest, dict]):
                The request object. Request for the
                `MarkInsightAccepted` method.
            name (:class:`str`):
                Required. Name of the insight.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            state_metadata (:class:`Sequence[google.cloud.recommender_v1beta1.types.MarkInsightAcceptedRequest.StateMetadataEntry]`):
                Optional. State properties user wish to include with
                this state. Full replace of the current state_metadata.

                This corresponds to the ``state_metadata`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            etag (:class:`str`):
                Required. Fingerprint of the Insight.
                Provides optimistic locking.

                This corresponds to the ``etag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.Insight:
                An insight along with the information
                used to derive the insight. The insight
                may have associated recomendations as
                well.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, state_metadata, etag])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.MarkInsightAcceptedRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if etag is not None:
            request.etag = etag

        if state_metadata:
            request.state_metadata.update(state_metadata)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.mark_insight_accepted,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_recommendations(
        self,
        request: Union[recommender_service.ListRecommendationsRequest, dict] = None,
        *,
        parent: str = None,
        filter: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListRecommendationsAsyncPager:
        r"""Lists recommendations for the specified Cloud Resource. Requires
        the recommender.*.list IAM permission for the specified
        recommender.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_list_recommendations():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.ListRecommendationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_recommendations(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.ListRecommendationsRequest, dict]):
                The request object. Request for the
                `ListRecommendations` method.
            parent (:class:`str`):
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

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Filter expression to restrict the recommendations
                returned. Supported filter fields:

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

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.services.recommender.pagers.ListRecommendationsAsyncPager:
                Response to the ListRecommendations method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, filter])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.ListRecommendationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_recommendations,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListRecommendationsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_recommendation(
        self,
        request: Union[recommender_service.GetRecommendationRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> recommendation.Recommendation:
        r"""Gets the requested recommendation. Requires the
        recommender.*.get IAM permission for the specified recommender.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_get_recommendation():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.GetRecommendationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_recommendation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.GetRecommendationRequest, dict]):
                The request object. Request to the `GetRecommendation`
                method.
            name (:class:`str`):
                Required. Name of the recommendation.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.Recommendation:
                A recommendation along with a
                suggested action. E.g., a rightsizing
                recommendation for an underutilized VM,
                IAM role recommendations, etc

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.GetRecommendationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_recommendation,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def mark_recommendation_claimed(
        self,
        request: Union[
            recommender_service.MarkRecommendationClaimedRequest, dict
        ] = None,
        *,
        name: str = None,
        state_metadata: Sequence[
            recommender_service.MarkRecommendationClaimedRequest.StateMetadataEntry
        ] = None,
        etag: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> recommendation.Recommendation:
        r"""Marks the Recommendation State as Claimed. Users can use this
        method to indicate to the Recommender API that they are starting
        to apply the recommendation themselves. This stops the
        recommendation content from being updated. Associated insights
        are frozen and placed in the ACCEPTED state.

        MarkRecommendationClaimed can be applied to recommendations in
        CLAIMED or ACTIVE state.

        Requires the recommender.*.update IAM permission for the
        specified recommender.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_mark_recommendation_claimed():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.MarkRecommendationClaimedRequest(
                    name="name_value",
                    etag="etag_value",
                )

                # Make the request
                response = client.mark_recommendation_claimed(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.MarkRecommendationClaimedRequest, dict]):
                The request object. Request for the
                `MarkRecommendationClaimed` Method.
            name (:class:`str`):
                Required. Name of the recommendation.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            state_metadata (:class:`Sequence[google.cloud.recommender_v1beta1.types.MarkRecommendationClaimedRequest.StateMetadataEntry]`):
                State properties to include with this state. Overwrites
                any existing ``state_metadata``. Keys must match the
                regex ``/^[a-z0-9][a-z0-9_.-]{0,62}$/``. Values must
                match the regex ``/^[a-zA-Z0-9_./-]{0,255}$/``.

                This corresponds to the ``state_metadata`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            etag (:class:`str`):
                Required. Fingerprint of the
                Recommendation. Provides optimistic
                locking.

                This corresponds to the ``etag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.Recommendation:
                A recommendation along with a
                suggested action. E.g., a rightsizing
                recommendation for an underutilized VM,
                IAM role recommendations, etc

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, state_metadata, etag])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.MarkRecommendationClaimedRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if etag is not None:
            request.etag = etag

        if state_metadata:
            request.state_metadata.update(state_metadata)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.mark_recommendation_claimed,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def mark_recommendation_succeeded(
        self,
        request: Union[
            recommender_service.MarkRecommendationSucceededRequest, dict
        ] = None,
        *,
        name: str = None,
        state_metadata: Sequence[
            recommender_service.MarkRecommendationSucceededRequest.StateMetadataEntry
        ] = None,
        etag: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> recommendation.Recommendation:
        r"""Marks the Recommendation State as Succeeded. Users can use this
        method to indicate to the Recommender API that they have applied
        the recommendation themselves, and the operation was successful.
        This stops the recommendation content from being updated.
        Associated insights are frozen and placed in the ACCEPTED state.

        MarkRecommendationSucceeded can be applied to recommendations in
        ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

        Requires the recommender.*.update IAM permission for the
        specified recommender.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_mark_recommendation_succeeded():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.MarkRecommendationSucceededRequest(
                    name="name_value",
                    etag="etag_value",
                )

                # Make the request
                response = client.mark_recommendation_succeeded(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.MarkRecommendationSucceededRequest, dict]):
                The request object. Request for the
                `MarkRecommendationSucceeded` Method.
            name (:class:`str`):
                Required. Name of the recommendation.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            state_metadata (:class:`Sequence[google.cloud.recommender_v1beta1.types.MarkRecommendationSucceededRequest.StateMetadataEntry]`):
                State properties to include with this state. Overwrites
                any existing ``state_metadata``. Keys must match the
                regex ``/^[a-z0-9][a-z0-9_.-]{0,62}$/``. Values must
                match the regex ``/^[a-zA-Z0-9_./-]{0,255}$/``.

                This corresponds to the ``state_metadata`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            etag (:class:`str`):
                Required. Fingerprint of the
                Recommendation. Provides optimistic
                locking.

                This corresponds to the ``etag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.Recommendation:
                A recommendation along with a
                suggested action. E.g., a rightsizing
                recommendation for an underutilized VM,
                IAM role recommendations, etc

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, state_metadata, etag])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.MarkRecommendationSucceededRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if etag is not None:
            request.etag = etag

        if state_metadata:
            request.state_metadata.update(state_metadata)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.mark_recommendation_succeeded,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def mark_recommendation_failed(
        self,
        request: Union[
            recommender_service.MarkRecommendationFailedRequest, dict
        ] = None,
        *,
        name: str = None,
        state_metadata: Sequence[
            recommender_service.MarkRecommendationFailedRequest.StateMetadataEntry
        ] = None,
        etag: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> recommendation.Recommendation:
        r"""Marks the Recommendation State as Failed. Users can use this
        method to indicate to the Recommender API that they have applied
        the recommendation themselves, and the operation failed. This
        stops the recommendation content from being updated. Associated
        insights are frozen and placed in the ACCEPTED state.

        MarkRecommendationFailed can be applied to recommendations in
        ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

        Requires the recommender.*.update IAM permission for the
        specified recommender.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_mark_recommendation_failed():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.MarkRecommendationFailedRequest(
                    name="name_value",
                    etag="etag_value",
                )

                # Make the request
                response = client.mark_recommendation_failed(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.MarkRecommendationFailedRequest, dict]):
                The request object. Request for the
                `MarkRecommendationFailed` Method.
            name (:class:`str`):
                Required. Name of the recommendation.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            state_metadata (:class:`Sequence[google.cloud.recommender_v1beta1.types.MarkRecommendationFailedRequest.StateMetadataEntry]`):
                State properties to include with this state. Overwrites
                any existing ``state_metadata``. Keys must match the
                regex ``/^[a-z0-9][a-z0-9_.-]{0,62}$/``. Values must
                match the regex ``/^[a-zA-Z0-9_./-]{0,255}$/``.

                This corresponds to the ``state_metadata`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            etag (:class:`str`):
                Required. Fingerprint of the
                Recommendation. Provides optimistic
                locking.

                This corresponds to the ``etag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.Recommendation:
                A recommendation along with a
                suggested action. E.g., a rightsizing
                recommendation for an underutilized VM,
                IAM role recommendations, etc

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, state_metadata, etag])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.MarkRecommendationFailedRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if etag is not None:
            request.etag = etag

        if state_metadata:
            request.state_metadata.update(state_metadata)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.mark_recommendation_failed,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_recommender_config(
        self,
        request: Union[recommender_service.GetRecommenderConfigRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> recommender_config.RecommenderConfig:
        r"""Gets the requested Recommender Config. There is only
        one instance of the config for each Recommender.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_get_recommender_config():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.GetRecommenderConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_recommender_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.GetRecommenderConfigRequest, dict]):
                The request object. Request for the
                GetRecommenderConfig` method.
            name (:class:`str`):
                Required. Name of the Recommendation Config to get.

                Acceptable formats:

                -  ``projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config``

                -  ``projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config``

                -  ``organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.RecommenderConfig:
                Configuration for a Recommender.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.GetRecommenderConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_recommender_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_recommender_config(
        self,
        request: Union[recommender_service.UpdateRecommenderConfigRequest, dict] = None,
        *,
        recommender_config: gcr_recommender_config.RecommenderConfig = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcr_recommender_config.RecommenderConfig:
        r"""Updates a Recommender Config. This will create a new
        revision of the config.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_update_recommender_config():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.UpdateRecommenderConfigRequest(
                )

                # Make the request
                response = client.update_recommender_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.UpdateRecommenderConfigRequest, dict]):
                The request object. Request for the
                `UpdateRecommenderConfig` method.
            recommender_config (:class:`google.cloud.recommender_v1beta1.types.RecommenderConfig`):
                Required. The RecommenderConfig to
                update.

                This corresponds to the ``recommender_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.RecommenderConfig:
                Configuration for a Recommender.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([recommender_config, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.UpdateRecommenderConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if recommender_config is not None:
            request.recommender_config = recommender_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_recommender_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("recommender_config.name", request.recommender_config.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_insight_type_config(
        self,
        request: Union[recommender_service.GetInsightTypeConfigRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> insight_type_config.InsightTypeConfig:
        r"""Gets the requested InsightTypeConfig. There is only
        one instance of the config for each InsightType.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_get_insight_type_config():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.GetInsightTypeConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_insight_type_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.GetInsightTypeConfigRequest, dict]):
                The request object. Request for the
                GetInsightTypeConfig` method.
            name (:class:`str`):
                Required. Name of the InsightTypeConfig to get.

                Acceptable formats:

                -  ``projects/[PROJECT_NUMBER]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config``

                -  ``projects/[PROJECT_ID]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config``

                -  ``organizations/[ORGANIZATION_ID]/locations/global/recommenders/[INSIGHT_TYPE_ID]/config``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.InsightTypeConfig:
                Configuration for an InsightType.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.GetInsightTypeConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_insight_type_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_insight_type_config(
        self,
        request: Union[recommender_service.UpdateInsightTypeConfigRequest, dict] = None,
        *,
        insight_type_config: gcr_insight_type_config.InsightTypeConfig = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcr_insight_type_config.InsightTypeConfig:
        r"""Updates an InsightTypeConfig change. This will create
        a new revision of the config.


        .. code-block::

            from google.cloud import recommender_v1beta1

            def sample_update_insight_type_config():
                # Create a client
                client = recommender_v1beta1.RecommenderClient()

                # Initialize request argument(s)
                request = recommender_v1beta1.UpdateInsightTypeConfigRequest(
                )

                # Make the request
                response = client.update_insight_type_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.recommender_v1beta1.types.UpdateInsightTypeConfigRequest, dict]):
                The request object. Request for the
                `UpdateInsightTypeConfig` method.
            insight_type_config (:class:`google.cloud.recommender_v1beta1.types.InsightTypeConfig`):
                Required. The InsightTypeConfig to
                update.

                This corresponds to the ``insight_type_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.recommender_v1beta1.types.InsightTypeConfig:
                Configuration for an InsightType.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([insight_type_config, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = recommender_service.UpdateInsightTypeConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if insight_type_config is not None:
            request.insight_type_config = insight_type_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_insight_type_config,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("insight_type_config.name", request.insight_type_config.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-recommender",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("RecommenderAsyncClient",)
