@echo off
call ../env.bat
esptool.py --chip esp32 --port %AMPY_PORT%  write_flash -z 0x1000 ./esp32spiram-idf4-20200902-v1.13.bin