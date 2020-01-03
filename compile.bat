@echo OFF

del switcheroo.py 2>NUL
powershell Compress-Archive src/* switcheroo.zip
rename switcheroo.zip switcheroo.py
