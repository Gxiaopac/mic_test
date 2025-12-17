@echo off
chcp 65001 >nul
echo ========================================
echo 麦克风批量测试工具 - Web版本 v2.10
echo ========================================
echo.
echo 正在启动服务器...
echo.

REM 优先使用 Anaconda 的 Python，如果不存在则使用系统的 python
if exist "E:\Anaconda\python.exe" (
    echo 使用 Anaconda Python: E:\Anaconda\python.exe
    E:\Anaconda\python.exe app.py
) else (
    echo 使用系统 Python
    python app.py
)

pause

