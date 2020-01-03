@echo OFF

powershell Compress-Archive src/* switcheroo.zip
rename switcheroo.zip switcheroo.py
