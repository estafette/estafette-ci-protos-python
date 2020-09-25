# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: estafette/ci/contracts/v1/release_target.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from estafette.ci.contracts.v1 import release_pb2 as estafette_dot_ci_dot_contracts_dot_v1_dot_release__pb2
from estafette.ci.manifest.v1 import estafette_release_action_pb2 as estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__release__action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='estafette/ci/contracts/v1/release_target.proto',
  package='estafette.ci.contracts.v1',
  syntax='proto3',
  serialized_options=_b('\n\035com.estafette.ci.contracts.v1P\001Z<github.com/estafette/estafette-ci-protos-golang/contracts/v1\252\002\031Estafette.Ci.Contracts.V1'),
  serialized_pb=_b('\n.estafette/ci/contracts/v1/release_target.proto\x12\x19\x65stafette.ci.contracts.v1\x1a\'estafette/ci/contracts/v1/release.proto\x1a\x37\x65stafette/ci/manifest/v1/estafette_release_action.proto\"\x9d\x01\n\rReleaseTarget\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x41\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x30.estafette.ci.manifest.v1.EstafetteReleaseAction\x12;\n\x0f\x61\x63tive_releases\x18\x03 \x03(\x0b\x32\".estafette.ci.contracts.v1.ReleaseB{\n\x1d\x63om.estafette.ci.contracts.v1P\x01Z<github.com/estafette/estafette-ci-protos-golang/contracts/v1\xaa\x02\x19\x45stafette.Ci.Contracts.V1b\x06proto3')
  ,
  dependencies=[estafette_dot_ci_dot_contracts_dot_v1_dot_release__pb2.DESCRIPTOR,estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__release__action__pb2.DESCRIPTOR,])




_RELEASETARGET = _descriptor.Descriptor(
  name='ReleaseTarget',
  full_name='estafette.ci.contracts.v1.ReleaseTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='estafette.ci.contracts.v1.ReleaseTarget.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='estafette.ci.contracts.v1.ReleaseTarget.actions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_releases', full_name='estafette.ci.contracts.v1.ReleaseTarget.active_releases', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=176,
  serialized_end=333,
)

_RELEASETARGET.fields_by_name['actions'].message_type = estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__release__action__pb2._ESTAFETTERELEASEACTION
_RELEASETARGET.fields_by_name['active_releases'].message_type = estafette_dot_ci_dot_contracts_dot_v1_dot_release__pb2._RELEASE
DESCRIPTOR.message_types_by_name['ReleaseTarget'] = _RELEASETARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReleaseTarget = _reflection.GeneratedProtocolMessageType('ReleaseTarget', (_message.Message,), {
  'DESCRIPTOR' : _RELEASETARGET,
  '__module__' : 'estafette.ci.contracts.v1.release_target_pb2'
  # @@protoc_insertion_point(class_scope:estafette.ci.contracts.v1.ReleaseTarget)
  })
_sym_db.RegisterMessage(ReleaseTarget)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)