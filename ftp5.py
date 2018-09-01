
from ftplib import FTP

# Host to connect to
host = 'ftp.cse.buffalo.edu'

# Make an FTP object and anonymously login
ftp = FTP(host)
print(ftp.login())

# List directories in current path
print(ftp.retrlines('LIST'))

# Change into one of the sub-directories
ftp.cwd('mirror')
print(ftp.retrlines('LIST'))
