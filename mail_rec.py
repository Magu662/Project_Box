import time
from imapclient import IMAPClient
import os

HOSTNAME = 'imap.gmail.com'
MAILBOX = 'Inbox'
MAIL_CHECK_FREQ = 15        # check mail every 60 seconds

# The following three variables must be customized for this
# script to work
USERNAME = 'maxs.raspi@gmail.com'
PASSWORD = 'MaxsPi2020'



def mail_check():
    # login to mailserver
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)
