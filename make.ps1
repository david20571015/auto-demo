python -OO -m PyInstaller --onefile .\build_test.py
.\dist\build_test.exe
python -OO -m PyInstaller --onefile --add-data "test.json;." .\grade.py

rmdir -Recurse -Force ".\build" 
rm ".\build_test.spec" 
rm ".\grade.spec"