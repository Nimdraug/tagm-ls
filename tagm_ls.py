#!/bin/env python2
import tagm, sys, os

def main():
    # Get the tagm db
    dbpath = tagm.find_db()
    tdb = tagm.TagmDB( os.path.join( dbpath, '.tagm.db' ) )

    # Work out what files to ls
    if len( sys.argv ) > 1:
        # Files provided in cmd args
        files = sys.argv[1:]
    else:
        # List all in dir
        files = os.listdir( u'.' )

    for f in files:
        tags = tdb.get_obj_tags( tagm.process_paths( dbpath, [ f ] ) )
        print f, tags and ','.join( [ ':'.join( t ) for t in tags ] ) or '-'

if __name__ == '__main__':
    main()