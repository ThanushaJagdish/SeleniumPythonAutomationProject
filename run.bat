@echo off

set datetime=%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%%time:~6,2%

set datetime=%datetime: =0%

pytest testcases --alluredir=reports\%datetime%

allure serve reports\%datetime%