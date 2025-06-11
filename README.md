# 📄 PDFMergerCLI

A simple command-line tool to merge multiple PDF files into a single PDF using Python and the `pypdf` library.

## 🚀 Features

- Merge multiple PDFs into one
- Lightweight and beginner-friendly
- Easily customizable output file name through a config file

## 🛠 Requirements

- Python 3.6 or above
- [`pypdf`](https://pypi.org/project/pypdf/)

Install the required package:

```bash
pip install pypdf
```

## 📁 Project Structure

```
PDFMergerCLI/
├── main.py         # Script to merge the PDF files
├── config.py       # Stores the output file name
└── README.md       # Project documentation
```

## 🔧 How to Use

1. Clone the repository:

```bash
git clone https://github.com/yourusername/PDFMergerCLI.git
cd PDFMergerCLI
```

2. Add the PDF files you want to merge in the same directory.

3. Run the script:

```bash
python main.py
```

4. Follow the on-screen prompts:

```bash
How many files you want to merge? 2
Enter the name of 1th file:- file1.pdf
Enter the name of 2th file:- file2.pdf
```

5. The merged file will be saved with the name defined in `config.py` (default is `Merger.pdf`).

## 🧾 Configuration

Open `config.py` to change the output file name:

```python
PDF_NAME = "MyCustomMergedFile.pdf"
```

## ✅ Example

Merging `resume.pdf`, `portfolio.pdf`, and `certificate.pdf`:

```bash
How many files you want to merge? 3
Enter the name of 1th file:- resume.pdf
Enter the name of 2th file:- portfolio.pdf
Enter the name of 3th file:- certificate.pdf
```

Output: `Merger.pdf` containing all three.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Contributing

Contributions, suggestions, and improvements are welcome! Feel free to fork the repository and submit a pull request.

---

Happy Merging! ✨
