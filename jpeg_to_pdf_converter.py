#!/usr/bin/env python3
"""
JPEG to PDF Converter
=====================

A Python application for converting multiple JPEG images into a single PDF document.
Handles EXIF orientation metadata to ensure proper image rotation in the output PDF.

Features:
- Interactive file selection dialog for JPEG files
- Automatic EXIF orientation correction
- Multi-page PDF generation
- User-friendly GUI dialogs
- Comprehensive error handling and logging

Author: AlexK195 vibe coded with Claude 4 Sonnet
Version: 1.1
Date: 2025
License: MIT

Dependencies:
- Pillow (PIL): For image processing and PDF generation
- tkinter: For GUI dialogs (included with Python)

Usage:
    python jpeg_to_pdf_converter.py

Requirements:
    pip install Pillow
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
from pathlib import Path


def select_jpeg_files():
    """
    Display a file selection dialog for choosing JPEG files.
    
    Opens a native file dialog allowing multiple file selection with
    appropriate file type filters for JPEG images.
    
    Returns:
        tuple: Tuple of selected file paths, empty if cancelled
    """
    # Create root window and hide it immediately
    root = tk.Tk()
    root.withdraw()  # Hide the main window to show only dialog
    
    # Define file type filters for the dialog
    file_types = [
        ("JPEG files", "*.jpg *.jpeg *.JPG *.JPEG"),
        ("All files", "*.*")
    ]
    
    # Open multiple file selection dialog
    files = filedialog.askopenfilenames(
        title="Select JPEG files to convert",
        filetypes=file_types
    )
    
    # Clean up the root window
    root.destroy()
    return files


def select_output_path():
    """
    Display a save dialog for choosing the output PDF location.
    
    Opens a native save dialog with PDF file type filter and
    automatic extension handling.
    
    Returns:
        str: Selected output file path, empty string if cancelled
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Open save file dialog with PDF filter
    output_file = filedialog.asksaveasfilename(
        title="Save PDF as",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )
    
    root.destroy()
    return output_file


def apply_exif_orientation(image, file_path):
    """
    Apply EXIF orientation correction to an image.
    
    Reads EXIF metadata from JPEG files and applies the appropriate rotation
    to ensure the image displays with correct orientation, matching how it
    appears in standard image viewers.
    
    Args:
        image (PIL.Image): The PIL Image object to process
        file_path (str): Path to the image file (for logging purposes)
    
    Returns:
        PIL.Image: The image with correct orientation applied
    
    Note:
        EXIF Orientation values:
        1 = Normal (no rotation)
        3 = Upside down (180° rotation)
        6 = Rotated 90° CW (needs 270° CCW correction)
        8 = Rotated 90° CCW (needs 90° CCW correction)
    """
    try:
        # Attempt to read EXIF data from the image
        exif = image._getexif()
        
        if exif is not None:
            # EXIF orientation tag number is 274
            orientation = exif.get(274)
            
            if orientation:
                # Apply rotation based on EXIF orientation value
                if orientation == 3:
                    # Image is upside down - rotate 180°
                    image = image.rotate(180, expand=True)
                    print(f"  → Applied 180° rotation (EXIF orientation: {orientation})")
                elif orientation == 6:
                    # Image is rotated 90° clockwise - rotate 270° to correct
                    image = image.rotate(270, expand=True)
                    print(f"  → Applied 270° rotation (EXIF orientation: {orientation})")
                elif orientation == 8:
                    # Image is rotated 90° counter-clockwise - rotate 90° to correct
                    image = image.rotate(90, expand=True)
                    print(f"  → Applied 90° rotation (EXIF orientation: {orientation})")
                elif orientation == 1:
                    # Normal orientation - no rotation needed
                    print(f"  → No rotation needed (EXIF orientation: {orientation})")
                else:
                    # Uncommon orientation values (2, 4, 5, 7) involve flipping
                    print(f"  → Unsupported EXIF orientation: {orientation} (no rotation applied)")
    
    except (AttributeError, KeyError, TypeError) as e:
        # EXIF data not available, corrupted, or unreadable
        print(f"  → No EXIF orientation data available")
    
    return image


def convert_jpegs_to_pdf(jpeg_files, output_path):
    """
    Convert a collection of JPEG files into a single multi-page PDF.
    
    Processes each JPEG file by:
    1. Opening the image
    2. Applying EXIF orientation correction
    3. Converting to RGB color mode (required for PDF)
    4. Adding to the PDF compilation
    
    Args:
        jpeg_files (tuple): Collection of JPEG file paths to convert
        output_path (str): Destination path for the output PDF file
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    # Validate input
    if not jpeg_files:
        print("❌ No files selected for conversion.")
        return False
    
    if not output_path:
        print("❌ No output path specified.")
        return False
    
    try:
        print(f"\n📁 Processing {len(jpeg_files)} image(s)...")
        
        # Collection to store processed images
        processed_images = []
        
        # Process each JPEG file
        for i, file_path in enumerate(jpeg_files, 1):
            print(f"\n[{i}/{len(jpeg_files)}] Processing: {os.path.basename(file_path)}")
            
            # Open the image file
            try:
                img = Image.open(file_path)
                print(f"  → Opened successfully ({img.size[0]}x{img.size[1]} pixels, {img.mode} mode)")
            except Exception as e:
                print(f"  ❌ Failed to open image: {str(e)}")
                continue
            
            # Apply EXIF orientation correction
            img = apply_exif_orientation(img, file_path)
            
            # Convert to RGB color mode if necessary
            # PDF format requires RGB mode for color images
            if img.mode != 'RGB':
                original_mode = img.mode
                img = img.convert('RGB')
                print(f"  → Converted from {original_mode} to RGB mode")
            else:
                print(f"  → Already in RGB mode")
            
            # Add processed image to collection
            processed_images.append(img)
            print(f"  ✅ Successfully processed")
        
        # Check if we have any successfully processed images
        if not processed_images:
            print("\n❌ No images were successfully processed.")
            return False
        
        # Generate the PDF file
        print(f"\n📄 Creating PDF with {len(processed_images)} page(s)...")
        
        # Save as multi-page PDF
        # First image becomes the base, additional images are appended as pages
        processed_images[0].save(
            output_path,
            save_all=True,  # Enable multi-page PDF
            append_images=processed_images[1:] if len(processed_images) > 1 else [],
            format='PDF',
            resolution=100.0  # Set PDF resolution (DPI)
        )
        
        print(f"✅ PDF created successfully!")
        print(f"📍 Output location: {output_path}")
        print(f"📊 File size: {os.path.getsize(output_path) / (1024*1024):.1f} MB")
        
        return True
        
    except Exception as e:
        error_msg = f"Failed to create PDF: {str(e)}"
        print(f"❌ {error_msg}")
        
        # Show error dialog to user
        messagebox.showerror("Conversion Error", error_msg)
        return False


def main():
    """
    Main application entry point.
    
    Orchestrates the complete workflow:
    1. Display application header
    2. Prompt user to select JPEG files
    3. Prompt user to choose output location
    4. Convert images to PDF
    5. Display success/failure message
    """
    # Display application header
    print("=" * 50)
    print("🖼️  JPEG to PDF Converter")
    print("=" * 50)
    print("Image to PDF conversion tool")
    print("Supports EXIF orientation correction")
    print()
    
    # Step 1: Select input JPEG files
    print("📂 Step 1: Select JPEG files to convert...")
    jpeg_files = select_jpeg_files()
    
    # Validate file selection
    if not jpeg_files:
        print("❌ No files selected. Operation cancelled.")
        print("\n👋 Goodbye!")
        return
    
    # Display selected files
    print(f"✅ Selected {len(jpeg_files)} file(s):")
    for i, file_path in enumerate(jpeg_files, 1):
        file_size = os.path.getsize(file_path) / (1024*1024)  # Size in MB
        print(f"  {i:2d}. {os.path.basename(file_path)} ({file_size:.1f} MB)")
    
    # Step 2: Select output location
    print(f"\n💾 Step 2: Choose output location for PDF...")
    output_path = select_output_path()
    
    # Validate output path
    if not output_path:
        print("❌ No output location selected. Operation cancelled.")
        print("\n👋 Goodbye!")
        return
    
    print(f"✅ PDF will be saved as: {os.path.basename(output_path)}")
    
    # Step 3: Convert files to PDF
    print(f"\n🔄 Step 3: Converting images to PDF...")
    conversion_success = convert_jpegs_to_pdf(jpeg_files, output_path)
    
    # Step 4: Display final result
    if conversion_success:
        # Show success dialog
        success_message = (
            f"PDF conversion completed successfully!\n\n"
            f"📄 Pages: {len(jpeg_files)}\n"
            f"📍 Location: {output_path}\n"
            f"📊 Size: {os.path.getsize(output_path) / (1024*1024):.1f} MB"
        )
        
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("✅ Conversion Complete", success_message)
        root.destroy()
        
        print(f"\n🎉 Conversion completed successfully!")
    else:
        print(f"\n❌ Conversion failed. Please check the error messages above.")
    
    print(f"\n👋 Thank you for using JPEG to PDF Converter!")
    print("=" * 50)


if __name__ == "__main__":
    # Entry point - execute main function when script is run directly
    main()