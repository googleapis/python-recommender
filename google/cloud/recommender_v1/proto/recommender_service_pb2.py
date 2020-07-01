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

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/recommender_v1/proto/recommender_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.recommender_v1.proto import (
    recommendation_pb2 as google_dot_cloud_dot_recommender__v1_dot_proto_dot_recommendation__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/recommender_v1/proto/recommender_service.proto",
    package="google.cloud.recommender.v1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.recommender.v1B\020RecommenderProtoP\001ZFgoogle.golang.org/genproto/googleapis/cloud/recommender/v1;recommender\242\002\004CREC\252\002\033Google.Cloud.Recommender.V1",
    serialized_pb=b'\n;google/cloud/recommender_v1/proto/recommender_service.proto\x12\x1bgoogle.cloud.recommender.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x36google/cloud/recommender_v1/proto/recommendation.proto"\x9d\x01\n\x1aListRecommendationsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0\x41\x02\xfa\x41(\n&recommender.googleapis.com/Recommender\x12\x16\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t"|\n\x1bListRecommendationsResponse\x12\x44\n\x0frecommendations\x18\x01 \x03(\x0b\x32+.google.cloud.recommender.v1.Recommendation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"[\n\x18GetRecommendationRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\n)recommender.googleapis.com/Recommendation"\x96\x02\n MarkRecommendationClaimedRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\n)recommender.googleapis.com/Recommendation\x12h\n\x0estate_metadata\x18\x02 \x03(\x0b\x32P.google.cloud.recommender.v1.MarkRecommendationClaimedRequest.StateMetadataEntry\x12\x11\n\x04\x65tag\x18\x03 \x01(\tB\x03\xe0\x41\x02\x1a\x34\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x9a\x02\n"MarkRecommendationSucceededRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\n)recommender.googleapis.com/Recommendation\x12j\n\x0estate_metadata\x18\x02 \x03(\x0b\x32R.google.cloud.recommender.v1.MarkRecommendationSucceededRequest.StateMetadataEntry\x12\x11\n\x04\x65tag\x18\x03 \x01(\tB\x03\xe0\x41\x02\x1a\x34\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x94\x02\n\x1fMarkRecommendationFailedRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0\x41\x02\xfa\x41+\n)recommender.googleapis.com/Recommendation\x12g\n\x0estate_metadata\x18\x02 \x03(\x0b\x32O.google.cloud.recommender.v1.MarkRecommendationFailedRequest.StateMetadataEntry\x12\x11\n\x04\x65tag\x18\x03 \x01(\tB\x03\xe0\x41\x02\x1a\x34\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x9d\n\n\x0bRecommender\x12\xed\x01\n\x13ListRecommendations\x12\x37.google.cloud.recommender.v1.ListRecommendationsRequest\x1a\x38.google.cloud.recommender.v1.ListRecommendationsResponse"c\x82\xd3\xe4\x93\x02\x44\x12\x42/v1/{parent=projects/*/locations/*/recommenders/*}/recommendations\xda\x41\x06parent\xda\x41\rparent,filter\x12\xca\x01\n\x11GetRecommendation\x12\x35.google.cloud.recommender.v1.GetRecommendationRequest\x1a+.google.cloud.recommender.v1.Recommendation"Q\x82\xd3\xe4\x93\x02\x44\x12\x42/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}\xda\x41\x04name\x12\xfd\x01\n\x19MarkRecommendationClaimed\x12=.google.cloud.recommender.v1.MarkRecommendationClaimedRequest\x1a+.google.cloud.recommender.v1.Recommendation"t\x82\xd3\xe4\x93\x02S"N/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*\xda\x41\x18name,state_metadata,etag\x12\x83\x02\n\x1bMarkRecommendationSucceeded\x12?.google.cloud.recommender.v1.MarkRecommendationSucceededRequest\x1a+.google.cloud.recommender.v1.Recommendation"v\x82\xd3\xe4\x93\x02U"P/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*\xda\x41\x18name,state_metadata,etag\x12\xfa\x01\n\x18MarkRecommendationFailed\x12<.google.cloud.recommender.v1.MarkRecommendationFailedRequest\x1a+.google.cloud.recommender.v1.Recommendation"s\x82\xd3\xe4\x93\x02R"M/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*\xda\x41\x18name,state_metadata,etag\x1aN\xca\x41\x1arecommender.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xa2\x01\n\x1f\x63om.google.cloud.recommender.v1B\x10RecommenderProtoP\x01ZFgoogle.golang.org/genproto/googleapis/cloud/recommender/v1;recommender\xa2\x02\x04\x43REC\xaa\x02\x1bGoogle.Cloud.Recommender.V1b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_recommender__v1_dot_proto_dot_recommendation__pb2.DESCRIPTOR,
    ],
)


_LISTRECOMMENDATIONSREQUEST = _descriptor.Descriptor(
    name="ListRecommendationsRequest",
    full_name="google.cloud.recommender.v1.ListRecommendationsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.recommender.v1.ListRecommendationsRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A(\n&recommender.googleapis.com/Recommender",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.cloud.recommender.v1.ListRecommendationsRequest.page_size",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.cloud.recommender.v1.ListRecommendationsRequest.page_token",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.cloud.recommender.v1.ListRecommendationsRequest.filter",
            index=3,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=264,
    serialized_end=421,
)


_LISTRECOMMENDATIONSRESPONSE = _descriptor.Descriptor(
    name="ListRecommendationsResponse",
    full_name="google.cloud.recommender.v1.ListRecommendationsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="recommendations",
            full_name="google.cloud.recommender.v1.ListRecommendationsResponse.recommendations",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.cloud.recommender.v1.ListRecommendationsResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=423,
    serialized_end=547,
)


_GETRECOMMENDATIONREQUEST = _descriptor.Descriptor(
    name="GetRecommendationRequest",
    full_name="google.cloud.recommender.v1.GetRecommendationRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.recommender.v1.GetRecommendationRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A+\n)recommender.googleapis.com/Recommendation",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=549,
    serialized_end=640,
)


_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY = _descriptor.Descriptor(
    name="StateMetadataEntry",
    full_name="google.cloud.recommender.v1.MarkRecommendationClaimedRequest.StateMetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.recommender.v1.MarkRecommendationClaimedRequest.StateMetadataEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.recommender.v1.MarkRecommendationClaimedRequest.StateMetadataEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=869,
    serialized_end=921,
)

_MARKRECOMMENDATIONCLAIMEDREQUEST = _descriptor.Descriptor(
    name="MarkRecommendationClaimedRequest",
    full_name="google.cloud.recommender.v1.MarkRecommendationClaimedRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.recommender.v1.MarkRecommendationClaimedRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A+\n)recommender.googleapis.com/Recommendation",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="state_metadata",
            full_name="google.cloud.recommender.v1.MarkRecommendationClaimedRequest.state_metadata",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.cloud.recommender.v1.MarkRecommendationClaimedRequest.etag",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=643,
    serialized_end=921,
)


_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY = _descriptor.Descriptor(
    name="StateMetadataEntry",
    full_name="google.cloud.recommender.v1.MarkRecommendationSucceededRequest.StateMetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.recommender.v1.MarkRecommendationSucceededRequest.StateMetadataEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.recommender.v1.MarkRecommendationSucceededRequest.StateMetadataEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=869,
    serialized_end=921,
)

_MARKRECOMMENDATIONSUCCEEDEDREQUEST = _descriptor.Descriptor(
    name="MarkRecommendationSucceededRequest",
    full_name="google.cloud.recommender.v1.MarkRecommendationSucceededRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.recommender.v1.MarkRecommendationSucceededRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A+\n)recommender.googleapis.com/Recommendation",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="state_metadata",
            full_name="google.cloud.recommender.v1.MarkRecommendationSucceededRequest.state_metadata",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.cloud.recommender.v1.MarkRecommendationSucceededRequest.etag",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=924,
    serialized_end=1206,
)


_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY = _descriptor.Descriptor(
    name="StateMetadataEntry",
    full_name="google.cloud.recommender.v1.MarkRecommendationFailedRequest.StateMetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.recommender.v1.MarkRecommendationFailedRequest.StateMetadataEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.recommender.v1.MarkRecommendationFailedRequest.StateMetadataEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=869,
    serialized_end=921,
)

_MARKRECOMMENDATIONFAILEDREQUEST = _descriptor.Descriptor(
    name="MarkRecommendationFailedRequest",
    full_name="google.cloud.recommender.v1.MarkRecommendationFailedRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.recommender.v1.MarkRecommendationFailedRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A+\n)recommender.googleapis.com/Recommendation",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="state_metadata",
            full_name="google.cloud.recommender.v1.MarkRecommendationFailedRequest.state_metadata",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.cloud.recommender.v1.MarkRecommendationFailedRequest.etag",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1209,
    serialized_end=1485,
)

_LISTRECOMMENDATIONSRESPONSE.fields_by_name[
    "recommendations"
].message_type = (
    google_dot_cloud_dot_recommender__v1_dot_proto_dot_recommendation__pb2._RECOMMENDATION
)
_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY.containing_type = (
    _MARKRECOMMENDATIONCLAIMEDREQUEST
)
_MARKRECOMMENDATIONCLAIMEDREQUEST.fields_by_name[
    "state_metadata"
].message_type = _MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY
_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY.containing_type = (
    _MARKRECOMMENDATIONSUCCEEDEDREQUEST
)
_MARKRECOMMENDATIONSUCCEEDEDREQUEST.fields_by_name[
    "state_metadata"
].message_type = _MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY
_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY.containing_type = (
    _MARKRECOMMENDATIONFAILEDREQUEST
)
_MARKRECOMMENDATIONFAILEDREQUEST.fields_by_name[
    "state_metadata"
].message_type = _MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY
DESCRIPTOR.message_types_by_name[
    "ListRecommendationsRequest"
] = _LISTRECOMMENDATIONSREQUEST
DESCRIPTOR.message_types_by_name[
    "ListRecommendationsResponse"
] = _LISTRECOMMENDATIONSRESPONSE
DESCRIPTOR.message_types_by_name["GetRecommendationRequest"] = _GETRECOMMENDATIONREQUEST
DESCRIPTOR.message_types_by_name[
    "MarkRecommendationClaimedRequest"
] = _MARKRECOMMENDATIONCLAIMEDREQUEST
DESCRIPTOR.message_types_by_name[
    "MarkRecommendationSucceededRequest"
] = _MARKRECOMMENDATIONSUCCEEDEDREQUEST
DESCRIPTOR.message_types_by_name[
    "MarkRecommendationFailedRequest"
] = _MARKRECOMMENDATIONFAILEDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListRecommendationsRequest = _reflection.GeneratedProtocolMessageType(
    "ListRecommendationsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTRECOMMENDATIONSREQUEST,
        "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2",
        "__doc__": """Request for the ``ListRecommendations`` method.
  Attributes:
      parent:
          Required. The container resource on which to execute the
          request. Acceptable formats:  1. “projects/[PROJECT_NUMBER]/lo
          cations/[LOCATION]/recommenders/[RECOMMENDER_ID]”,  LOCATION
          here refers to GCP Locations:
          https://cloud.google.com/about/locations/
      page_size:
          Optional. The maximum number of results to return from this
          request. Non-positive values are ignored. If not specified,
          the server will determine the number of results to return.
      page_token:
          Optional. If present, retrieves the next batch of results from
          the preceding call to this method. ``page_token`` must be the
          value of ``next_page_token`` from the previous response. The
          values of other method parameters must be identical to those
          in the previous call.
      filter:
          Filter expression to restrict the recommendations returned.
          Supported filter fields: state_info.state Eg:
          \`state_info.state:“DISMISSED” or state_info.state:“FAILED”
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.ListRecommendationsRequest)
    },
)
_sym_db.RegisterMessage(ListRecommendationsRequest)

ListRecommendationsResponse = _reflection.GeneratedProtocolMessageType(
    "ListRecommendationsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTRECOMMENDATIONSRESPONSE,
        "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2",
        "__doc__": """Response to the ``ListRecommendations`` method.
  Attributes:
      recommendations:
          The set of recommendations for the ``parent`` resource.
      next_page_token:
          A token that can be used to request the next page of results.
          This field is empty if there are no additional results.  ..
          [1]    a-z0-9  .. [2]    a-z0-9  .. [3]    a-z0-9
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.ListRecommendationsResponse)
    },
)
_sym_db.RegisterMessage(ListRecommendationsResponse)

GetRecommendationRequest = _reflection.GeneratedProtocolMessageType(
    "GetRecommendationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETRECOMMENDATIONREQUEST,
        "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2",
        "__doc__": """Request to the ``GetRecommendation`` method.
  Attributes:
      name:
          Required. Name of the recommendation.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.GetRecommendationRequest)
    },
)
_sym_db.RegisterMessage(GetRecommendationRequest)

MarkRecommendationClaimedRequest = _reflection.GeneratedProtocolMessageType(
    "MarkRecommendationClaimedRequest",
    (_message.Message,),
    {
        "StateMetadataEntry": _reflection.GeneratedProtocolMessageType(
            "StateMetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY,
                "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.MarkRecommendationClaimedRequest.StateMetadataEntry)
            },
        ),
        "DESCRIPTOR": _MARKRECOMMENDATIONCLAIMEDREQUEST,
        "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2",
        "__doc__": """Request for the ``MarkRecommendationClaimed`` Method.
  Attributes:
      name:
          Required. Name of the recommendation.
      state_metadata:
          State properties to include with this state. Overwrites any
          existing ``state_metadata``. Keys must match the regex ``/
          [3]_[a-z0-9_.-]{0,62}/``. Values must match the regex
          ``/^[a-zA-Z0-9_./-]{0,255}/``.
      etag:
          Required. Fingerprint of the Recommendation. Provides
          optimistic locking.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.MarkRecommendationClaimedRequest)
    },
)
_sym_db.RegisterMessage(MarkRecommendationClaimedRequest)
_sym_db.RegisterMessage(MarkRecommendationClaimedRequest.StateMetadataEntry)

MarkRecommendationSucceededRequest = _reflection.GeneratedProtocolMessageType(
    "MarkRecommendationSucceededRequest",
    (_message.Message,),
    {
        "StateMetadataEntry": _reflection.GeneratedProtocolMessageType(
            "StateMetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY,
                "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.MarkRecommendationSucceededRequest.StateMetadataEntry)
            },
        ),
        "DESCRIPTOR": _MARKRECOMMENDATIONSUCCEEDEDREQUEST,
        "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2",
        "__doc__": """Request for the ``MarkRecommendationSucceeded`` Method.
  Attributes:
      name:
          Required. Name of the recommendation.
      state_metadata:
          State properties to include with this state. Overwrites any
          existing ``state_metadata``. Keys must match the regex ``/
          [2]_[a-z0-9_.-]{0,62}/``. Values must match the regex
          ``/^[a-zA-Z0-9_./-]{0,255}/``.
      etag:
          Required. Fingerprint of the Recommendation. Provides
          optimistic locking.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.MarkRecommendationSucceededRequest)
    },
)
_sym_db.RegisterMessage(MarkRecommendationSucceededRequest)
_sym_db.RegisterMessage(MarkRecommendationSucceededRequest.StateMetadataEntry)

MarkRecommendationFailedRequest = _reflection.GeneratedProtocolMessageType(
    "MarkRecommendationFailedRequest",
    (_message.Message,),
    {
        "StateMetadataEntry": _reflection.GeneratedProtocolMessageType(
            "StateMetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY,
                "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.MarkRecommendationFailedRequest.StateMetadataEntry)
            },
        ),
        "DESCRIPTOR": _MARKRECOMMENDATIONFAILEDREQUEST,
        "__module__": "google.cloud.recommender_v1.proto.recommender_service_pb2",
        "__doc__": """Request for the ``MarkRecommendationFailed`` Method.
  Attributes:
      name:
          Required. Name of the recommendation.
      state_metadata:
          State properties to include with this state. Overwrites any
          existing ``state_metadata``. Keys must match the regex ``/
          [1]_[a-z0-9_.-]{0,62}/``. Values must match the regex
          ``/^[a-zA-Z0-9_./-]{0,255}/``.
      etag:
          Required. Fingerprint of the Recommendation. Provides
          optimistic locking.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.MarkRecommendationFailedRequest)
    },
)
_sym_db.RegisterMessage(MarkRecommendationFailedRequest)
_sym_db.RegisterMessage(MarkRecommendationFailedRequest.StateMetadataEntry)


DESCRIPTOR._options = None
_LISTRECOMMENDATIONSREQUEST.fields_by_name["parent"]._options = None
_LISTRECOMMENDATIONSREQUEST.fields_by_name["page_size"]._options = None
_LISTRECOMMENDATIONSREQUEST.fields_by_name["page_token"]._options = None
_GETRECOMMENDATIONREQUEST.fields_by_name["name"]._options = None
_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY._options = None
_MARKRECOMMENDATIONCLAIMEDREQUEST.fields_by_name["name"]._options = None
_MARKRECOMMENDATIONCLAIMEDREQUEST.fields_by_name["etag"]._options = None
_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY._options = None
_MARKRECOMMENDATIONSUCCEEDEDREQUEST.fields_by_name["name"]._options = None
_MARKRECOMMENDATIONSUCCEEDEDREQUEST.fields_by_name["etag"]._options = None
_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY._options = None
_MARKRECOMMENDATIONFAILEDREQUEST.fields_by_name["name"]._options = None
_MARKRECOMMENDATIONFAILEDREQUEST.fields_by_name["etag"]._options = None

_RECOMMENDER = _descriptor.ServiceDescriptor(
    name="Recommender",
    full_name="google.cloud.recommender.v1.Recommender",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\032recommender.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform",
    serialized_start=1488,
    serialized_end=2797,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListRecommendations",
            full_name="google.cloud.recommender.v1.Recommender.ListRecommendations",
            index=0,
            containing_service=None,
            input_type=_LISTRECOMMENDATIONSREQUEST,
            output_type=_LISTRECOMMENDATIONSRESPONSE,
            serialized_options=b"\202\323\344\223\002D\022B/v1/{parent=projects/*/locations/*/recommenders/*}/recommendations\332A\006parent\332A\rparent,filter",
        ),
        _descriptor.MethodDescriptor(
            name="GetRecommendation",
            full_name="google.cloud.recommender.v1.Recommender.GetRecommendation",
            index=1,
            containing_service=None,
            input_type=_GETRECOMMENDATIONREQUEST,
            output_type=google_dot_cloud_dot_recommender__v1_dot_proto_dot_recommendation__pb2._RECOMMENDATION,
            serialized_options=b"\202\323\344\223\002D\022B/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}\332A\004name",
        ),
        _descriptor.MethodDescriptor(
            name="MarkRecommendationClaimed",
            full_name="google.cloud.recommender.v1.Recommender.MarkRecommendationClaimed",
            index=2,
            containing_service=None,
            input_type=_MARKRECOMMENDATIONCLAIMEDREQUEST,
            output_type=google_dot_cloud_dot_recommender__v1_dot_proto_dot_recommendation__pb2._RECOMMENDATION,
            serialized_options=b'\202\323\344\223\002S"N/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\001*\332A\030name,state_metadata,etag',
        ),
        _descriptor.MethodDescriptor(
            name="MarkRecommendationSucceeded",
            full_name="google.cloud.recommender.v1.Recommender.MarkRecommendationSucceeded",
            index=3,
            containing_service=None,
            input_type=_MARKRECOMMENDATIONSUCCEEDEDREQUEST,
            output_type=google_dot_cloud_dot_recommender__v1_dot_proto_dot_recommendation__pb2._RECOMMENDATION,
            serialized_options=b'\202\323\344\223\002U"P/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\001*\332A\030name,state_metadata,etag',
        ),
        _descriptor.MethodDescriptor(
            name="MarkRecommendationFailed",
            full_name="google.cloud.recommender.v1.Recommender.MarkRecommendationFailed",
            index=4,
            containing_service=None,
            input_type=_MARKRECOMMENDATIONFAILEDREQUEST,
            output_type=google_dot_cloud_dot_recommender__v1_dot_proto_dot_recommendation__pb2._RECOMMENDATION,
            serialized_options=b'\202\323\344\223\002R"M/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markFailed:\001*\332A\030name,state_metadata,etag',
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_RECOMMENDER)

DESCRIPTOR.services_by_name["Recommender"] = _RECOMMENDER

# @@protoc_insertion_point(module_scope)
