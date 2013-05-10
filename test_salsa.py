#!/usr/bin/env python
from salsa import Salsa

def print_state(s):
  assert len(s) == 16
  for i in xrange(4):
    print "{:08x} {:08x} {:08x} {:08x}".format(s[4*i],s[4*i+1],s[4*i+2],s[4*i+3])

if __name__ == '__main__':
  salsa20 = Salsa()

  vectors = [ 
     [ range(1,33), [3,1,4,1,5,9,2,6], [7,0,0,0,0,0,0,0], 
     [ 0xb9a205a3,0x0695e150,0xaa94881a,0xadb7b12c,
       0x798942d4,0x26107016,0x64edb1a4,0x2d27173f,
       0xb1c7f1fa,0x62066edc,0xe035fa23,0xc4496f04,
       0x2131e6b3,0x810bde28,0xf62cb407,0x6bdede3d ] ] ]

  for i in xrange(len(vectors)):
    v = vectors[i]
    s =  salsa20(v[0],v[1],v[2]) 
    #print_state(s)
    assert s == v[3]
  print "All tests passed!"
