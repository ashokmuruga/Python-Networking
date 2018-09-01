from ftplib import FTP

# Host to connect to
host = 'ftp.cse.buffalo.edu'

# Make an Python FTP object and anonymously login
ftp = FTP(host)
print(ftp.login())
