import requests
import config
import os


class ReelUpload:
    def __init__(self):
        self.access_token = config.access_token
        self.page_id = config.page_id
        self.video_id = None
        self.upload_url = None

# Step 1: Initialize an Upload Session
    def initialize(self):
        print('Initializing an Upload Session...')

        url = f'https://graph.facebook.com/v21.0/{self.page_id}/video_reels'
        headers = {'Content-Type': 'application/json'}
        data = {
            'upload_phase': 'start',
            'access_token': self.access_token
        }
        response = requests.post(url, headers=headers, json=data)

        if response.ok:
            data = response.json()
            print(data)
            print('Finished Initialize\n')
            # print(data)
            self.video_id = data.get('video_id')
            self.upload_url = data.get('upload_url')
        else:
            print('error')
            print(response.json())

# Step 2: Upload the Video
    def ready_upload(self):
        print("Ready to Upload reels...")
        # folder_path = os.getcwd()

        # for file_name in os.listdir(folder_path):
            # if file_name.endswith((".webm", ".mp4")):
                # self.data = os.path.join(folder_path, file_name)
                # self.file_size = os.path.getsize(self.data)
                # print('self data: ',self.data)
                # description = file_name
                # title = file_name

        # print("Video ID from another function:", self.video_id)
        # file_size = os.path.getsize(video_file_location)
        

        # with open(folder_path, 'rb') as file:
            # data = file.read()

        # file_size = os.path.getsize(data)
        # video = 'a.webm'
        # self.data = f'--data-binary {video}'
        if not self.upload_url:
            print('Error: Upload URL is not set.')
            return

        if not self.video_id:
            print('Error: Video ID is not set.')
            return

        video_file = 'a.webm'
        if not os.path.exists(video_file):
            print(f'Error: File {video_file} does not exist.')
            return

        file_size = os.path.getsize(video_file)
        header = {
            'Authorization': f'OAuth {self.access_token}',
            'offset': '0',
            'file_size': str(file_size),
        }

        with open(video_file, 'rb') as file:
            data = file.read()
        
        response = requests.post(self.upload_url, headers=header, data=data)

        if response.ok:
            data = response.json()
            # print('data json:', data)
            # self.response_ok = data.get('success')
            # print('response ok: ',self.response_ok)
            print('response json', response.json())
            print('Reels is ready to Upload\n')
        else:
            print('Failed to Ready to Upload Reels\n')
            print(response.json())

    def upload_status(self):
        print("check video status...")
        # print('upload url: ', self.upload_url)
        # print('video id: ',self.video_id)
        params = {
            'fields': 'status',
            'access_token': self.access_token
        }
        response = requests.get(self.upload_url, params=params)
        if response.ok:
            # print(response.json())
            print('response status: ', response.json())
            print('response status OK\n')
        else:
            print('response status failed\n')

# Step 3: Publish the Reel
    def publish_reel(self):
        print('Uploading Reel...')
        description = 'awesome'

        url = f'https://graph.facebook.com/v21.0/{self.page_id}/video_reels'
        params = {
            'access_token': self.access_token,
            'video_id': self.video_id,
            'upload_phase': 'finish',
            'video_state': 'PUBLISHED',
            'description': description,
            'title': 'awesome ti'
        }
        response = requests.post(url, params=params)

        if response.ok:
            print('upload reel response json: ', response.json())
            print('Successfully Uploaded reel\n')
        else:
            print('Failed to Upload reel\n')

if __name__ == '__main__':
    reel = ReelUpload()
    reel.initialize()
    reel.ready_upload()
    reel.upload_status()
    reel.publish_reel()
    # reel.upload_status()
