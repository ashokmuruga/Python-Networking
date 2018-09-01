
from ftplib import FTP

host = 'ftp.cse.buffalo.edu'
ftp = FTP(host)
ftp.login()

ftp.cwd('mirror')
print(ftp.pwd())
