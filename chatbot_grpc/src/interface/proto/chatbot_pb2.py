# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/chatbot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/chatbot.proto\x12\x07\x63hatbot\"P\n/GetFetusResponseFromChatbotOutboundPortInputDto\x12\r\n\x05input\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\r\"W\n0GetFetusResponseFromChatbotOutboundPortOutputDto\x12\x10\n\x08response\x18\x01 \x01(\t\x12\x11\n\tcreatedAt\x18\x02 \x01(\t2\xa5\x01\n\x0e\x43hatbotService\x12\x92\x01\n\x1bgetFetusResponseFromChatbot\x12\x38.chatbot.GetFetusResponseFromChatbotOutboundPortInputDto\x1a\x39.chatbot.GetFetusResponseFromChatbotOutboundPortOutputDtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.chatbot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GETFETUSRESPONSEFROMCHATBOTOUTBOUNDPORTINPUTDTO']._serialized_start=32
  _globals['_GETFETUSRESPONSEFROMCHATBOTOUTBOUNDPORTINPUTDTO']._serialized_end=112
  _globals['_GETFETUSRESPONSEFROMCHATBOTOUTBOUNDPORTOUTPUTDTO']._serialized_start=114
  _globals['_GETFETUSRESPONSEFROMCHATBOTOUTBOUNDPORTOUTPUTDTO']._serialized_end=201
  _globals['_CHATBOTSERVICE']._serialized_start=204
  _globals['_CHATBOTSERVICE']._serialized_end=369
# @@protoc_insertion_point(module_scope)
