# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: build.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import label_pb2 as label__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='build.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x62uild.proto\x12\x0c\x63ontracts.v1\x1a\x0blabel.proto\"\xa9\x02\n\x05\x42uild\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0brepo_source\x18\x02 \x01(\t\x12\x12\n\nrepo_owner\x18\x03 \x01(\t\x12\x11\n\trepo_name\x18\x04 \x01(\t\x12\x13\n\x0brepo_branch\x18\x05 \x01(\t\x12\x15\n\rrepo_revision\x18\x06 \x01(\t\x12\x15\n\rbuild_version\x18\x07 \x01(\t\x12\x14\n\x0c\x62uild_status\x18\x08 \x01(\t\x12#\n\x06labels\x18\t \x03(\x0b\x32\x13.contracts.v1.Label\"Z\n\x06\x43orpus\x12\r\n\tUNIVERSAL\x10\x00\x12\x07\n\x03WEB\x10\x01\x12\n\n\x06IMAGES\x10\x02\x12\t\n\x05LOCAL\x10\x03\x12\x08\n\x04NEWS\x10\x04\x12\x0c\n\x08PRODUCTS\x10\x05\x12\t\n\x05VIDEO\x10\x06\x62\x06proto3')
  ,
  dependencies=[label__pb2.DESCRIPTOR,])



_BUILD_CORPUS = _descriptor.EnumDescriptor(
  name='Corpus',
  full_name='contracts.v1.Build.Corpus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNIVERSAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGES', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEWS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCTS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=250,
  serialized_end=340,
)
_sym_db.RegisterEnumDescriptor(_BUILD_CORPUS)


_BUILD = _descriptor.Descriptor(
  name='Build',
  full_name='contracts.v1.Build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='contracts.v1.Build.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_source', full_name='contracts.v1.Build.repo_source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_owner', full_name='contracts.v1.Build.repo_owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='contracts.v1.Build.repo_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_branch', full_name='contracts.v1.Build.repo_branch', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_revision', full_name='contracts.v1.Build.repo_revision', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_version', full_name='contracts.v1.Build.build_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_status', full_name='contracts.v1.Build.build_status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='contracts.v1.Build.labels', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BUILD_CORPUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=340,
)

_BUILD.fields_by_name['labels'].message_type = label__pb2._LABEL
_BUILD_CORPUS.containing_type = _BUILD
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), dict(
  DESCRIPTOR = _BUILD,
  __module__ = 'build_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.Build)
  ))
_sym_db.RegisterMessage(Build)


# @@protoc_insertion_point(module_scope)
