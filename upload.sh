PORT="/dev/tty.usbserial-9152409F45"

#HOME="/flash/"
HOME="/"

rshell -p ${PORT} cp main.py ${HOME}main.py
rshell -p ${PORT} cp secrets.py ${HOME}secrets.py
rshell -p ${PORT} cp ../MicroWebSrv/microWebSrv.py ${HOME}microWebSrv.py

rshell -p ${PORT} cp www/index.html ${HOME}/www/index.html
