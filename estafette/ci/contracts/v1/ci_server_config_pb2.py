# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: estafette/ci/contracts/v1/ci_server_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='estafette/ci/contracts/v1/ci_server_config.proto',
  package='estafette.ci.contracts.v1',
  syntax='proto3',
  serialized_options=_b('\n\035com.estafette.ci.contracts.v1P\001Z<github.com/estafette/estafette-ci-protos-golang/contracts/v1\252\002\031Estafette.Ci.Contracts.V1'),
  serialized_pb=_b('\n0estafette/ci/contracts/v1/ci_server_config.proto\x12\x19\x65stafette.ci.contracts.v1\"f\n\x0e\x43iServerConfig\x12\x10\n\x08\x62\x61se_url\x18\x01 \x01(\t\x12\x1a\n\x12\x62uilder_events_url\x18\x02 \x01(\t\x12\x15\n\rpost_logs_url\x18\x03 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x04 \x01(\tB{\n\x1d\x63om.estafette.ci.contracts.v1P\x01Z<github.com/estafette/estafette-ci-protos-golang/contracts/v1\xaa\x02\x19\x45stafette.Ci.Contracts.V1b\x06proto3')
)




_CISERVERCONFIG = _descriptor.Descriptor(
  name='CiServerConfig',
  full_name='estafette.ci.contracts.v1.CiServerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_url', full_name='estafette.ci.contracts.v1.CiServerConfig.base_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='builder_events_url', full_name='estafette.ci.contracts.v1.CiServerConfig.builder_events_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='post_logs_url', full_name='estafette.ci.contracts.v1.CiServerConfig.post_logs_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='estafette.ci.contracts.v1.CiServerConfig.api_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['CiServerConfig'] = _CISERVERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CiServerConfig = _reflection.GeneratedProtocolMessageType('CiServerConfig', (_message.Message,), {
  'DESCRIPTOR' : _CISERVERCONFIG,
  '__module__' : 'estafette.ci.contracts.v1.ci_server_config_pb2'
  # @@protoc_insertion_point(class_scope:estafette.ci.contracts.v1.CiServerConfig)
  })
_sym_db.RegisterMessage(CiServerConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
