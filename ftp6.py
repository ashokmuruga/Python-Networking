from ftplib import FTP

host = 'ftp.cse.buffalo.edu'
ftp = FTP(host)
print(ftp.login())

# Check server status
print(ftp.sendcmd('STAT'))
