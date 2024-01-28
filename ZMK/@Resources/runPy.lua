function RunPythonScript()
    os.execute('echo.> "C:\\Users\\Luerl\\Documents\\Rainmeter\\Skins\\ZMK\\@Resources\\flagfile.txt"')
    os.execute('start /B C:\\Users\\Luerl\\AppData\\Local\\Programs\\Python\\Python311\\pythonw.exe "C:\\Users\\Luerl\\Documents\\Rainmeter\\Skins\\ZMK\\@Resources\\main.py"')
end

function DeleteFlagFile()
    os.execute('del "C:\\Users\\Luerl\\Documents\\Rainmeter\\Skins\\ZMK\\@Resources\\flagfile.txt"')
end