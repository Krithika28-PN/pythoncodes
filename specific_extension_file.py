files = ["document.txt", "image.jpg", "script.py", "notes.pdf", "data.csv","script2.py"]
extension = ".py"

filtered_files = []
count = 0
for file in files:
    if file.endswith(extension): # file.endswith(extension)
        filtered_files.append(file)
        count += 1

print(filtered_files)  # ✅ Output: ['script.py']
print(len(filtered_files))
print(count)
