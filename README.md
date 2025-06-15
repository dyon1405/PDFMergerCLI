# PDFMergerCLI 🐍📄

![PDFMergerCLI](https://img.shields.io/badge/version-1.0.0-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg) ![Python](https://img.shields.io/badge/python-3.6%2B-yellow.svg)

Welcome to the **PDFMergerCLI** repository! This lightweight Python command-line tool allows you to merge multiple PDF files into a single document effortlessly. Built with the powerful `pypdf` library, this script provides a simple interface for users to select their PDF files and create a unified output file with a name of their choice.

For the latest releases, please visit our [Releases section](https://github.com/dyon1405/PDFMergerCLI/releases).

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Example](#example)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

---

## Features

- **Easy to Use**: Simple command-line interface.
- **Multiple PDF Support**: Merge any number of PDF files.
- **Custom Output Name**: Specify the name for the merged PDF.
- **Open Source**: Free to use and modify.
- **Lightweight**: Minimal dependencies, fast performance.

---

## Installation

To install **PDFMergerCLI**, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dyon1405/PDFMergerCLI.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd PDFMergerCLI
   ```

3. **Install the required packages**:
   Ensure you have Python 3.6 or higher installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the latest release**: 
   For the latest version, check the [Releases section](https://github.com/dyon1405/PDFMergerCLI/releases) and download the appropriate file. 

---

## Usage

To use **PDFMergerCLI**, open your terminal and run the following command:

```bash
python pdf_merger.py
```

The script will prompt you to select the PDF files you wish to merge. Follow the on-screen instructions to complete the process.

### Command-Line Options

- `-h`, `--help`: Show help message and exit.
- `-o OUTPUT`, `--output OUTPUT`: Specify the output file name (default is `merged.pdf`).

---

## Configuration

You can customize the behavior of **PDFMergerCLI** by modifying the configuration file. This file allows you to set default values for the output name and other preferences.

1. **Locate the configuration file**:
   The configuration file is named `config.json` and is located in the root directory of the project.

2. **Edit the configuration**:
   Open the file in your preferred text editor and modify the settings as needed.

### Example Configuration

```json
{
  "output_name": "merged_document.pdf"
}
```

---

## Example

Here’s a quick example of how to merge PDF files using **PDFMergerCLI**:

1. Run the script:
   ```bash
   python pdf_merger.py
   ```

2. When prompted, select the PDF files you want to merge. For example:
   ```
   Select PDF files to merge (comma-separated):
   file1.pdf, file2.pdf, file3.pdf
   ```

3. Specify the output name when prompted:
   ```
   Enter output file name (default: merged.pdf):
   my_merged_file.pdf
   ```

4. The script will process the files and create the merged PDF.

---

## Contributing

We welcome contributions! If you want to help improve **PDFMergerCLI**, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your message"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **pypdf**: The library that powers the PDF merging functionality.
- **Open Source Community**: For their continuous support and contributions.

---

For any issues or feature requests, please open an issue in the GitHub repository. We appreciate your interest in **PDFMergerCLI**! Don't forget to check the [Releases section](https://github.com/dyon1405/PDFMergerCLI/releases) for updates and new features.