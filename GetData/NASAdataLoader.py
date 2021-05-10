#NASA File Downloader

from ftplib import FTP
from datetime import datetime


for m in range(3, 31):
    if (m==3)m=1
    n = str(m)
    if m < 10:
        n = '0'+n
        
start = datetime.now()
ftp = FTP('atmos.nmsu.edu','anonymous', 'anonymous')
ftp.cwd("/PDS/data/MROM_2104/DATA/2015/201504/201504"+n+"/")

# Get All Files
files = ftp.nlst()

# Print out the files
for file in files:
    print("Downloading..." + file)
    ftp.retrbinary("RETR " + file ,open("data/" + file, 'wb').write)

ftp.close()

end = datetime.now()
diff = end - start
print('All files downloaded for ' + str(diff.seconds) + 's')
