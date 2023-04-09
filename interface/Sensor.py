import uuid

class Sensor:

    def __init__(

        self,

        channel,

        base_name,

        suffix,

        io_type,

        unit,

        value,

        begin,

        mac_addr,

        fromStart=False,

    ):

        self._channel = channel

        self._base_name = base_name

        self._suffix = suffix

        self._type = io_type

        self._unit = unit

        self._value = value

        self._begin = begin

        self._sensor_id = None

        self._fromStart = fromStart

        self.hub_mac_address = mac_addr

        self.set_sensor_id(mac_addr)

    def get_channel(self):

        return self._channel

    def set_channel(self, channel):

        self._channel = channel

    def get_sensor_id(self):

        return self._sensor_id

    def set_sensor_id(self, hub_mac_address):

        self._sensor_id = f"{hub_mac_address}_{self._type}_{self.get_name()}"

    def get_source_name(self):

        return self._base_name + (f"{self._suffix}" if self._suffix is not None else "")

    def get_name(self):

        return self.get_source_name() + ("_last" if self._suffix == ".wh" and not self._fromStart else "")

    def get_base_name(self):

        return self._base_name

    def set_base_name(self, base_name):

        self._base_name = base_name

    def get_suffix(self):

        return self._suffix

    def set_suffix(self, suffix):

        self._suffix = suffix

    def get_type(self):

        return self._type

    def set_type(self, io_type):

        self._type = io_type

    def get_unit(self):

        return self._unit

    def set_unit(self, unit):

        self._unit = unit

    def get_value(self):

        return self._value

    def set_value(self, value):

        self._value = value

    def get_begin(self):

        return self._begin

    def set_begin(self, begin):

        self._begin = begin

    def get_from_start(self):

        return self._fromStart

    def set_from_start(self, from_start):

        self._fromStart = from_start

    def generate_uuid(self):

        return str(uuid.uuid4())

    def set_sensor_id(self, hub_mac_address):

        self._sensor_id = f"{hub_mac_address}_{self._type}_{self.get_name()}_{self.generate_uuid()}"

