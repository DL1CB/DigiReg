@echo off

call ./env.bat

echo uploading ui
rem ampy rmdir /ui
ampy put ./src/ui /ui

echo uploading bitmaps
REM ampy rmdir /bitmaps
ampy put ./src/bitmaps /bitmaps

echo uploading store
rem ampy rmdir /store
ampy put ./src/store /store

echo uploading drivers
rem ampy rmdir /drivers
ampy put ./src/drivers /drivers

echo uploading networking
ampy rmdir /networking
ampy put ./src/networking /networking

echo uploading main 
ampy put ./src/main.py /main.py

echo starting serial console
call ./console.bat



