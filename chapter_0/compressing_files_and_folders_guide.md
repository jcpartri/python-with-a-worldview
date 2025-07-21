
# Compressing Files and Folders from the Command Line

This guide explains how to zip and unzip files and folders using command-line tools on Windows, macOS, and Linux (Debian) systems.

## Windows
On Windows, you can use the built-in `tar` command (available in Windows 10 and later) or PowerShell to compress and decompress files.

### Zipping Files
To create a zip file:
```powershell
tar -a -cf archive.zip file1.txt file2.txt folder/
```
- `-a`: Automatically determines the compression type (zip in this case).
- `-cf`: Creates a new archive file named `archive.zip`.
- Replace `file1.txt`, `file2.txt`, and `folder/` with your files or folders.

### Unzipping Files
To extract a zip file:
```powershell
tar -xf archive.zip
```
- `-xf`: Extracts the contents of `archive.zip` to the current directory.
- Use `-C path/` to extract to a specific directory, e.g., `tar -xf archive.zip -C extracted_files/`.

## macOS
On macOS, the `zip` and `unzip` commands are built-in and can be used from the Terminal.

### Zipping Files
To create a zip file:
```bash
zip -r archive.zip file1.txt file2.txt folder/
```
- `-r`: Recursively includes all files in directories like `folder/`.
- Replace `file1.txt`, `file2.txt`, and `folder/` with your files or folders.

### Unzipping Files
To extract a zip file:
```bash
unzip archive.zip
```
- Extracts contents to the current directory.
- Use `-d path/` to extract to a specific directory, e.g., `unzip archive.zip -d extracted_files/`.

## Linux (Debian)
On Debian-based Linux systems, use the `zip` and `unzip` commands. If not installed, install them with:
```bash
sudo apt update && sudo apt install zip unzip
```

### Zipping Files
To create a zip file:
```bash
zip -r archive.zip file1.txt file2.txt folder/
```
- `-r`: Recursively includes all files in directories like `folder/`.
- Replace `file1.txt`, `file2.txt`, and `folder/` with your files or folders.

### Unzipping Files
To extract a zip file:
```bash
unzip archive.zip
```
- Extracts contents to the current directory.
- Use `-d path/` to extract to a specific directory, e.g., `unzip archive.zip -d extracted_files/`.

## Notes
- Ensure you have sufficient permissions to access files and directories.
- For large files, consider using compression tools like `gzip` or `bzip2` with `tar` on Linux/macOS for better efficiency.
- Always verify the zip file’s integrity after creation using tools like `unzip -t archive.zip` on macOS/Linux or `tar -tvf archive.zip` on Windows.
