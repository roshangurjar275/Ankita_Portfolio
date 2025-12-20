#!/usr/bin/env python3
"""
Script to extract text and images from PDF portfolio
"""

import os
import sys

def extract_with_pymupdf():
    """Extract using PyMuPDF (fitz) - best for both text and images"""
    try:
        import fitz  # PyMuPDF
        print("Using PyMuPDF for extraction...")
        
        pdf_path = "Portfolio PDF.pdf"
        if not os.path.exists(pdf_path):
            print(f"Error: {pdf_path} not found!")
            return False
        
        # Create output directories
        os.makedirs("extracted_images", exist_ok=True)
        os.makedirs("extracted_text", exist_ok=True)
        
        doc = fitz.open(pdf_path)
        all_text = []
        
        print(f"\nProcessing {len(doc)} pages...")
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            print(f"Processing page {page_num + 1}...")
            
            # Extract text
            text = page.get_text()
            if text.strip():
                all_text.append(f"\n{'='*80}\n")
                all_text.append(f"PAGE {page_num + 1}\n")
                all_text.append(f"{'='*80}\n\n")
                all_text.append(text)
                all_text.append("\n")
            
            # Extract images
            image_list = page.get_images()
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # Save image
                img_filename = f"extracted_images/page_{page_num + 1}_img_{img_index + 1}.{image_ext}"
                with open(img_filename, "wb") as img_file:
                    img_file.write(image_bytes)
                print(f"  Extracted image: {img_filename}")
        
        # Save all text
        text_output = "extracted_text/all_text.txt"
        with open(text_output, "w", encoding="utf-8") as f:
            f.write("".join(all_text))
        print(f"\nText saved to: {text_output}")
        
        doc.close()
        print("\n[SUCCESS] Extraction completed successfully!")
        return True
        
    except ImportError:
        print("PyMuPDF not installed. Trying alternative method...")
        return False
    except Exception as e:
        print(f"Error with PyMuPDF: {e}")
        return False

def extract_with_pypdf2():
    """Extract text using PyPDF2 (fallback)"""
    try:
        import PyPDF2
        print("Using PyPDF2 for text extraction...")
        
        pdf_path = "Portfolio PDF.pdf"
        if not os.path.exists(pdf_path):
            print(f"Error: {pdf_path} not found!")
            return False
        
        os.makedirs("extracted_text", exist_ok=True)
        
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            all_text = []
            
            print(f"\nProcessing {len(pdf_reader.pages)} pages...")
            
            for page_num, page in enumerate(pdf_reader.pages):
                print(f"Processing page {page_num + 1}...")
                text = page.extract_text()
                if text.strip():
                    all_text.append(f"\n{'='*80}\n")
                    all_text.append(f"PAGE {page_num + 1}\n")
                    all_text.append(f"{'='*80}\n\n")
                    all_text.append(text)
                    all_text.append("\n")
        
        text_output = "extracted_text/all_text.txt"
        with open(text_output, "w", encoding="utf-8") as f:
            f.write("".join(all_text))
        print(f"\nText saved to: {text_output}")
        print("Note: PyPDF2 cannot extract images. Install PyMuPDF for image extraction.")
        print("\n[SUCCESS] Text extraction completed!")
        return True
        
    except ImportError:
        print("PyPDF2 not installed.")
        return False
    except Exception as e:
        print(f"Error with PyPDF2: {e}")
        return False

def main():
    print("PDF Extraction Tool")
    print("=" * 80)
    
    # Try PyMuPDF first (best option)
    if extract_with_pymupdf():
        return
    
    # Fallback to PyPDF2
    if extract_with_pypdf2():
        print("\n[WARNING] Images not extracted. Install PyMuPDF for image extraction:")
        print("  pip install PyMuPDF")
        return
    
    # If both fail, provide installation instructions
    print("\n[ERROR] No PDF library found!")
    print("\nPlease install one of the following:")
    print("  pip install PyMuPDF  (recommended - extracts text and images)")
    print("  pip install PyPDF2   (text only)")
    print("\nThen run this script again.")

if __name__ == "__main__":
    main()

