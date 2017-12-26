import ftplib

__author__ = 'itymoshenko'

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
number_list = ['38063210xxxx', '38093xxxxxxx', '38063210xxxx', '38096xxxxxxx']


def create_message(*arg):
    int_id = "0{0}".format(count)
    oa = "Test"
    da = "{0}".format(number)
    message = "Test message {0} via FTP. Please ignore it!".format(count)
    msg = message + "\n"
    data = "{0};{1};{2};{3}".format(int_id, oa, da, msg)
    return data


count = 1
counter = 4
new_file_list = []

while count < counter:
    if counter == len(number_list):
        for number in number_list:
            final_number = number
            with open(ftp_test, 'rU') as f:
                new_file = "ftp_test_v2_{0}.txt".format(str(count))
                outFile = open(new_file, 'w')
                outFile.write(create_message(count, final_number))
                outFile.close()
		new_file_list.append(new_file)
                count += 1
    else:
        print "Error"
        break

# Upload files to a current directory
for new_file in new_file_list:
    fh = open(new_file, 'rb')
    ftp_connection.storbinary('STOR {0}'.format(new_file), fh)
    print "File: {0} has successfully uploaded!".format(new_file)
    # Close files and FTP connection
    fh.close()

ftp_connection.quit()

