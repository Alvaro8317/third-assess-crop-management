# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: crop_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'crop_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x63rop_service.proto\x12\x0b\x63ropservice\"~\n\x04\x43rop\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07variety\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\t\x12\x15\n\rplanting_date\x18\x06 \x01(\t\x12\x14\n\x0charvest_date\x18\x07 \x01(\t\"4\n\x11\x43reateCropRequest\x12\x1f\n\x04\x63rop\x18\x01 \x01(\x0b\x32\x11.cropservice.Crop\"\x1c\n\x0eGetCropRequest\x12\n\n\x02id\x18\x01 \x01(\t\"4\n\x11UpdateCropRequest\x12\x1f\n\x04\x63rop\x18\x01 \x01(\x0b\x32\x11.cropservice.Crop\"\x1f\n\x11\x44\x65leteCropRequest\x12\n\n\x02id\x18\x01 \x01(\t\"/\n\x0c\x43ropResponse\x12\x1f\n\x04\x63rop\x18\x01 \x01(\x0b\x32\x11.cropservice.Crop\"\x07\n\x05\x45mpty2\xa4\x02\n\x0b\x43ropService\x12G\n\nCreateCrop\x12\x1e.cropservice.CreateCropRequest\x1a\x19.cropservice.CropResponse\x12\x41\n\x07GetCrop\x12\x1b.cropservice.GetCropRequest\x1a\x19.cropservice.CropResponse\x12G\n\nUpdateCrop\x12\x1e.cropservice.UpdateCropRequest\x1a\x19.cropservice.CropResponse\x12@\n\nDeleteCrop\x12\x1e.cropservice.DeleteCropRequest\x1a\x12.cropservice.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crop_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CROP']._serialized_start=35
  _globals['_CROP']._serialized_end=161
  _globals['_CREATECROPREQUEST']._serialized_start=163
  _globals['_CREATECROPREQUEST']._serialized_end=215
  _globals['_GETCROPREQUEST']._serialized_start=217
  _globals['_GETCROPREQUEST']._serialized_end=245
  _globals['_UPDATECROPREQUEST']._serialized_start=247
  _globals['_UPDATECROPREQUEST']._serialized_end=299
  _globals['_DELETECROPREQUEST']._serialized_start=301
  _globals['_DELETECROPREQUEST']._serialized_end=332
  _globals['_CROPRESPONSE']._serialized_start=334
  _globals['_CROPRESPONSE']._serialized_end=381
  _globals['_EMPTY']._serialized_start=383
  _globals['_EMPTY']._serialized_end=390
  _globals['_CROPSERVICE']._serialized_start=393
  _globals['_CROPSERVICE']._serialized_end=685
# @@protoc_insertion_point(module_scope)
