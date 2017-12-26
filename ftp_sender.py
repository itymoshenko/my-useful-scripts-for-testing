import ftplib

# Create connection via FTP
server = 'localhost'
username = ''
password = ''
ftp_connection = ftplib.FTP(server, username, password)

# list directory content
# ftp_connection.retrlines('LIST')

# Change directory
remote_path = "in/"
ftp_connection.cwd(remote_path)

ftp_test = "/root/scripts/test_ftp.txt"


def update_file(arg):
    f = open(ftp_test, 'a')
    msg = "{0}".format(arg)
    f.write(msg + '\n')
    f.close()

count = 0

while count < 10:
    count = count + 1
    int_id = "0{0}".format(count)
    oa = "Test"
    da = "380632107529"
    message = "Test message {0} via FTP. Please ignore it!".format(count)
    data = "{0};{1};{2};{3}".format(int_id, oa, da, message)
    update_file(data)

# Upload file to a current directory
fh = open(ftp_test, 'rb')
ftp_connection.storbinary('STOR test_ftp.txt', fh)
print "File has successfully uploaded!"

# Close file and FTP connection
fh.close()
ftp_connection.quit()

"Erase file content before writing to it next time"
f = open(ftp_test, 'w').close()
