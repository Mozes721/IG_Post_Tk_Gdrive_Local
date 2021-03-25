from googleapiclient.http import MediaIoBaseDownload
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import io
import time


image_input = []

#Obtaining application credentials 
SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    #use your personal client_secret.json file
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

page_token = None


#loop through the files prompt the user for input when matched assign id and name
def get_file():
    files = img_files()
    choose_img = input('What photo do you choose out of these given: ')
    image_input.append(choose_img)
    for file in files:
        if choose_img == file['name']:
            id = file['id']
            name = file['name']
            #run the download_file function with the id and name of the found file
            download_file(id, name)
         else:
            print("The image you choose by the name of {} doesn't exist".format(choose_img))
            
            

#loop through the image files in Gdrive
def img_files():
    files = DRIVE.files().list(q="mimeType='image/jpeg'",
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)').execute()
    #assign the files in the item variable and then print them all out                                      
    items = files.get('files', [])
    for item in items:
        print(u'{0}'.format(item['name']))
    return items
    

#download the specific file using the fileid 
def download_file(id, filename):
    #assign a varible with the found id name
    request = DRIVE.files().get_media(fileId=id)
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
        time.sleep(2)
        
    

       
   
    



