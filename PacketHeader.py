class PacketHeader :
  def __init__(self, PakcetType,Routing,fromID,toID,Payload):
      self.PakcetType=PakcetType
      self.Routing = Routing
      self.fromID = fromID
      self.toID = toID
      self.Payload = Payload
      self.crc=None
      self.Packet=None


