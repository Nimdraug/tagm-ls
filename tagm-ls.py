#!/bin/env python2
import tagm, sys, os

# Get the tagm db
tdb = tagm.TagmDB( os.path.join( tagm.find_db(), '.tagm.db' ) )

# Work out what files to ls
if len( sys.argv ) > 1:
    # Files provided in cmd args
    files = sys.argv[1:]
else:
    # List all in dir
    files = os.listdir( u'.' )

for f in files:
    tags = tdb.get_obj_tags( [ f ] )
    print f, tags and ','.join( [ ':'.join( t ) for t in tags ] ) or '-'