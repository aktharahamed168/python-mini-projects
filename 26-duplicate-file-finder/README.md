<div align="center">

# Duplicate File Finder

Find duplicate files in a folder by comparing their file content using Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Hashlib](https://img.shields.io/badge/Hashlib-File%20Hashing-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)

</div>

---

## About

Duplicate File Finder is a Python command-line application that scans a folder and identifies files with identical content.

The program uses file hashing to compare files and detect duplicates, even when the files have different names.

---

## Features

- Scan files inside a folder
- Calculate file hashes
- Compare file contents
- Detect duplicate files
- Display duplicate file pairs
- Works with different file types

---

## How It Works

```text
Files
  ↓
Read File Content
  ↓
Calculate Hash
  ↓
Compare Hashes
  ↓
Find Duplicates
  ↓
Display Results
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| os | File and Folder Handling |
| hashlib | File Hashing |

---

## Project Structure

```text
25-duplicate-file-finder/
│
├── main.py
├── requirements.txt
├── README.md
├── screenshot.png
│
└── sample_files/
    ├── file1.txt
    ├── file2.txt
    ├── file3.txt
    └── file4.txt
```

---

## Installation

No external libraries are required.

Run the program directly:

```bash
python main.py
```

---

## Sample Output

```text
===== Duplicate File Finder =====

Duplicates Found
-----------------
file1.txt = file2.txt
file3.txt = file4.txt
```

---

## Example

If two files contain exactly the same content:

```text
file1.txt
file2.txt
```

the program identifies them as duplicates.

Changing even a small part of the content produces a different hash.

---

## Screenshot

<p align="center">
  <!-- <img src="screenshot.png" width="700"> -->
</p>

---

## Future Improvements

- Scan subfolders
- Support large folders
- Show duplicate file sizes
- Calculate total storage that can be recovered
- Add option to delete duplicates
- Add GUI interface
- Export duplicate reports

---

## Author

**Akthar Ahamed**

GitHub: https://github.com/aktharahamed168

LinkedIn: https://www.linkedin.com/in/akthar-ahamed/
