import zipfile

with zipfile.ZipFile("calculator.zip", "w") as zip:
    zip.write("calculator.py")
    