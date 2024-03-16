import os
import shutil
import time  # Import the time module for delays
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the folders to sort into
folders = {
    'word': 'word',
    'pdf': 'pdfs',
    'image': 'images',
    'excel': 'excel',
    'codefile': 'codefiles',
    'ppt':'ppts',
    'note':'notes',
    'exe':'exes',
    'video':'videos',
    'zip':'zip',
    'others':'others'
}

# Function to determine the type of a file
def get_file_type(file_path):
    _, ext = os.path.splitext(file_path)
    if ext.lower() in ['.doc', '.docx', '.odt', '.rtf']:
        return 'word'
    elif ext.lower() in ['.pdf']:
        return 'pdf'
    elif ext.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
        return 'image'
    elif ext.lower() in ['.ipynb', '.py', '.c', '.js', '.v','.java']:
        return 'codefile'
    elif ext.lower() in ['.txt', '.md']:
        return 'note'
    elif ext.lower() in ['.pptx','.pps','.ppsx']:
        return 'ppt'
    elif ext.lower() in ['.zip','.rar']:
        return 'zip'
    elif ext.lower() in ['.xlsx']:
        return 'excel'
    elif ext.lower() in ['.exe','.appinstaller','.msi']:
        return 'exe'
    elif ext.lower() in ['.mp4']:
        return 'video'
    else:
        return 'others'

# Event handler for file system events
class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_type = get_file_type(event.src_path)
        if file_type:
            time.sleep(2)  # Add a 1-second delay
            destination_folder = os.path.join(os.path.expanduser('~'), 'Downloads', folders[file_type])
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            new_path = os.path.join(destination_folder, os.path.basename(event.src_path))
            try:
                # Attempt to move the file
                os.rename(event.src_path, new_path)
                print(f'Moved {event.src_path} to {new_path}')
            except Exception as e:
                print(f'Failed to move {event.src_path} to {new_path}: {e}')

# Set up the observer
if __name__ == "__main__":
    print("Running!")
    path = os.path.expanduser('~') + '/Downloads'
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting")
        observer.stop()
    observer.join()
