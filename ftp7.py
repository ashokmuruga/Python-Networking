
from ftplib import FTP

host = 'ftp.cse.buffalo.edu'
ftp = FTP(host)
ftp.login()

ftp.cwd('CSE421')
print(ftp.retrlines('LIST'))

out = '/README.txt'
with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'README.txt', f.write)
