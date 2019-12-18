@echo off

set drrun_path=C:\DynamoRIO-Windows\bin64\drrun.exe
set afl_path=C:\winafl\bin64\winafl.dll

set fuzz_prog_path=C:\winafl\bin64\xxx.exe
set fuzz_prog=xxx.exe
set fuzz_method=test
set nargs=1
set test_file=test.jpg

set fuzz_cmd=%drrun_path% -c %afl_path% -debug -target_module %fuzz_prog% -target_method %fuzz_method% -fuzz_iterations 10 -nargs %nargs% -- %fuzz_prog_path% %test_file%

echo %fuzz_cmd%
pause
%fuzz_cmd%

pause
