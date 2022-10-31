FROM alpine:3.14
RUN apk add --no-cache py3-pip && \
    pip3 install paho-mqtt pyserial pymodbus
CMD python3 /modbus2mqtt/modbus2mqtt.py --rtu /dev/ttyUSB0 --rtu-baud 9600 --rtu-parity none --set-modbus-timeout 5 --autoremove --mqtt-host 127.0.0.1 --mqtt-user modbus --mqtt-pass m0dbus --mqtt-topic modbus/ --add-to-homeassistant --diagnostics-rate 600 --config /modbus2mqtt/apb.csv --verbosity 2
