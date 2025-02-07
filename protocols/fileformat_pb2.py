# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fileformat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protocol_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fileformat.proto',
  package='OstProto',
  serialized_pb=_b('\n\x10\x66ileformat.proto\x12\x08OstProto\x1a\x0eprotocol.proto\"\xe1\x01\n\x0c\x46ileMetaData\x12%\n\tfile_type\x18\x01 \x02(\x0e\x32\x12.OstProto.FileType\x12\x1c\n\x14\x66ormat_version_major\x18\x02 \x02(\r\x12\x1c\n\x14\x66ormat_version_minor\x18\x03 \x02(\r\x12\x1f\n\x17\x66ormat_version_revision\x18\x04 \x02(\r\x12\x16\n\x0egenerator_name\x18\x05 \x02(\t\x12\x19\n\x11generator_version\x18\x06 \x02(\t\x12\x1a\n\x12generator_revision\x18\x07 \x02(\t\"\x83\x01\n\x0bPortContent\x12#\n\x0bport_config\x18\x01 \x01(\x0b\x32\x0e.OstProto.Port\x12!\n\x07streams\x18\x02 \x03(\x0b\x32\x10.OstProto.Stream\x12,\n\rdevice_groups\x18\x03 \x03(\x0b\x32\x15.OstProto.DeviceGroup\"b\n\x10PortGroupContent\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12\x13\n\x0bserver_port\x18\x02 \x01(\r\x12$\n\x05ports\x18\x0f \x03(\x0b\x32\x15.OstProto.PortContent\"A\n\x0eSessionContent\x12/\n\x0bport_groups\x18\x01 \x03(\x0b\x32\x1a.OstProto.PortGroupContent\"k\n\x11\x46ileContentMatter\x12+\n\x07streams\x18\x01 \x01(\x0b\x32\x1a.OstProto.StreamConfigList\x12)\n\x07session\x18\n \x01(\x0b\x32\x18.OstProto.SessionContent\"\x8d\x01\n\x04\x46ile\x12\x13\n\x0bmagic_value\x18\x02 \x02(\x0c\x12)\n\tmeta_data\x18\x03 \x02(\x0b\x32\x16.OstProto.FileMetaData\x12-\n\x0e\x63ontent_matter\x18\t \x01(\x0b\x32\x15.OstProto.FileContent\x12\x16\n\x0e\x63hecksum_value\x18\x0f \x02(\x07\"\x1a\n\tFileMagic\x12\r\n\x05value\x18\x02 \x02(\x0c\"0\n\x08\x46ileMeta\x12$\n\x04\x64\x61ta\x18\x03 \x02(\x0b\x32\x16.OstProto.FileMetaData\":\n\x0b\x46ileContent\x12+\n\x06matter\x18\t \x01(\x0b\x32\x1b.OstProto.FileContentMatter\"\x1d\n\x0c\x46ileChecksum\x12\r\n\x05value\x18\x0f \x02(\x07*M\n\x08\x46ileType\x12\x15\n\x11kReservedFileType\x10\x00\x12\x14\n\x10kStreamsFileType\x10\x01\x12\x14\n\x10kSessionFileType\x10\n')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FILETYPE = _descriptor.EnumDescriptor(
  name='FileType',
  full_name='OstProto.FileType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kReservedFileType', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kStreamsFileType', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSessionFileType', index=2, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=997,
  serialized_end=1074,
)
_sym_db.RegisterEnumDescriptor(_FILETYPE)

FileType = enum_type_wrapper.EnumTypeWrapper(_FILETYPE)
kReservedFileType = 0
kStreamsFileType = 1
kSessionFileType = 10



_FILEMETADATA = _descriptor.Descriptor(
  name='FileMetaData',
  full_name='OstProto.FileMetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_type', full_name='OstProto.FileMetaData.file_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format_version_major', full_name='OstProto.FileMetaData.format_version_major', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format_version_minor', full_name='OstProto.FileMetaData.format_version_minor', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format_version_revision', full_name='OstProto.FileMetaData.format_version_revision', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generator_name', full_name='OstProto.FileMetaData.generator_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generator_version', full_name='OstProto.FileMetaData.generator_version', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generator_revision', full_name='OstProto.FileMetaData.generator_revision', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=272,
)


_PORTCONTENT = _descriptor.Descriptor(
  name='PortContent',
  full_name='OstProto.PortContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_config', full_name='OstProto.PortContent.port_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='streams', full_name='OstProto.PortContent.streams', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_groups', full_name='OstProto.PortContent.device_groups', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=406,
)


_PORTGROUPCONTENT = _descriptor.Descriptor(
  name='PortGroupContent',
  full_name='OstProto.PortGroupContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_name', full_name='OstProto.PortGroupContent.server_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_port', full_name='OstProto.PortGroupContent.server_port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ports', full_name='OstProto.PortGroupContent.ports', index=2,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=506,
)


_SESSIONCONTENT = _descriptor.Descriptor(
  name='SessionContent',
  full_name='OstProto.SessionContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_groups', full_name='OstProto.SessionContent.port_groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=573,
)


_FILECONTENTMATTER = _descriptor.Descriptor(
  name='FileContentMatter',
  full_name='OstProto.FileContentMatter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='streams', full_name='OstProto.FileContentMatter.streams', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='OstProto.FileContentMatter.session', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=575,
  serialized_end=682,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='OstProto.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='magic_value', full_name='OstProto.File.magic_value', index=0,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meta_data', full_name='OstProto.File.meta_data', index=1,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_matter', full_name='OstProto.File.content_matter', index=2,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum_value', full_name='OstProto.File.checksum_value', index=3,
      number=15, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=685,
  serialized_end=826,
)


_FILEMAGIC = _descriptor.Descriptor(
  name='FileMagic',
  full_name='OstProto.FileMagic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='OstProto.FileMagic.value', index=0,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=854,
)


_FILEMETA = _descriptor.Descriptor(
  name='FileMeta',
  full_name='OstProto.FileMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='OstProto.FileMeta.data', index=0,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=856,
  serialized_end=904,
)


_FILECONTENT = _descriptor.Descriptor(
  name='FileContent',
  full_name='OstProto.FileContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='matter', full_name='OstProto.FileContent.matter', index=0,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=906,
  serialized_end=964,
)


_FILECHECKSUM = _descriptor.Descriptor(
  name='FileChecksum',
  full_name='OstProto.FileChecksum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='OstProto.FileChecksum.value', index=0,
      number=15, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=966,
  serialized_end=995,
)

_FILEMETADATA.fields_by_name['file_type'].enum_type = _FILETYPE
_PORTCONTENT.fields_by_name['port_config'].message_type = protocol_pb2._PORT
_PORTCONTENT.fields_by_name['streams'].message_type = protocol_pb2._STREAM
_PORTCONTENT.fields_by_name['device_groups'].message_type = protocol_pb2._DEVICEGROUP
_PORTGROUPCONTENT.fields_by_name['ports'].message_type = _PORTCONTENT
_SESSIONCONTENT.fields_by_name['port_groups'].message_type = _PORTGROUPCONTENT
_FILECONTENTMATTER.fields_by_name['streams'].message_type = protocol_pb2._STREAMCONFIGLIST
_FILECONTENTMATTER.fields_by_name['session'].message_type = _SESSIONCONTENT
_FILE.fields_by_name['meta_data'].message_type = _FILEMETADATA
_FILE.fields_by_name['content_matter'].message_type = _FILECONTENT
_FILEMETA.fields_by_name['data'].message_type = _FILEMETADATA
_FILECONTENT.fields_by_name['matter'].message_type = _FILECONTENTMATTER
DESCRIPTOR.message_types_by_name['FileMetaData'] = _FILEMETADATA
DESCRIPTOR.message_types_by_name['PortContent'] = _PORTCONTENT
DESCRIPTOR.message_types_by_name['PortGroupContent'] = _PORTGROUPCONTENT
DESCRIPTOR.message_types_by_name['SessionContent'] = _SESSIONCONTENT
DESCRIPTOR.message_types_by_name['FileContentMatter'] = _FILECONTENTMATTER
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['FileMagic'] = _FILEMAGIC
DESCRIPTOR.message_types_by_name['FileMeta'] = _FILEMETA
DESCRIPTOR.message_types_by_name['FileContent'] = _FILECONTENT
DESCRIPTOR.message_types_by_name['FileChecksum'] = _FILECHECKSUM
DESCRIPTOR.enum_types_by_name['FileType'] = _FILETYPE

FileMetaData = _reflection.GeneratedProtocolMessageType('FileMetaData', (_message.Message,), dict(
  DESCRIPTOR = _FILEMETADATA,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.FileMetaData)
  ))
_sym_db.RegisterMessage(FileMetaData)

PortContent = _reflection.GeneratedProtocolMessageType('PortContent', (_message.Message,), dict(
  DESCRIPTOR = _PORTCONTENT,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.PortContent)
  ))
_sym_db.RegisterMessage(PortContent)

PortGroupContent = _reflection.GeneratedProtocolMessageType('PortGroupContent', (_message.Message,), dict(
  DESCRIPTOR = _PORTGROUPCONTENT,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.PortGroupContent)
  ))
_sym_db.RegisterMessage(PortGroupContent)

SessionContent = _reflection.GeneratedProtocolMessageType('SessionContent', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONCONTENT,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.SessionContent)
  ))
_sym_db.RegisterMessage(SessionContent)

FileContentMatter = _reflection.GeneratedProtocolMessageType('FileContentMatter', (_message.Message,), dict(
  DESCRIPTOR = _FILECONTENTMATTER,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.FileContentMatter)
  ))
_sym_db.RegisterMessage(FileContentMatter)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.File)
  ))
_sym_db.RegisterMessage(File)

FileMagic = _reflection.GeneratedProtocolMessageType('FileMagic', (_message.Message,), dict(
  DESCRIPTOR = _FILEMAGIC,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.FileMagic)
  ))
_sym_db.RegisterMessage(FileMagic)

FileMeta = _reflection.GeneratedProtocolMessageType('FileMeta', (_message.Message,), dict(
  DESCRIPTOR = _FILEMETA,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.FileMeta)
  ))
_sym_db.RegisterMessage(FileMeta)

FileContent = _reflection.GeneratedProtocolMessageType('FileContent', (_message.Message,), dict(
  DESCRIPTOR = _FILECONTENT,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.FileContent)
  ))
_sym_db.RegisterMessage(FileContent)

FileChecksum = _reflection.GeneratedProtocolMessageType('FileChecksum', (_message.Message,), dict(
  DESCRIPTOR = _FILECHECKSUM,
  __module__ = 'fileformat_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.FileChecksum)
  ))
_sym_db.RegisterMessage(FileChecksum)


# @@protoc_insertion_point(module_scope)
