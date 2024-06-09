

# Neat Folder


### This is a Python automation script to clear the Downloads folder.

Downloads folder tends to get cluttered as anything we download on the browser goes directly to this folder.
To avoid this, I made an automation script which organizes the Downloads folder.


### Libraries to install

#### `pip install watchdog`


### There are 2 files

#### - ``` sorted. py ```

#### - ``` new_downloads. py ```


### Working


The `sorted.py` will sort the files in the Downloads folder into sub folder like images, word documents, pdfs, powerpoint presentations, etc. If these folders are not already there in the main Downloads folder, it is automatically created and everything is sorted.


The `new_downloads.py` is to be kept running all the time, so whenever the user downloads anything on the browser, it goes to its designated folder.


Recommended order is to execute the `sorted.py` first, and then have `new_downloads.py` running.


### To run it in the background

- In Linux and macOS
	- Use `systemd`, `supervisord`, or `pm2`
- In Windows
	- Use Task Scheduler
