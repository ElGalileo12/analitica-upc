import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Cambia 'tu_proyecto' al nombre de tu proyecto Django
DJANGO_PROJECT = 'AnaliticaUPC'

def restart_server():
    print("Detected change in files. Restarting server...")
    os.system('python manage.py runserver')

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py") or event.src_path.endswith(".html"):
            restart_server()

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=('.',), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
