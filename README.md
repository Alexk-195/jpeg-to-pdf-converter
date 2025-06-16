# 🖼️ JPEG to PDF Converter

A Python application for converting multiple JPEG images into a single PDF document with automatic EXIF orientation correction.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/jpeg-to-pdf-converter)

## ✨ Features

- 🔄 **Batch Conversion**: Convert multiple JPEG files into a single PDF
- 🔧 **EXIF Orientation Support**: Automatically corrects image rotation based on EXIF metadata
- 🖱️ **User-Friendly GUI**: Interactive file selection and save dialogs
- 📊 **Progress Tracking**: Real-time processing feedback with file information
- 🛡️ **Error Handling**: Robust error handling with detailed logging
- 📱 **Cross-Platform**: Works on Windows, macOS, and Linux
- 🎯 **Professional Output**: High-quality PDF generation with proper formatting

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Alexk-195/jpeg-to-pdf-converter.git
   cd jpeg-to-pdf-converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install Pillow
   ```

3. **Run the application**
   ```bash
   python jpeg_to_pdf_converter.py
   ```

## 🎯 Usage

1. **Launch the application**
   ```bash
   python jpeg_to_pdf_converter.py
   ```

2. **Select JPEG files**
   - A file dialog will open
   - Select one or multiple JPEG files (`.jpg`, `.jpeg`)
   - Supports multi-selection with Ctrl+Click (Windows/Linux) or Cmd+Click (macOS)

3. **Choose output location**
   - Select where to save your PDF file
   - The application will automatically add `.pdf` extension if not provided

4. **Automatic conversion**
   - The app processes each image with EXIF orientation correction
   - Creates a multi-page PDF with one image per page
   - Displays progress and completion status

## 📋 Example Output

```
==================================================
🖼️  JPEG to PDF Converter
==================================================
Professional image to PDF conversion tool
Supports EXIF orientation correction

📂 Step 1: Select JPEG files to convert...
✅ Selected 3 file(s):
   1. IMG_001.jpg (2.1 MB)
   2. IMG_002.jpg (1.8 MB)
   3. IMG_003.jpg (2.3 MB)

💾 Step 2: Choose output location for PDF...
✅ PDF will be saved as: my_photos.pdf

🔄 Step 3: Converting images to PDF...

📁 Processing 3 image(s)...

[1/3] Processing: IMG_001.jpg
  → Opened successfully (3024x4032 pixels, RGB mode)
  → Applied 90° rotation (EXIF orientation: 8)
  → Already in RGB mode
  ✅ Successfully processed

[2/3] Processing: IMG_002.jpg
  → Opened successfully (4032x3024 pixels, RGB mode)
  → No rotation needed (EXIF orientation: 1)
  → Already in RGB mode
  ✅ Successfully processed

[3/3] Processing: IMG_003.jpg
  → Opened successfully (3024x4032 pixels, RGB mode)
  → Applied 270° rotation (EXIF orientation: 6)
  → Already in RGB mode
  ✅ Successfully processed

📄 Creating PDF with 3 page(s)...
✅ PDF created successfully!
📍 Output location: /Users/username/Documents/my_photos.pdf
📊 File size: 5.2 MB

🎉 Conversion completed successfully!
```

## 🔧 Technical Details

### EXIF Orientation Support

The application automatically handles EXIF orientation metadata to ensure images appear correctly in the PDF:

| EXIF Value | Description | Applied Rotation |
|------------|-------------|------------------|
| 1 | Normal | None |
| 3 | Upside down | 180° |
| 6 | Rotated 90° CW | 270° |
| 8 | Rotated 90° CCW | 90° |

### Supported Formats

- **Input**: `.jpg`, `.jpeg`, `.JPG`, `.JPEG`
- **Output**: `.pdf`

### Color Mode Handling

- Automatically converts images to RGB mode for PDF compatibility
- Preserves image quality and resolution
- Handles various input color modes (RGBA, Grayscale, etc.)

## 📁 Project Structure

```
jpeg-to-pdf-converter/
├── jpeg_to_pdf_converter.py    # Main application file
├── requirements.txt            # Python dependencies
├── README.md                  # Project documentation
└── LICENSE                  # MIT License
```

## 🛠️ Requirements

### System Requirements
- **Python**: 3.6 or higher

### Python Dependencies
- **Pillow (PIL)**: Image processing and PDF generation
- **tkinter**: GUI dialogs (included with Python)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests if applicable**
5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Development Setup

```bash
# Clone and setup development environment
git clone https://github.com/Alexk-195/jpeg-to-pdf-converter.git
cd jpeg-to-pdf-converter
pip install -r requirements.txt

# Run the application
python jpeg_to_pdf_converter.py
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: "No module named 'PIL'"
```bash
# Solution: Install Pillow
pip install Pillow
```

**Issue**: Images appear rotated in PDF
- This should be automatically handled by EXIF orientation correction
- If issues persist, please report with sample images

**Issue**: File dialog doesn't appear
- Check if tkinter is installed: `python -c "import tkinter"`
- On some Linux distributions: `sudo apt-get install python3-tk`

**Issue**: PDF file is very large
- Large file sizes are normal for high-resolution images
- Consider resizing images before conversion if file size is a concern

### Getting Help

1. Check the [Issues](https://github.com/Alexk-195/jpeg-to-pdf-converter/issues) page
2. Create a new issue with:
   - Your operating system
   - Python version
   - Error message (if any)
   - Steps to reproduce

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Pillow (PIL)](https://pillow.readthedocs.io/) - Python Imaging Library
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI library
- EXIF orientation handling inspired by best practices in image processing


## 🔗 Links

- [Report Bug](https://github.com/Alexk-195/jpeg-to-pdf-converter/issues)
- [Request Feature](https://github.com/Alexk-195/jpeg-to-pdf-converter/issues)
- [Documentation](https://github.com/Alexk-195/jpeg-to-pdf-converter/wiki)

---

**Made with ❤️ by [Alexk-195](https://github.com/Alexk-195) and Claude 4 Sonnet**

*If this project helped you, please consider giving it a ⭐ on GitHub!*
