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
# source: google/cloud/recommender_v1/proto/insight.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/recommender_v1/proto/insight.proto",
    package="google.cloud.recommender.v1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.recommender.v1B\014InsightProtoP\001ZFgoogle.golang.org/genproto/googleapis/cloud/recommender/v1;recommender\242\002\004CREC\252\002\033Google.Cloud.Recommender.V1\352Am\n&recommender.googleapis.com/InsightType\022Cprojects/{project}/locations/{location}/insightTypes/{insight_type}",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n/google/cloud/recommender_v1/proto/insight.proto\x12\x1bgoogle.cloud.recommender.v1\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x81\x06\n\x07Insight\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x18\n\x10target_resources\x18\t \x03(\t\x12\x17\n\x0finsight_subtype\x18\n \x01(\t\x12(\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x35\n\x11last_refresh_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x12observation_period\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x41\n\nstate_info\x18\x06 \x01(\x0b\x32-.google.cloud.recommender.v1.InsightStateInfo\x12?\n\x08\x63\x61tegory\x18\x07 \x01(\x0e\x32-.google.cloud.recommender.v1.Insight.Category\x12\x0c\n\x04\x65tag\x18\x0b \x01(\t\x12`\n\x1a\x61ssociated_recommendations\x18\x08 \x03(\x0b\x32<.google.cloud.recommender.v1.Insight.RecommendationReference\x1a\x31\n\x17RecommendationReference\x12\x16\n\x0erecommendation\x18\x01 \x01(\t"`\n\x08\x43\x61tegory\x12\x18\n\x14\x43\x41TEGORY_UNSPECIFIED\x10\x00\x12\x08\n\x04\x43OST\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\x0f\n\x0bPERFORMANCE\x10\x03\x12\x11\n\rMANAGEABILITY\x10\x04:\x7f\xea\x41|\n"recommender.googleapis.com/Insight\x12Vprojects/{project}/locations/{location}/insightTypes/{insight_type}/insights/{insight}"\xaf\x02\n\x10InsightStateInfo\x12\x42\n\x05state\x18\x01 \x01(\x0e\x32\x33.google.cloud.recommender.v1.InsightStateInfo.State\x12X\n\x0estate_metadata\x18\x02 \x03(\x0b\x32@.google.cloud.recommender.v1.InsightStateInfo.StateMetadataEntry\x1a\x34\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"G\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x02\x12\r\n\tDISMISSED\x10\x03\x42\x8e\x02\n\x1f\x63om.google.cloud.recommender.v1B\x0cInsightProtoP\x01ZFgoogle.golang.org/genproto/googleapis/cloud/recommender/v1;recommender\xa2\x02\x04\x43REC\xaa\x02\x1bGoogle.Cloud.Recommender.V1\xea\x41m\n&recommender.googleapis.com/InsightType\x12\x43projects/{project}/locations/{location}/insightTypes/{insight_type}b\x06proto3',
    dependencies=[
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_INSIGHT_CATEGORY = _descriptor.EnumDescriptor(
    name="Category",
    full_name="google.cloud.recommender.v1.Insight.Category",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CATEGORY_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COST",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SECURITY",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERFORMANCE",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MANAGEABILITY",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=747,
    serialized_end=843,
)
_sym_db.RegisterEnumDescriptor(_INSIGHT_CATEGORY)

_INSIGHTSTATEINFO_STATE = _descriptor.EnumDescriptor(
    name="State",
    full_name="google.cloud.recommender.v1.InsightStateInfo.State",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STATE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACTIVE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACCEPTED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DISMISSED",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1207,
    serialized_end=1278,
)
_sym_db.RegisterEnumDescriptor(_INSIGHTSTATEINFO_STATE)


_INSIGHT_RECOMMENDATIONREFERENCE = _descriptor.Descriptor(
    name="RecommendationReference",
    full_name="google.cloud.recommender.v1.Insight.RecommendationReference",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="recommendation",
            full_name="google.cloud.recommender.v1.Insight.RecommendationReference.recommendation",
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
            create_key=_descriptor._internal_create_key,
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
    serialized_start=696,
    serialized_end=745,
)

_INSIGHT = _descriptor.Descriptor(
    name="Insight",
    full_name="google.cloud.recommender.v1.Insight",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.recommender.v1.Insight.name",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.cloud.recommender.v1.Insight.description",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="target_resources",
            full_name="google.cloud.recommender.v1.Insight.target_resources",
            index=2,
            number=9,
            type=9,
            cpp_type=9,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="insight_subtype",
            full_name="google.cloud.recommender.v1.Insight.insight_subtype",
            index=3,
            number=10,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="content",
            full_name="google.cloud.recommender.v1.Insight.content",
            index=4,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="last_refresh_time",
            full_name="google.cloud.recommender.v1.Insight.last_refresh_time",
            index=5,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="observation_period",
            full_name="google.cloud.recommender.v1.Insight.observation_period",
            index=6,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="state_info",
            full_name="google.cloud.recommender.v1.Insight.state_info",
            index=7,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="category",
            full_name="google.cloud.recommender.v1.Insight.category",
            index=8,
            number=7,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.cloud.recommender.v1.Insight.etag",
            index=9,
            number=11,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="associated_recommendations",
            full_name="google.cloud.recommender.v1.Insight.associated_recommendations",
            index=10,
            number=8,
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
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _INSIGHT_RECOMMENDATIONREFERENCE,
    ],
    enum_types=[
        _INSIGHT_CATEGORY,
    ],
    serialized_options=b'\352A|\n"recommender.googleapis.com/Insight\022Vprojects/{project}/locations/{location}/insightTypes/{insight_type}/insights/{insight}',
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=203,
    serialized_end=972,
)


_INSIGHTSTATEINFO_STATEMETADATAENTRY = _descriptor.Descriptor(
    name="StateMetadataEntry",
    full_name="google.cloud.recommender.v1.InsightStateInfo.StateMetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.recommender.v1.InsightStateInfo.StateMetadataEntry.key",
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.recommender.v1.InsightStateInfo.StateMetadataEntry.value",
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
            create_key=_descriptor._internal_create_key,
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
    serialized_start=1153,
    serialized_end=1205,
)

_INSIGHTSTATEINFO = _descriptor.Descriptor(
    name="InsightStateInfo",
    full_name="google.cloud.recommender.v1.InsightStateInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="state",
            full_name="google.cloud.recommender.v1.InsightStateInfo.state",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="state_metadata",
            full_name="google.cloud.recommender.v1.InsightStateInfo.state_metadata",
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
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _INSIGHTSTATEINFO_STATEMETADATAENTRY,
    ],
    enum_types=[
        _INSIGHTSTATEINFO_STATE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=975,
    serialized_end=1278,
)

_INSIGHT_RECOMMENDATIONREFERENCE.containing_type = _INSIGHT
_INSIGHT.fields_by_name[
    "content"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INSIGHT.fields_by_name[
    "last_refresh_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INSIGHT.fields_by_name[
    "observation_period"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_INSIGHT.fields_by_name["state_info"].message_type = _INSIGHTSTATEINFO
_INSIGHT.fields_by_name["category"].enum_type = _INSIGHT_CATEGORY
_INSIGHT.fields_by_name[
    "associated_recommendations"
].message_type = _INSIGHT_RECOMMENDATIONREFERENCE
_INSIGHT_CATEGORY.containing_type = _INSIGHT
_INSIGHTSTATEINFO_STATEMETADATAENTRY.containing_type = _INSIGHTSTATEINFO
_INSIGHTSTATEINFO.fields_by_name["state"].enum_type = _INSIGHTSTATEINFO_STATE
_INSIGHTSTATEINFO.fields_by_name[
    "state_metadata"
].message_type = _INSIGHTSTATEINFO_STATEMETADATAENTRY
_INSIGHTSTATEINFO_STATE.containing_type = _INSIGHTSTATEINFO
DESCRIPTOR.message_types_by_name["Insight"] = _INSIGHT
DESCRIPTOR.message_types_by_name["InsightStateInfo"] = _INSIGHTSTATEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Insight = _reflection.GeneratedProtocolMessageType(
    "Insight",
    (_message.Message,),
    {
        "RecommendationReference": _reflection.GeneratedProtocolMessageType(
            "RecommendationReference",
            (_message.Message,),
            {
                "DESCRIPTOR": _INSIGHT_RECOMMENDATIONREFERENCE,
                "__module__": "google.cloud.recommender_v1.proto.insight_pb2",
                "__doc__": """Reference to an associated recommendation.
    
    Attributes:
        recommendation:
            Recommendation resource name, e.g. projects/[PROJECT_NUMBER]/l
            ocations/[LOCATION]/recommenders/[RECOMMENDER_ID]/recommendati
            ons/[RECOMMENDATION_ID]
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.Insight.RecommendationReference)
            },
        ),
        "DESCRIPTOR": _INSIGHT,
        "__module__": "google.cloud.recommender_v1.proto.insight_pb2",
        "__doc__": """An insight along with the information used to derive the insight. The
  insight may have associated recomendations as well.
  
  Attributes:
      name:
          Name of the insight.
      description:
          Free-form human readable summary in English. The maximum
          length is 500 characters.
      target_resources:
          Fully qualified resource names that this insight is targeting.
      insight_subtype:
          Insight subtype. Insight content schema will be stable for a
          given subtype.
      content:
          A struct of custom fields to explain the insight. Example:
          “grantedPermissionsCount”: “1000”
      last_refresh_time:
          Timestamp of the latest data used to generate the insight.
      observation_period:
          Observation period that led to the insight. The source data
          used to generate the insight ends at last_refresh_time and
          begins at (last_refresh_time - observation_period).
      state_info:
          Information state and metadata.
      category:
          Category being targeted by the insight.
      etag:
          Fingerprint of the Insight. Provides optimistic locking when
          updating states.
      associated_recommendations:
          Recommendations derived from this insight.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.Insight)
    },
)
_sym_db.RegisterMessage(Insight)
_sym_db.RegisterMessage(Insight.RecommendationReference)

InsightStateInfo = _reflection.GeneratedProtocolMessageType(
    "InsightStateInfo",
    (_message.Message,),
    {
        "StateMetadataEntry": _reflection.GeneratedProtocolMessageType(
            "StateMetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _INSIGHTSTATEINFO_STATEMETADATAENTRY,
                "__module__": "google.cloud.recommender_v1.proto.insight_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.InsightStateInfo.StateMetadataEntry)
            },
        ),
        "DESCRIPTOR": _INSIGHTSTATEINFO,
        "__module__": "google.cloud.recommender_v1.proto.insight_pb2",
        "__doc__": """Information related to insight state.
  
  Attributes:
      state:
          Insight state.
      state_metadata:
          A map of metadata for the state, provided by user or
          automations systems.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.recommender.v1.InsightStateInfo)
    },
)
_sym_db.RegisterMessage(InsightStateInfo)
_sym_db.RegisterMessage(InsightStateInfo.StateMetadataEntry)


DESCRIPTOR._options = None
_INSIGHT._options = None
_INSIGHTSTATEINFO_STATEMETADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
