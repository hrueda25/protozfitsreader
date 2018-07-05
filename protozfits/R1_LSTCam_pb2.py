# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: R1_LSTCam.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CoreMessages_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='R1_LSTCam.proto',
  package='DataModel',
  serialized_pb=_b('\n\x0fR1_LSTCam.proto\x12\tDataModel\x1a\x12\x43oreMessages.proto\"\xb2\x01\n\x0cLstCamConfig\x12\x14\n\x0cidaq_version\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x64hs_version\x18\x02 \x01(\t\x12\x13\n\x0bnum_modules\x18\x03 \x01(\x07\x12\x30\n\x13\x65xpected_modules_id\x18\x04 \x01(\x0b\x32\x13.DataModel.AnyArray\x12\x12\n\nalgorithms\x18\x05 \x01(\x07\x12\x1b\n\x13pre_proc_algorithms\x18\x06 \x01(\x07\"\xa2\x03\n\x0bLstCamEvent\x12*\n\rmodule_status\x18\x01 \x01(\x0b\x32\x13.DataModel.AnyArray\x12\x1b\n\x13\x65xtdevices_presence\x18\x02 \x01(\x07\x12%\n\x08tib_data\x18\x03 \x01(\x0b\x32\x13.DataModel.AnyArray\x12&\n\tcdts_data\x18\x04 \x01(\x0b\x32\x13.DataModel.AnyArray\x12&\n\tswat_data\x18\x05 \x01(\x0b\x32\x13.DataModel.AnyArray\x12%\n\x08\x63ounters\x18\x06 \x01(\x0b\x32\x13.DataModel.AnyArray\x12(\n\x0b\x63hips_flags\x18\x07 \x01(\x0b\x32\x13.DataModel.AnyArray\x12/\n\x12\x66irst_capacitor_id\x18\x08 \x01(\x0b\x32\x13.DataModel.AnyArray\x12+\n\x0e\x64rs_tag_status\x18\t \x01(\x0b\x32\x13.DataModel.AnyArray\x12$\n\x07\x64rs_tag\x18\n \x01(\x0b\x32\x13.DataModel.AnyArray')
  ,
  dependencies=[CoreMessages_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LSTCAMCONFIG = _descriptor.Descriptor(
  name='LstCamConfig',
  full_name='DataModel.LstCamConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idaq_version', full_name='DataModel.LstCamConfig.idaq_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cdhs_version', full_name='DataModel.LstCamConfig.cdhs_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_modules', full_name='DataModel.LstCamConfig.num_modules', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expected_modules_id', full_name='DataModel.LstCamConfig.expected_modules_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithms', full_name='DataModel.LstCamConfig.algorithms', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_proc_algorithms', full_name='DataModel.LstCamConfig.pre_proc_algorithms', index=5,
      number=6, type=7, cpp_type=3, label=1,
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
  serialized_start=51,
  serialized_end=229,
)


_LSTCAMEVENT = _descriptor.Descriptor(
  name='LstCamEvent',
  full_name='DataModel.LstCamEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_status', full_name='DataModel.LstCamEvent.module_status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extdevices_presence', full_name='DataModel.LstCamEvent.extdevices_presence', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tib_data', full_name='DataModel.LstCamEvent.tib_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cdts_data', full_name='DataModel.LstCamEvent.cdts_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='swat_data', full_name='DataModel.LstCamEvent.swat_data', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counters', full_name='DataModel.LstCamEvent.counters', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chips_flags', full_name='DataModel.LstCamEvent.chips_flags', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_capacitor_id', full_name='DataModel.LstCamEvent.first_capacitor_id', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drs_tag_status', full_name='DataModel.LstCamEvent.drs_tag_status', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drs_tag', full_name='DataModel.LstCamEvent.drs_tag', index=9,
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
  serialized_start=232,
  serialized_end=650,
)

_LSTCAMCONFIG.fields_by_name['expected_modules_id'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['module_status'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['tib_data'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['cdts_data'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['swat_data'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['counters'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['chips_flags'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['first_capacitor_id'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['drs_tag_status'].message_type = CoreMessages_pb2._ANYARRAY
_LSTCAMEVENT.fields_by_name['drs_tag'].message_type = CoreMessages_pb2._ANYARRAY
DESCRIPTOR.message_types_by_name['LstCamConfig'] = _LSTCAMCONFIG
DESCRIPTOR.message_types_by_name['LstCamEvent'] = _LSTCAMEVENT

LstCamConfig = _reflection.GeneratedProtocolMessageType('LstCamConfig', (_message.Message,), dict(
  DESCRIPTOR = _LSTCAMCONFIG,
  __module__ = 'R1_LSTCam_pb2'
  # @@protoc_insertion_point(class_scope:DataModel.LstCamConfig)
  ))
_sym_db.RegisterMessage(LstCamConfig)

LstCamEvent = _reflection.GeneratedProtocolMessageType('LstCamEvent', (_message.Message,), dict(
  DESCRIPTOR = _LSTCAMEVENT,
  __module__ = 'R1_LSTCam_pb2'
  # @@protoc_insertion_point(class_scope:DataModel.LstCamEvent)
  ))
_sym_db.RegisterMessage(LstCamEvent)


# @@protoc_insertion_point(module_scope)
