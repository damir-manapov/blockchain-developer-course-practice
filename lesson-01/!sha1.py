from hashlib import sha1
import sys

d1 = open( sys.argv[ 1 ], "rb" ).read()
d2 = open( sys.argv[ 2 ], "rb" ).read()

h1 = sha1( d1 ).digest()
h2 = sha1( d2 ).digest()

print( h1 == h2 )



