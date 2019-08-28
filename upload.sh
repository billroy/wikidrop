PORT="/dev/tty.usbserial-9152409F45"

#HOME="/flash/"
HOME="/"

ampy -p ${PORT} put main.py
ampy -p ${PORT} put secrets.py
ampy -p ${PORT} put ../MicroWebSrv/microWebSrv.py
ampy -p ${PORT} put /www/index.html
