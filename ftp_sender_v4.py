import ftplib
import random
import argparse
import sys

parser = argparse.ArgumentParser(description='FTP sender parser')
parser.add_argument('-c', '--count', help='Please specify count of files that will be creating.', required=True)
arg = parser.parse_args(sys.argv[1:])
number_count = int(arg.count)

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

number_list = []

for i in xrange(number_count):
    digits = random.sample(range(10), 4)
    final_digits = (''.join(map(str, digits)))
    number = "38063210"
    final_number = number + final_digits
    number_list.append(final_number)


def create_message(*args):
    int_id = "0{0}".format(count)
    oa = "Test"
    da = "{0}".format(number)
    message = "Test message {0} via FTP. Please ignore it!".format(count)
    data = "{0};{1};{2};{3}".format(int_id, oa, da, message)
    return data


count = 1
counter = number_count
new_file_list = []
text_list = []

while count < counter:
    for number in number_list:
        final_number = number
        text = create_message(count, final_number)
        text_list.append(text)
        all_text = '\n'.join(t for t in text_list)
        final_text = all_text + '\n'
        new_file = "ftp_test_v4_{0}.txt".format(str(count))
        outFile = open(new_file, 'w')
        outFile.write(final_text)
        outFile.close()
        new_file_list.append(new_file)
        count += 1

# Upload files to a current directory
for new_file in new_file_list:
    fh = open(new_file, 'rb')
    ftp_connection.storbinary('STOR {0}'.format(new_file), fh)
    print "File: {0} has successfully uploaded!".format(new_file)
    # Close files and FTP connection
    fh.close()

ftp_connection.quit()
