from craftmap import app
import webbrowser
import threading

if __name__ == '__main__':
    threading.Timer(1.25, lambda: webbrowser.open('http://localhost:5000')).start()
    app.run()
