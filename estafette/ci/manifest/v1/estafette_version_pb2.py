# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: estafette/ci/manifest/v1/estafette_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from estafette.ci.manifest.v1 import estafette_custom_version_pb2 as estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__custom__version__pb2
from estafette.ci.manifest.v1 import estafette_semver_version_pb2 as estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__semver__version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='estafette/ci/manifest/v1/estafette_version.proto',
  package='estafette.ci.manifest.v1',
  syntax='proto3',
  serialized_options=_b('\n\034com.estafette.ci.manifest.v1P\001Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\252\002\030Estafette.Ci.Manifest.V1'),
  serialized_pb=_b('\n0estafette/ci/manifest/v1/estafette_version.proto\x12\x18\x65stafette.ci.manifest.v1\x1a\x37\x65stafette/ci/manifest/v1/estafette_custom_version.proto\x1a\x37\x65stafette/ci/manifest/v1/estafette_semver_version.proto\"\x96\x01\n\x10\x45stafetteVersion\x12@\n\x06semver\x18\x01 \x01(\x0b\x32\x30.estafette.ci.manifest.v1.EstafetteSemverVersion\x12@\n\x06\x63ustom\x18\x02 \x01(\x0b\x32\x30.estafette.ci.manifest.v1.EstafetteCustomVersionBx\n\x1c\x63om.estafette.ci.manifest.v1P\x01Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\xaa\x02\x18\x45stafette.Ci.Manifest.V1b\x06proto3')
  ,
  dependencies=[estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__custom__version__pb2.DESCRIPTOR,estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__semver__version__pb2.DESCRIPTOR,])




_ESTAFETTEVERSION = _descriptor.Descriptor(
  name='EstafetteVersion',
  full_name='estafette.ci.manifest.v1.EstafetteVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='semver', full_name='estafette.ci.manifest.v1.EstafetteVersion.semver', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom', full_name='estafette.ci.manifest.v1.EstafetteVersion.custom', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=193,
  serialized_end=343,
)

_ESTAFETTEVERSION.fields_by_name['semver'].message_type = estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__semver__version__pb2._ESTAFETTESEMVERVERSION
_ESTAFETTEVERSION.fields_by_name['custom'].message_type = estafette_dot_ci_dot_manifest_dot_v1_dot_estafette__custom__version__pb2._ESTAFETTECUSTOMVERSION
DESCRIPTOR.message_types_by_name['EstafetteVersion'] = _ESTAFETTEVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteVersion = _reflection.GeneratedProtocolMessageType('EstafetteVersion', (_message.Message,), dict(
  DESCRIPTOR = _ESTAFETTEVERSION,
  __module__ = 'estafette.ci.manifest.v1.estafette_version_pb2'
  # @@protoc_insertion_point(class_scope:estafette.ci.manifest.v1.EstafetteVersion)
  ))
_sym_db.RegisterMessage(EstafetteVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
