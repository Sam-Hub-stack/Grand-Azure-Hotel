@echo off
echo 🏨 Grand Azure Hotel - Backend Setup
echo.

:: Check if we're in the right location
if exist "hotel-backend" (
    echo ✅ Found hotel-backend folder
    cd hotel-backend
) else (
    echo 📁 Creating hotel-backend folder...
    mkdir hotel-backend
    cd hotel-backend
)

:: Check Python
echo Checking Python...
python --version
if errorlevel 1 (
    echo ❌ Python not found! Please install Python from:
    echo https://python.org
    pause
    exit /b 1
)

:: Create app.py if it doesn't exist
if not exist "app.py" (
    echo 📄 Creating app.py...
    type nul > app.py
    echo Please copy the Python code into app.py
    pause
    exit /b 1
)

:: Install dependencies
echo 📦 Installing Flask dependencies...
pip install flask flask-cors

echo.
echo ✅ Setup complete! Starting server...
echo 🌐 Backend will run at: http://localhost:5000
echo 📱 Health check: http://localhost:5000/api/health
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
pause