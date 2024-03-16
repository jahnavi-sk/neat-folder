import os
import shutil
import glob

# Define the source directory
SOURCE_DIR = os.path.expanduser('~/Downloads/')

# Define the destination directories
DEST_DIR_IMAGES = 'C:/Users/Jahnavi/Downloads/images'
DEST_DIR_WORD = 'C:/Users/Jahnavi/Downloads/word'
DEST_DIR_NOTES = 'C:/Users/Jahnavi/Downloads/notes'
DEST_DIR_PDFS = 'C:/Users/Jahnavi/Downloads/pdfs'
DEST_DIR_EXES = 'C:/Users/Jahnavi/Downloads/exes'
DEST_DIR_VIDEOS = 'C:/Users/Jahnavi/Downloads/videos'
DEST_DIR_CODEFILES = 'C:/Users/Jahnavi/Downloads/codefiles'
DEST_DIR_ZIP = 'C:/Users/Jahnavi/Downloads/zip'
DEST_DIR_PPTS = 'C:/Users/Jahnavi/Downloads/ppts'
DEST_DIR_EXCEL = 'C:/Users/Jahnavi/Downloads/excel'
DEST_DIR_OTHERS = 'C:/Users/Jahnavi/Downloads/others'


destinations = [DEST_DIR_IMAGES,DEST_DIR_WORD,DEST_DIR_NOTES,DEST_DIR_PDFS,DEST_DIR_EXES,DEST_DIR_VIDEOS,DEST_DIR_CODEFILES,DEST_DIR_ZIP,DEST_DIR_PPTS]

# Ensure the destination directories exist, if not, create them
for dest_dir in destinations:
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

# Iterate over files in the source directory
for file_path in glob.glob(os.path.join(SOURCE_DIR, '*.*')):
    # Check if the file is not a directory
    if os.path.isfile(file_path):
        # Determine the destination directory based on the file extension
        if file_path.lower().endswith(('.jpg', '.gif')):
            dest_dir = DEST_DIR_IMAGES
        elif file_path.lower().endswith('.docx'):
            dest_dir = DEST_DIR_WORD
        elif file_path.lower().endswith(('.txt', '.md')):
            dest_dir = DEST_DIR_NOTES
        elif file_path.lower().endswith(('.pdf')):
            dest_dir = DEST_DIR_PDFS
        elif file_path.lower().endswith(('.exe', '.msi','.appinstaller')):
            dest_dir = DEST_DIR_EXES
        elif file_path.lower().endswith(('.mp4')):
            dest_dir = DEST_DIR_VIDEOS
        elif file_path.lower().endswith(('.ipynb', '.py', '.c', '.js', '.v','.java')):
            dest_dir = DEST_DIR_CODEFILES
        elif file_path.lower().endswith(('.zip', '.rar')):
            dest_dir = DEST_DIR_ZIP
        elif file_path.lower().endswith(('.pptx','.pps','.ppsx')):
            dest_dir = DEST_DIR_PPTS
        elif file_path.lower().endswith(('.txt', '.md')):
            dest_dir = DEST_DIR_EXCEL
        else:
            dest_dir = DEST_DIR_OTHERS

        # Move the file to the destination directory
        try:
            shutil.move(file_path, dest_dir)
            print(f'Moved: {os.path.basename(file_path)} to {dest_dir}')
        except Exception as e:
            print(f"Error moving {os.path.basename(file_path)}: {e}")
