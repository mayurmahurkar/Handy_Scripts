import pickle
from getpass import getpass
import argparse

print("\nPlease enter pickle file name\n")
filename = input("creds_file_name:")

print("\nPlease enter AWS bucket name\n")
bucket_name = input("bucket_name:")

print("\nPlease enter AWS access key id\n")
access = getpass("aws_access_key_id:")

print("\nPlease enter AWS secret access key\n")
secret_access = getpass("aws_secret_access_key:")

creds = {'ID'   : access, 
		'KEY'   : secret_access,
 		'BUCKET': bucket_name}

if filename.endswith(".pkl"):
	pass
else:
	filename = filename + ".pkl"

# filename = 'mayro_creds.pkl'
outfile = open(filename,'wb')
pickle.dump(creds,outfile)
outfile.close()

print(f'\n{filename} SUCCESSFULLY CREATED !!!')