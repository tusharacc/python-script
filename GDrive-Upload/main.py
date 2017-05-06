
from __future__ import print_function
import httplib2
import os, time

from PIL import Image
from apiclient import discovery
from apiclient.http import MediaFileUpload
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'photos-gdrive'
MY_PATH = ['/home/tushar/Pictures/Marraige Photos/DCIM/100EOS5D/','/home/tushar/Pictures/Marraige Photos/DCIM/101EOS5D/','/home/tushar/Pictures/Marraige Photos/DCIM/EOSMISC/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 1/Cam 1/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 1/Cam 2/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 2/Cam 1/','/home/tushar/Pictures/Marraige Photos/Priyadharshini Blue Logoon/Day 2/Cam 2/']

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'file_upload.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    folder_id = '0By03Xv6Ghz5-OEtsVDJkOHBfN28'
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())

    service = discovery.build('drive', 'v3', http=http)
    #image = '1E1A9721.JPG'
    #im = Image.open(image)
    #im.save(image.split('.')[0],'PNG',compress_level=0)
    for path in MY_PATH:
    	count = 0
    	images = os.listdir(path)
    	for image in images:
    		if image.split('.')[-1] == 'JPG':
    			count += 1
    			file_metadata = {'name':image,
            		         	 'parents':[folder_id]}
    			media = MediaFileUpload(path + image,mimetype='image/jpeg')
    			file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    			time.sleep(1)
    	print ('The number of files in {0}: {1}'.format(file.get('id'),str(count)))

if __name__ == '__main__':
    main()

# file_metadata = {
#   'name' : 'Invoices',
#   'mimeType' : 'application/vnd.google-apps.folder'
# }
# file = drive_service.files().create(body=file_metadata,
#                                     fields='id').execute()
# print 'Folder ID: %s' % file.get('id')

# folder_id = file.get('id')
# file_metadata = {
#   'name' : 'photo.jpg',
#   'parents': [ folder_id ]
# }
# media = MediaFileUpload('files/photo.jpg',
#                         mimetype='image/jpeg',
#                         resumable=True)
# file = drive_service.files().create(body=file_metadata,
#                                     media_body=media,
#                                     fields='id').execute()
# print 'File ID: %s' % file.get('id')