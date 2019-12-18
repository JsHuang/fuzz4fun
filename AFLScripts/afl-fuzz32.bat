@echo off
cd /d C:\winafl\bin32\

set fuzz_in=R:\in
set fuzz_out=R:\test-out
set fuzz_prog_path=C:\winafl\bin32\xxx.exe
set fuzz_prog=xxx.exe
set fuzz_method=test
set coverage_module=xxx.dll
set nargs=1

set fuzz_cmd=afl-fuzz.exe -i %fuzz_in% -o %fuzz_out% -D C:\DynamoRIO-Windows\bin32 -t 200000 --  -coverage_module %coverage_module% -target_module %fuzz_prog% -target_method %fuzz_method% -fuzz_iterations 100000 -nargs %nargs% -- %fuzz_prog_path% @@

echo %fuzz_cmd%

%fuzz_cmd%

pause
