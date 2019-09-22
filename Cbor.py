#Concise Binary Object Representation

import  cbor2
# Serialize an object as a bytestring
def Serialize(obj):

    return (cbor2.dumps(obj))
# Deserialize a bytestring

def deSerialize(obj):
    return cbor2.loads(obj)
#Efficiently deserialize from a file
def deserialize_file(File_name):

    with open( File_name, 'rb') as fp:
     obj =cbor2.load(fp)
# Efficiently serialize an object to a file
def serialize_file(File_name,obj):
    with open(File_name, 'wb') as fp:
     obj =cbor2.dump(obj,fp)


