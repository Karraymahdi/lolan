# cyclic redundancy check (CRC) :error-detecting code  detects  accidental changes to raw data
def CRC_calc(data, size):
    crc = 0
    for x in range(size):
        c = data[x]
        q = (crc ^ c) & 0x0f
        crc = (crc >> 4) ^ (q * 0x1081)
        q = (crc ^ (c >> 4)) & 0xf
        crc = (crc >> 4) ^ (q * 0x1081)
    return ((crc << 8) & 0xFF00) | ((crc >> 8) & 0x00FF);






