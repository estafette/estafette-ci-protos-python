# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: estafette/ci/manifest/v1/estafette_manual_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='estafette/ci/manifest/v1/estafette_manual_event.proto',
  package='estafette.ci.manifest.v1',
  syntax='proto3',
  serialized_options=_b('\n\034com.estafette.ci.manifest.v1P\001Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\252\002\030Estafette.Ci.Manifest.V1'),
  serialized_pb=_b('\n5estafette/ci/manifest/v1/estafette_manual_event.proto\x12\x18\x65stafette.ci.manifest.v1\"\'\n\x14\x45stafetteManualEvent\x12\x0f\n\x07user_id\x18\x01 \x01(\tBx\n\x1c\x63om.estafette.ci.manifest.v1P\x01Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\xaa\x02\x18\x45stafette.Ci.Manifest.V1b\x06proto3')
)




_ESTAFETTEMANUALEVENT = _descriptor.Descriptor(
  name='EstafetteManualEvent',
  full_name='estafette.ci.manifest.v1.EstafetteManualEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='estafette.ci.manifest.v1.EstafetteManualEvent.user_id', index=0,
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
  serialized_start=83,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['EstafetteManualEvent'] = _ESTAFETTEMANUALEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteManualEvent = _reflection.GeneratedProtocolMessageType('EstafetteManualEvent', (_message.Message,), {
  'DESCRIPTOR' : _ESTAFETTEMANUALEVENT,
  '__module__' : 'estafette.ci.manifest.v1.estafette_manual_event_pb2'
  # @@protoc_insertion_point(class_scope:estafette.ci.manifest.v1.EstafetteManualEvent)
  })
_sym_db.RegisterMessage(EstafetteManualEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
