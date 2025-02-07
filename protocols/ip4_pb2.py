# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ip4.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ip4.proto',
  package='OstProto',
  serialized_pb=_b('\n\tip4.proto\x12\x08OstProto\x1a\x0eprotocol.proto\"\x8a\x05\n\x03Ip4\x12\x17\n\x0fis_override_ver\x18\x01 \x01(\x08\x12\x1a\n\x12is_override_hdrlen\x18\x02 \x01(\x08\x12\x1a\n\x12is_override_totlen\x18\x03 \x01(\x08\x12\x19\n\x11is_override_proto\x18\x1e \x01(\x08\x12\x19\n\x11is_override_cksum\x18\x04 \x01(\x08\x12\x16\n\nver_hdrlen\x18\x05 \x01(\r:\x02\x36\x39\x12\x0b\n\x03tos\x18\x06 \x01(\r\x12\x0e\n\x06totlen\x18\x07 \x01(\r\x12\x10\n\x02id\x18\x08 \x01(\r:\x04\x31\x32\x33\x34\x12\r\n\x05\x66lags\x18\t \x01(\r\x12\x10\n\x08\x66rag_ofs\x18\n \x01(\r\x12\x10\n\x03ttl\x18\x0b \x01(\r:\x03\x31\x32\x37\x12\r\n\x05proto\x18\x0c \x01(\r\x12\r\n\x05\x63ksum\x18\r \x01(\r\x12\x0e\n\x06src_ip\x18\x0e \x01(\x07\x12\x39\n\x0bsrc_ip_mode\x18\x0f \x01(\x0e\x32\x18.OstProto.Ip4.IpAddrMode:\ne_im_fixed\x12\x18\n\x0csrc_ip_count\x18\x10 \x01(\r:\x02\x31\x36\x12\x1f\n\x0bsrc_ip_mask\x18\x11 \x01(\x07:\n4294967040\x12\x0e\n\x06\x64st_ip\x18\x12 \x01(\x07\x12\x39\n\x0b\x64st_ip_mode\x18\x13 \x01(\x0e\x32\x18.OstProto.Ip4.IpAddrMode:\ne_im_fixed\x12\x18\n\x0c\x64st_ip_count\x18\x14 \x01(\r:\x02\x31\x36\x12\x1f\n\x0b\x64st_ip_mask\x18\x15 \x01(\x07:\n4294967040\"X\n\nIpAddrMode\x12\x0e\n\ne_im_fixed\x10\x00\x12\x11\n\re_im_inc_host\x10\x01\x12\x11\n\re_im_dec_host\x10\x02\x12\x14\n\x10\x65_im_random_host\x10\x03:/\n\x03ip4\x12\x12.OstProto.Protocol\x18\xad\x02 \x01(\x0b\x32\r.OstProto.Ip4')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


IP4_FIELD_NUMBER = 301
ip4 = _descriptor.FieldDescriptor(
  name='ip4', full_name='OstProto.ip4', index=0,
  number=301, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

_IP4_IPADDRMODE = _descriptor.EnumDescriptor(
  name='IpAddrMode',
  full_name='OstProto.Ip4.IpAddrMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='e_im_fixed', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='e_im_inc_host', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='e_im_dec_host', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='e_im_random_host', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=602,
  serialized_end=690,
)
_sym_db.RegisterEnumDescriptor(_IP4_IPADDRMODE)


_IP4 = _descriptor.Descriptor(
  name='Ip4',
  full_name='OstProto.Ip4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_override_ver', full_name='OstProto.Ip4.is_override_ver', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_hdrlen', full_name='OstProto.Ip4.is_override_hdrlen', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_totlen', full_name='OstProto.Ip4.is_override_totlen', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_proto', full_name='OstProto.Ip4.is_override_proto', index=3,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_cksum', full_name='OstProto.Ip4.is_override_cksum', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ver_hdrlen', full_name='OstProto.Ip4.ver_hdrlen', index=5,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=69,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tos', full_name='OstProto.Ip4.tos', index=6,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totlen', full_name='OstProto.Ip4.totlen', index=7,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='OstProto.Ip4.id', index=8,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1234,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='OstProto.Ip4.flags', index=9,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frag_ofs', full_name='OstProto.Ip4.frag_ofs', index=10,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='OstProto.Ip4.ttl', index=11,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=127,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proto', full_name='OstProto.Ip4.proto', index=12,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cksum', full_name='OstProto.Ip4.cksum', index=13,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='src_ip', full_name='OstProto.Ip4.src_ip', index=14,
      number=14, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='src_ip_mode', full_name='OstProto.Ip4.src_ip_mode', index=15,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='src_ip_count', full_name='OstProto.Ip4.src_ip_count', index=16,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='src_ip_mask', full_name='OstProto.Ip4.src_ip_mask', index=17,
      number=17, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=4294967040,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dst_ip', full_name='OstProto.Ip4.dst_ip', index=18,
      number=18, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dst_ip_mode', full_name='OstProto.Ip4.dst_ip_mode', index=19,
      number=19, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dst_ip_count', full_name='OstProto.Ip4.dst_ip_count', index=20,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dst_ip_mask', full_name='OstProto.Ip4.dst_ip_mask', index=21,
      number=21, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=4294967040,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IP4_IPADDRMODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=690,
)

_IP4.fields_by_name['src_ip_mode'].enum_type = _IP4_IPADDRMODE
_IP4.fields_by_name['dst_ip_mode'].enum_type = _IP4_IPADDRMODE
_IP4_IPADDRMODE.containing_type = _IP4
DESCRIPTOR.message_types_by_name['Ip4'] = _IP4
DESCRIPTOR.extensions_by_name['ip4'] = ip4

Ip4 = _reflection.GeneratedProtocolMessageType('Ip4', (_message.Message,), dict(
  DESCRIPTOR = _IP4,
  __module__ = 'ip4_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.Ip4)
  ))
_sym_db.RegisterMessage(Ip4)

ip4.message_type = _IP4
protocol_pb2.Protocol.RegisterExtension(ip4)

# @@protoc_insertion_point(module_scope)
