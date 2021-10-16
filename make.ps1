python -OO -m PyInstaller --onefile --add-data "test.json;." .\grade.py

rmdir -Recurse -Force ".\build" 
rm ".\grade.spec"