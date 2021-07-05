echo off
REM First, check if python installed
REM echo %~dp0

python -V
if errorlevel 1 goto errorNoPython

goto:installStuff

:errorNoPython
echo Please install Python (https://www.python.org/) first!
goto:eof

:installStuff
pip install -r ac-data/requirements.txt
python ac-data/setup.py
if errorlevel 15 (echo exiting...) else (echo Please drag "run.bat" to a convenient location!)
goto:eof
