# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/raster_source.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from rastervision.protos import raster_transformer_pb2 as rastervision_dot_protos_dot_raster__transformer__pb2
from rastervision.protos import vector_source_pb2 as rastervision_dot_protos_dot_vector__source__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/raster_source.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n\'rastervision/protos/raster_source.proto\x12\trv.protos\x1a\x1cgoogle/protobuf/struct.proto\x1a,rastervision/protos/raster_transformer.proto\x1a\'rastervision/protos/vector_source.proto\"\xf5\x07\n\x12RasterSourceConfig\x12\x13\n\x0bsource_type\x18\x01 \x02(\t\x12\x38\n\x0ctransformers\x18\x02 \x03(\x0b\x32\".rv.protos.RasterTransformerConfig\x12\x15\n\rchannel_order\x18\x03 \x03(\x05\x12\x43\n\rgeotiff_files\x18\x04 \x01(\x0b\x32*.rv.protos.RasterSourceConfig.GeoTiffFilesH\x00\x12=\n\nimage_file\x18\x05 \x01(\x0b\x32\'.rv.protos.RasterSourceConfig.ImageFileH\x00\x12\x41\n\x0cgeojson_file\x18\x06 \x01(\x0b\x32).rv.protos.RasterSourceConfig.GeoJSONFileH\x00\x12\x30\n\rcustom_config\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12K\n\x11rasterized_source\x18\x08 \x01(\x0b\x32..rv.protos.RasterSourceConfig.RasterizedSourceH\x00\x1aL\n\x0cGeoTiffFiles\x12\x0c\n\x04uris\x18\x01 \x03(\t\x12\x16\n\x0ex_shift_meters\x18\x02 \x01(\x02\x12\x16\n\x0ey_shift_meters\x18\x03 \x01(\x02\x1a\x18\n\tImageFile\x12\x0b\n\x03uri\x18\x01 \x02(\t\x1a\xf1\x01\n\x10RasterizedSource\x12\x34\n\rvector_source\x18\x01 \x02(\x0b\x32\x1d.rv.protos.VectorSourceConfig\x12\\\n\x12rasterizer_options\x18\x02 \x02(\x0b\x32@.rv.protos.RasterSourceConfig.RasterizedSource.RasterizerOptions\x1aI\n\x11RasterizerOptions\x12\x1b\n\x13\x62\x61\x63kground_class_id\x18\x02 \x02(\x05\x12\x17\n\x0bline_buffer\x18\x03 \x01(\x05:\x02\x31\x35\x1a\xbe\x01\n\x0bGeoJSONFile\x12\x0b\n\x03uri\x18\x01 \x02(\t\x12W\n\x12rasterizer_options\x18\x02 \x02(\x0b\x32;.rv.protos.RasterSourceConfig.GeoJSONFile.RasterizerOptions\x1aI\n\x11RasterizerOptions\x12\x1b\n\x13\x62\x61\x63kground_class_id\x18\x02 \x02(\x05\x12\x17\n\x0bline_buffer\x18\x03 \x01(\x05:\x02\x31\x35\x42\x16\n\x14raster_source_config')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,rastervision_dot_protos_dot_raster__transformer__pb2.DESCRIPTOR,rastervision_dot_protos_dot_vector__source__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RASTERSOURCECONFIG_GEOTIFFFILES = _descriptor.Descriptor(
  name='GeoTiffFiles',
  full_name='rv.protos.RasterSourceConfig.GeoTiffFiles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uris', full_name='rv.protos.RasterSourceConfig.GeoTiffFiles.uris', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_shift_meters', full_name='rv.protos.RasterSourceConfig.GeoTiffFiles.x_shift_meters', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_shift_meters', full_name='rv.protos.RasterSourceConfig.GeoTiffFiles.y_shift_meters', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=698,
)

_RASTERSOURCECONFIG_IMAGEFILE = _descriptor.Descriptor(
  name='ImageFile',
  full_name='rv.protos.RasterSourceConfig.ImageFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='rv.protos.RasterSourceConfig.ImageFile.uri', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=724,
)

_RASTERSOURCECONFIG_RASTERIZEDSOURCE_RASTERIZEROPTIONS = _descriptor.Descriptor(
  name='RasterizerOptions',
  full_name='rv.protos.RasterSourceConfig.RasterizedSource.RasterizerOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='background_class_id', full_name='rv.protos.RasterSourceConfig.RasterizedSource.RasterizerOptions.background_class_id', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_buffer', full_name='rv.protos.RasterSourceConfig.RasterizedSource.RasterizerOptions.line_buffer', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=968,
)

_RASTERSOURCECONFIG_RASTERIZEDSOURCE = _descriptor.Descriptor(
  name='RasterizedSource',
  full_name='rv.protos.RasterSourceConfig.RasterizedSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector_source', full_name='rv.protos.RasterSourceConfig.RasterizedSource.vector_source', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rasterizer_options', full_name='rv.protos.RasterSourceConfig.RasterizedSource.rasterizer_options', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RASTERSOURCECONFIG_RASTERIZEDSOURCE_RASTERIZEROPTIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=727,
  serialized_end=968,
)

_RASTERSOURCECONFIG_GEOJSONFILE_RASTERIZEROPTIONS = _descriptor.Descriptor(
  name='RasterizerOptions',
  full_name='rv.protos.RasterSourceConfig.GeoJSONFile.RasterizerOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='background_class_id', full_name='rv.protos.RasterSourceConfig.GeoJSONFile.RasterizerOptions.background_class_id', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_buffer', full_name='rv.protos.RasterSourceConfig.GeoJSONFile.RasterizerOptions.line_buffer', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=968,
)

_RASTERSOURCECONFIG_GEOJSONFILE = _descriptor.Descriptor(
  name='GeoJSONFile',
  full_name='rv.protos.RasterSourceConfig.GeoJSONFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='rv.protos.RasterSourceConfig.GeoJSONFile.uri', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rasterizer_options', full_name='rv.protos.RasterSourceConfig.GeoJSONFile.rasterizer_options', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RASTERSOURCECONFIG_GEOJSONFILE_RASTERIZEROPTIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=971,
  serialized_end=1161,
)

_RASTERSOURCECONFIG = _descriptor.Descriptor(
  name='RasterSourceConfig',
  full_name='rv.protos.RasterSourceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_type', full_name='rv.protos.RasterSourceConfig.source_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transformers', full_name='rv.protos.RasterSourceConfig.transformers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_order', full_name='rv.protos.RasterSourceConfig.channel_order', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='geotiff_files', full_name='rv.protos.RasterSourceConfig.geotiff_files', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_file', full_name='rv.protos.RasterSourceConfig.image_file', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='geojson_file', full_name='rv.protos.RasterSourceConfig.geojson_file', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_config', full_name='rv.protos.RasterSourceConfig.custom_config', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rasterized_source', full_name='rv.protos.RasterSourceConfig.rasterized_source', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RASTERSOURCECONFIG_GEOTIFFFILES, _RASTERSOURCECONFIG_IMAGEFILE, _RASTERSOURCECONFIG_RASTERIZEDSOURCE, _RASTERSOURCECONFIG_GEOJSONFILE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='raster_source_config', full_name='rv.protos.RasterSourceConfig.raster_source_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=172,
  serialized_end=1185,
)

_RASTERSOURCECONFIG_GEOTIFFFILES.containing_type = _RASTERSOURCECONFIG
_RASTERSOURCECONFIG_IMAGEFILE.containing_type = _RASTERSOURCECONFIG
_RASTERSOURCECONFIG_RASTERIZEDSOURCE_RASTERIZEROPTIONS.containing_type = _RASTERSOURCECONFIG_RASTERIZEDSOURCE
_RASTERSOURCECONFIG_RASTERIZEDSOURCE.fields_by_name['vector_source'].message_type = rastervision_dot_protos_dot_vector__source__pb2._VECTORSOURCECONFIG
_RASTERSOURCECONFIG_RASTERIZEDSOURCE.fields_by_name['rasterizer_options'].message_type = _RASTERSOURCECONFIG_RASTERIZEDSOURCE_RASTERIZEROPTIONS
_RASTERSOURCECONFIG_RASTERIZEDSOURCE.containing_type = _RASTERSOURCECONFIG
_RASTERSOURCECONFIG_GEOJSONFILE_RASTERIZEROPTIONS.containing_type = _RASTERSOURCECONFIG_GEOJSONFILE
_RASTERSOURCECONFIG_GEOJSONFILE.fields_by_name['rasterizer_options'].message_type = _RASTERSOURCECONFIG_GEOJSONFILE_RASTERIZEROPTIONS
_RASTERSOURCECONFIG_GEOJSONFILE.containing_type = _RASTERSOURCECONFIG
_RASTERSOURCECONFIG.fields_by_name['transformers'].message_type = rastervision_dot_protos_dot_raster__transformer__pb2._RASTERTRANSFORMERCONFIG
_RASTERSOURCECONFIG.fields_by_name['geotiff_files'].message_type = _RASTERSOURCECONFIG_GEOTIFFFILES
_RASTERSOURCECONFIG.fields_by_name['image_file'].message_type = _RASTERSOURCECONFIG_IMAGEFILE
_RASTERSOURCECONFIG.fields_by_name['geojson_file'].message_type = _RASTERSOURCECONFIG_GEOJSONFILE
_RASTERSOURCECONFIG.fields_by_name['custom_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RASTERSOURCECONFIG.fields_by_name['rasterized_source'].message_type = _RASTERSOURCECONFIG_RASTERIZEDSOURCE
_RASTERSOURCECONFIG.oneofs_by_name['raster_source_config'].fields.append(
  _RASTERSOURCECONFIG.fields_by_name['geotiff_files'])
_RASTERSOURCECONFIG.fields_by_name['geotiff_files'].containing_oneof = _RASTERSOURCECONFIG.oneofs_by_name['raster_source_config']
_RASTERSOURCECONFIG.oneofs_by_name['raster_source_config'].fields.append(
  _RASTERSOURCECONFIG.fields_by_name['image_file'])
_RASTERSOURCECONFIG.fields_by_name['image_file'].containing_oneof = _RASTERSOURCECONFIG.oneofs_by_name['raster_source_config']
_RASTERSOURCECONFIG.oneofs_by_name['raster_source_config'].fields.append(
  _RASTERSOURCECONFIG.fields_by_name['geojson_file'])
_RASTERSOURCECONFIG.fields_by_name['geojson_file'].containing_oneof = _RASTERSOURCECONFIG.oneofs_by_name['raster_source_config']
_RASTERSOURCECONFIG.oneofs_by_name['raster_source_config'].fields.append(
  _RASTERSOURCECONFIG.fields_by_name['custom_config'])
_RASTERSOURCECONFIG.fields_by_name['custom_config'].containing_oneof = _RASTERSOURCECONFIG.oneofs_by_name['raster_source_config']
_RASTERSOURCECONFIG.oneofs_by_name['raster_source_config'].fields.append(
  _RASTERSOURCECONFIG.fields_by_name['rasterized_source'])
_RASTERSOURCECONFIG.fields_by_name['rasterized_source'].containing_oneof = _RASTERSOURCECONFIG.oneofs_by_name['raster_source_config']
DESCRIPTOR.message_types_by_name['RasterSourceConfig'] = _RASTERSOURCECONFIG

RasterSourceConfig = _reflection.GeneratedProtocolMessageType('RasterSourceConfig', (_message.Message,), dict(

  GeoTiffFiles = _reflection.GeneratedProtocolMessageType('GeoTiffFiles', (_message.Message,), dict(
    DESCRIPTOR = _RASTERSOURCECONFIG_GEOTIFFFILES,
    __module__ = 'rastervision.protos.raster_source_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.RasterSourceConfig.GeoTiffFiles)
    ))
  ,

  ImageFile = _reflection.GeneratedProtocolMessageType('ImageFile', (_message.Message,), dict(
    DESCRIPTOR = _RASTERSOURCECONFIG_IMAGEFILE,
    __module__ = 'rastervision.protos.raster_source_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.RasterSourceConfig.ImageFile)
    ))
  ,

  RasterizedSource = _reflection.GeneratedProtocolMessageType('RasterizedSource', (_message.Message,), dict(

    RasterizerOptions = _reflection.GeneratedProtocolMessageType('RasterizerOptions', (_message.Message,), dict(
      DESCRIPTOR = _RASTERSOURCECONFIG_RASTERIZEDSOURCE_RASTERIZEROPTIONS,
      __module__ = 'rastervision.protos.raster_source_pb2'
      # @@protoc_insertion_point(class_scope:rv.protos.RasterSourceConfig.RasterizedSource.RasterizerOptions)
      ))
    ,
    DESCRIPTOR = _RASTERSOURCECONFIG_RASTERIZEDSOURCE,
    __module__ = 'rastervision.protos.raster_source_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.RasterSourceConfig.RasterizedSource)
    ))
  ,

  GeoJSONFile = _reflection.GeneratedProtocolMessageType('GeoJSONFile', (_message.Message,), dict(

    RasterizerOptions = _reflection.GeneratedProtocolMessageType('RasterizerOptions', (_message.Message,), dict(
      DESCRIPTOR = _RASTERSOURCECONFIG_GEOJSONFILE_RASTERIZEROPTIONS,
      __module__ = 'rastervision.protos.raster_source_pb2'
      # @@protoc_insertion_point(class_scope:rv.protos.RasterSourceConfig.GeoJSONFile.RasterizerOptions)
      ))
    ,
    DESCRIPTOR = _RASTERSOURCECONFIG_GEOJSONFILE,
    __module__ = 'rastervision.protos.raster_source_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.RasterSourceConfig.GeoJSONFile)
    ))
  ,
  DESCRIPTOR = _RASTERSOURCECONFIG,
  __module__ = 'rastervision.protos.raster_source_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.RasterSourceConfig)
  ))
_sym_db.RegisterMessage(RasterSourceConfig)
_sym_db.RegisterMessage(RasterSourceConfig.GeoTiffFiles)
_sym_db.RegisterMessage(RasterSourceConfig.ImageFile)
_sym_db.RegisterMessage(RasterSourceConfig.RasterizedSource)
_sym_db.RegisterMessage(RasterSourceConfig.RasterizedSource.RasterizerOptions)
_sym_db.RegisterMessage(RasterSourceConfig.GeoJSONFile)
_sym_db.RegisterMessage(RasterSourceConfig.GeoJSONFile.RasterizerOptions)


# @@protoc_insertion_point(module_scope)
