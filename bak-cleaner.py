import time
from time import strptime
from boto.s3.connection import S3Connection

conn = S3Connection(<your-access-id>, <your-secret-key>)

bak_bucket = conn.get_bucket(<destination-bucket>)

keys = bak_bucket.list()
max_keep = 5

date_list = []
for key in keys:
  if(key.key[0:6]=='backup'):
    date_list.append(key.key)


def getListOfKeysToDelete(max_keep, date_list):
  date_list.sort()
  rem_list = []

  if len(date_list) > max_keep:
    rem_list = date_list[0:len(date_list)-max_keep]

  return rem_list

for key in getListOfKeysToDelete(max_keep, date_list):
  bak_bucket.delete_key(key)
