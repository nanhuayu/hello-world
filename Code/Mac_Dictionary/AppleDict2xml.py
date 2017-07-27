from struct import unpack
from zlib import decompress
import re

title = 'Dictionnaire_Français.dictionary'
filename = title + '/Contents/Resources/Body.data'
f = open(filename, 'rb')

def gen_chunk():
    f.seek(0x40)
    limit = 0x40 + unpack('i', f.read(4))[0]
    f.seek(0x60)
    while f.tell()<limit:
        sz, = unpack('i', f.read(4))
        buf = decompress(f.read(sz)[8:])
        yield re.sub(b'(?m)^....<', b'<', buf)

def gen_entry():
    f.seek(0x40)
    limit = 0x40 + unpack('i', f.read(4))[0]
    f.seek(0x60)
    while f.tell()<limit:
        sz, = unpack('i', f.read(4))
        buf = decompress(f.read(sz)[8:])
        for m in re.finditer(b'<d:entry[^\n]+', buf):
            entry = m.group().decode()
            title = re.search('d:title="(.*?)"', entry).group(1)
            yield title, entry


with open(title + '.xml', 'wb') as fo:
  for s in gen_chunk():
    fo.write(s)

"""
for word, definition in gen_entry():
  # extract info from definition
"""
