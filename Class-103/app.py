import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/sadhakshinde/WhiteHatJR/Python/Class-103"
to_dir = "/Users/sadhakshinde/WhiteHatJR/Python/Class-103"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("File has been created",event.src_path)
    def on_modified(self, event):
        print("The file has been modified",event.src_path)
    def on_moved(self,event):
        print("File has been moved from",event.src_path)
    def on_deleted(self, event):
        print("File has been deleted",event.src_path)        
    
event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler,from_dir,recursive=True)

observer.start()

try:
    while True:
        time.sleep(1)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()