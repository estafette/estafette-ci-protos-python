# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.v1/estafette_version_params.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.v1/estafette_version_params.proto',
  package='manifest.v1',
  syntax='proto3',
  serialized_options=_b('Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1'),
  serialized_pb=_b('\n*manifest.v1/estafette_version_params.proto\x12\x0bmanifest.v1\"R\n\x16\x45stafetteVersionParams\x12\x16\n\x0e\x61uto_increment\x18\x01 \x01(\x03\x12\x0e\n\x06\x62ranch\x18\x02 \x01(\t\x12\x10\n\x08revision\x18\x03 \x01(\tB@Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1b\x06proto3')
)




_ESTAFETTEVERSIONPARAMS = _descriptor.Descriptor(
  name='EstafetteVersionParams',
  full_name='manifest.v1.EstafetteVersionParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auto_increment', full_name='manifest.v1.EstafetteVersionParams.auto_increment', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='branch', full_name='manifest.v1.EstafetteVersionParams.branch', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision', full_name='manifest.v1.EstafetteVersionParams.revision', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=59,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['EstafetteVersionParams'] = _ESTAFETTEVERSIONPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteVersionParams = _reflection.GeneratedProtocolMessageType('EstafetteVersionParams', (_message.Message,), dict(
  DESCRIPTOR = _ESTAFETTEVERSIONPARAMS,
  __module__ = 'manifest.v1.estafette_version_params_pb2'
  # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteVersionParams)
  ))
_sym_db.RegisterMessage(EstafetteVersionParams)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)