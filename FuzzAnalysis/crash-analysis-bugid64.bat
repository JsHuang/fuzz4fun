@echo off

if "%2"=="" (
    echo Usage: %0 program_path crash_dir 
    goto :end
)

set ProgramPath=%1
set CrashFilePath=%2


for %%f in (%CrashFilePath%\*) do (
    echo BugId.cmd --symbols=c:\symbols %ProgramPath% -- %%f
)

:end