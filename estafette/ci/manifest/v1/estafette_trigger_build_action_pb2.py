# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: estafette/ci/manifest/v1/estafette_trigger_build_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='estafette/ci/manifest/v1/estafette_trigger_build_action.proto',
  package='estafette.ci.manifest.v1',
  syntax='proto3',
  serialized_options=_b('\n\034com.estafette.ci.manifest.v1P\001Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\252\002\030Estafette.Ci.Manifest.V1'),
  serialized_pb=_b('\n=estafette/ci/manifest/v1/estafette_trigger_build_action.proto\x12\x18\x65stafette.ci.manifest.v1\"-\n\x1b\x45stafetteTriggerBuildAction\x12\x0e\n\x06\x62ranch\x18\x01 \x01(\tBx\n\x1c\x63om.estafette.ci.manifest.v1P\x01Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\xaa\x02\x18\x45stafette.Ci.Manifest.V1b\x06proto3')
)




_ESTAFETTETRIGGERBUILDACTION = _descriptor.Descriptor(
  name='EstafetteTriggerBuildAction',
  full_name='estafette.ci.manifest.v1.EstafetteTriggerBuildAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='branch', full_name='estafette.ci.manifest.v1.EstafetteTriggerBuildAction.branch', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=91,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['EstafetteTriggerBuildAction'] = _ESTAFETTETRIGGERBUILDACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteTriggerBuildAction = _reflection.GeneratedProtocolMessageType('EstafetteTriggerBuildAction', (_message.Message,), {
  'DESCRIPTOR' : _ESTAFETTETRIGGERBUILDACTION,
  '__module__' : 'estafette.ci.manifest.v1.estafette_trigger_build_action_pb2'
  # @@protoc_insertion_point(class_scope:estafette.ci.manifest.v1.EstafetteTriggerBuildAction)
  })
_sym_db.RegisterMessage(EstafetteTriggerBuildAction)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)