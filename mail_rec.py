import time
from imapclient import IMAPClient
import os

HOSTNAME = 'imap.gmail.com'
MAILBOX = 'Inbox'
MAIL_CHECK_FREQ = 15        # check mail every 60 seconds

# The following three variables must be customized for this
# script to work
USERNAME = 'test@gmail '
PASSWORD = 'password'



def mail_check():
    # login to mailserver
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)
    
    # select our MAILBOX and looked for unread messages
    unseen = server.folder_status(MAILBOX, ['UNSEEN'])

    # number of unread messages
    # print to console to determine NEWMAIL_OFFSET
    newmail_count = (unseen[b'UNSEEN'])
    print('%d unseen messages' % newmail_count)

    if newmail_count > 0:

        print ('recived')
       # os.system("cd /home/pi/del.py")
    time.sleep(MAIL_CHECK_FREQ)

while True:
    mail_check()


