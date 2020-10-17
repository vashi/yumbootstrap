import sys
import bsddb3

#-----------------------------------------------------------------------------

# poor man's BDB database dumper
# this function makes dependencies on host a little lower (BDB in Python
# should be the same as Yum/RPM use)
def db_dump(filename, outfile = sys.stdout):
  try:
    f = bsddb3.hashopen(filename, 'r')
    db_type = "hash"
  except:
    f = bsddb3.btopen(filename, 'r')
    db_type = "btree"

  outfile.write("VERSION=3\n") # magic
  outfile.write("format=bytevalue\n")
  outfile.write("type=%s\n" % (db_type))

  outfile.write("HEADER=END\n")
  for (key,value) in f.items():
    outfile.write(" ")
    for c in key:
      outfile.write("%02x" % ord(c))
    outfile.write("\n")

    outfile.write(" ")
    for c in value:
      outfile.write("%02x" % ord(c))
    outfile.write("\n")
  outfile.write("DATA=END\n")

#-----------------------------------------------------------------------------
# vim:ft=python
