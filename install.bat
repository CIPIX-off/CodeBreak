@echo off
setlocal

ver | find "Windows" > nul
if %errorlevel% == 0 (
    call :windows
) else (
    call :other
)
exit /b

:windows
echo Installing Python dependencies for windows...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo -------------------------------------------------
    echo Failed to install Python dependencies. Pausing...
    pause
)
echo ----------------------------------------------
echo Python dependencies are successfully installed
pause
echo CodeBreak startup...
python CodeBreak.py
exit /b

:other
bash -c '
echo "Installing Python dependencies for other operating systems..."
python3 -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "-------------------------------------------------"
    echo "Failed to install Python dependencies. Pausing..."
    read -p "Press [Enter] key to continue..."
fi
echo "----------------------------------------------"
echo "Python dependencies are successfully installed"
read -p "Press [Enter] key to continue..."
echo "CodeBreak startup..."
python3 CodeBreak.py
'
exit /b
