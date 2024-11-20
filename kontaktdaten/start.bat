@echo off

rem starte den Vorgang
python server.py

rem Warte 3 Sekunden, um sicherzustellen, dass der Server gestartet ist
timeout /t 3

rem Öffne den Browser mit der lokalen IP-Adresse (ersetze hier die IP mit deiner tatsächlichen IP)
start http://192.168.1.10:8000