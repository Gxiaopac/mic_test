@echo off
chcp 65001 >nul
echo ========================================
echo 安装 Python 依赖包
echo ========================================
echo.

pip install -r requirements.txt

echo.
echo 安装完成！
pause

