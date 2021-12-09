# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from intera_core_msgs/NavigatorStates.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import intera_core_msgs.msg

class NavigatorStates(genpy.Message):
  _md5sum = "2c2eeb02fbbaa6f1ab6c680887f2db78"
  _type = "intera_core_msgs/NavigatorStates"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# used when publishing multiple navigators
string[]         names
NavigatorState[] states

================================================================================
MSG: intera_core_msgs/NavigatorState
# buttons
string[] button_names
bool[] buttons

# wheel position
uint8   wheel

# true if the light is on, false if not
# lights map to button names
string[] light_names
bool[] lights
"""
  __slots__ = ['names','states']
  _slot_types = ['string[]','intera_core_msgs/NavigatorState[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       names,states

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(NavigatorStates, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.names is None:
        self.names = []
      if self.states is None:
        self.states = []
    else:
      self.names = []
      self.states = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.names)
      buff.write(_struct_I.pack(length))
      for val1 in self.names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.states)
      buff.write(_struct_I.pack(length))
      for val1 in self.states:
        length = len(val1.button_names)
        buff.write(_struct_I.pack(length))
        for val2 in val1.button_names:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        length = len(val1.buttons)
        buff.write(_struct_I.pack(length))
        pattern = '<%sB'%length
        buff.write(struct.Struct(pattern).pack(*val1.buttons))
        _x = val1.wheel
        buff.write(_get_struct_B().pack(_x))
        length = len(val1.light_names)
        buff.write(_struct_I.pack(length))
        for val2 in val1.light_names:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        length = len(val1.lights)
        buff.write(_struct_I.pack(length))
        pattern = '<%sB'%length
        buff.write(struct.Struct(pattern).pack(*val1.lights))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.states is None:
        self.states = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.states = []
      for i in range(0, length):
        val1 = intera_core_msgs.msg.NavigatorState()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.button_names = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.button_names.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sB'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.buttons = s.unpack(str[start:end])
        val1.buttons = list(map(bool, val1.buttons))
        start = end
        end += 1
        (val1.wheel,) = _get_struct_B().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.light_names = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.light_names.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sB'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.lights = s.unpack(str[start:end])
        val1.lights = list(map(bool, val1.lights))
        self.states.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.names)
      buff.write(_struct_I.pack(length))
      for val1 in self.names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.states)
      buff.write(_struct_I.pack(length))
      for val1 in self.states:
        length = len(val1.button_names)
        buff.write(_struct_I.pack(length))
        for val2 in val1.button_names:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        length = len(val1.buttons)
        buff.write(_struct_I.pack(length))
        pattern = '<%sB'%length
        buff.write(val1.buttons.tostring())
        _x = val1.wheel
        buff.write(_get_struct_B().pack(_x))
        length = len(val1.light_names)
        buff.write(_struct_I.pack(length))
        for val2 in val1.light_names:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        length = len(val1.lights)
        buff.write(_struct_I.pack(length))
        pattern = '<%sB'%length
        buff.write(val1.lights.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.states is None:
        self.states = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.states = []
      for i in range(0, length):
        val1 = intera_core_msgs.msg.NavigatorState()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.button_names = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.button_names.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sB'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.buttons = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=length)
        val1.buttons = list(map(bool, val1.buttons))
        start = end
        end += 1
        (val1.wheel,) = _get_struct_B().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.light_names = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.light_names.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sB'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.lights = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=length)
        val1.lights = list(map(bool, val1.lights))
        self.states.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
