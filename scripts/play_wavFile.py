import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore # QtMultimedia
from PyQt5.QtMultimedia import QSound

# sudo apt-get install python3-pyqt5.qtmultimedia
       
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sound_file_str = "/home/oj/catkin_ws/src/ero/scripts/pacman_death.wav"
    QSound.play(sound_file_str)
    
    # url = QtCore.QUrl.fromLocalFile("pacman_death.wav")
    # content = QtMultimedia.QMediaContent(url)
    # player = QtMultimedia.QMediaPlayer()
    # player.setMedia(content)
    # player.setVolume(50.0)
    # player.play()
    sys.exit(app.exec())

