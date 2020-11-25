#Customer Profile variables
from pathlib import Path
sender = 'clemens12@gmail.com'
contact_base_url = "http://utild.abafm.org/contactforms_app/"
subject = 'Please help us build the Moorhead Brewers Baseball Alumni directory'
message_text=('<html><body><img src="http://www.brewerball.com/templates/rt_antares/custom/images/fastball/MB-Logo-160x-transparent.gif" style="width:166px;height:156px;">' +
                       '<body><font face="tahoma">'+
                       '<p>Hello from Moorhead Brewers Baseball!<br><br>'+
                       'We are excited to be reaching out to create an alumni directory. Your team has had a pretty good run the past few years. We are eager to share news and events with the alumni who enjoyed our program in the past.<br><br>'+
                       'For that reason, we are reaching out to ask that you help us with 2 requests<br>'+
                       '<ol>'+
                       '<li>Enter your contact information into our alumni database'+
                       '<li>Add names and email addresses for other alumni who should also get this email message'+
                       '</ol>'+
                       'Please click here for to complete both steps: <a href="$c_base_url$c_id/">Moorhead Brewers Baseball Alumni List Builder</a><br><br>'+
                       'Please reply to this email with any question.<br><br>'+
                       'Thank you,<br>'+
                       'Chris Clemenson<br>'+
                       'Moorhead Brewers'+
                       '</p>'+
                       '</font></body></html>')

from Google import Create_Service
import base64
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from string import Template
from urllib.error import HTTPError

CLIENT_SECRET_FILE = '/opt/contacts_proj/venv/scripts/CustomerProfiles/client_secret_946174048091-9hcm08cv3soaqnkofdcp4grjpds7d0eh.apps.googleusercontent.com.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#emailMsg = 'You won $100,000'
#mimeMessage = MIMEMultipart()
#mimeMessage['to'] = 'clemens12@gmail.com'
#mimeMessage['subject'] = 'You won'
#mimeMessage.attach(MIMEText(emailMsg, 'plain'))
#raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

#message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
#print(message)
import sqlite3, sys, os, re
from sqlite3 import Error
def create_connection(db_file):
    # create a database connection to the SQLite database
    # specified by the db_file
    # :param db_file database file
    # return: Connection object or None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

#Function to create MIME message, encoding to a base64url string, and assigning it to the raw field of the Message resource:
def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  print(sender + ', ' + to + ', ' + subject + ', ' + message_text)
  message = MIMEText(message_text,'html')
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  #pprint(message)
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


#Function to send message by supplying it in the request body of a call to messages.send, as demonstrated in the following examples.
def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id: %s' % message['id'])
    return message
  except HTTPError as err:
    print('An error occurred: %s' % err)


#Connect to DB, query for recipients and send the email
import uuid
from string import Template

conn = create_connection('/var/opt/contacts_proj/contacts.db')
#conn = create_connection(r'C:\Users\chris.clemenson\OneDrive\Training\py4e\DOProjects\Contact project\db.sqlite3')
cur = conn.cursor()
rows = cur.execute("SELECT * FROM contactforms_app_contacts WHERE web_updated=0")
for row in rows:
    # typical values for text_subtype are plain, html, xml
    recipient = str(row[3])
    contact_id = str(row[0])
    contact_id_4URL = uuid.UUID(contact_id)
    print(recipient)
    html_message = Template(message_text).safe_substitute(c_base_url=contact_base_url, c_id=contact_id_4URL)
    created_message = create_message(sender, recipient, subject, html_message)
    send_message(service, sender, created_message)
