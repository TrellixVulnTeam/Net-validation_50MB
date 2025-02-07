# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ip4over4.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protocol_pb2
import ip4_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ip4over4.proto',
  package='OstProto',
  serialized_pb=_b('\n\x0eip4over4.proto\x12\x08OstProto\x1a\x0eprotocol.proto\x1a\tip4.proto\"\x10\n\x08Ip4over4*\x04\x08\x01\x10\x03:4\n\tip4_outer\x12\x12.OstProto.Ip4over4\x18\x01 \x01(\x0b\x32\r.OstProto.Ip4:4\n\tip4_inner\x12\x12.OstProto.Ip4over4\x18\x02 \x01(\x0b\x32\r.OstProto.Ip4:9\n\x08ip4over4\x12\x12.OstProto.Protocol\x18\xb1\x02 \x01(\x0b\x32\x12.OstProto.Ip4over4')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,ip4_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


IP4_OUTER_FIELD_NUMBER = 1
ip4_outer = _descriptor.FieldDescriptor(
  name='ip4_outer', full_name='OstProto.ip4_outer', index=0,
  number=1, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
IP4_INNER_FIELD_NUMBER = 2
ip4_inner = _descriptor.FieldDescriptor(
  name='ip4_inner', full_name='OstProto.ip4_inner', index=1,
  number=2, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
IP4OVER4_FIELD_NUMBER = 305
ip4over4 = _descriptor.FieldDescriptor(
  name='ip4over4', full_name='OstProto.ip4over4', index=2,
  number=305, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_IP4OVER4 = _descriptor.Descriptor(
  name='Ip4over4',
  full_name='OstProto.Ip4over4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(1, 3), ],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['Ip4over4'] = _IP4OVER4
DESCRIPTOR.extensions_by_name['ip4_outer'] = ip4_outer
DESCRIPTOR.extensions_by_name['ip4_inner'] = ip4_inner
DESCRIPTOR.extensions_by_name['ip4over4'] = ip4over4

Ip4over4 = _reflection.GeneratedProtocolMessageType('Ip4over4', (_message.Message,), dict(
  DESCRIPTOR = _IP4OVER4,
  __module__ = 'ip4over4_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.Ip4over4)
  ))
_sym_db.RegisterMessage(Ip4over4)

ip4_outer.message_type = ip4_pb2._IP4
Ip4over4.RegisterExtension(ip4_outer)
ip4_inner.message_type = ip4_pb2._IP4
Ip4over4.RegisterExtension(ip4_inner)
ip4over4.message_type = _IP4OVER4
protocol_pb2.Protocol.RegisterExtension(ip4over4)

# @@protoc_insertion_point(module_scope)
