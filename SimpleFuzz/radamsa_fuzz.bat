@echo off

set process_name=XXX.exe
:loop
echo "Fuzz XXX"
radamsa.exe  input -o output
%process_name% output
tasklist /fi "imagename eq %process_name%" 2>nul | findstr /i "%process_name%" >nul

if %errorlevel% equ 0 (
  echo Process %process_name% is running.
) else (
  echo Process %process_name% is not running.
  goto end
)
goto loop

:end
echo Loop ended.
