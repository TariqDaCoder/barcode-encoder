# Libre Barcode 128 Encoder GUI

!Python
!License

A free and open-source tool to encode text into Code 128 format for Libre Barcode font.

Developed by **Tariq Hassan**.

---

## Features
✔ Encode text into Code 128 for Libre Barcode  
✔ Copy encoded text to clipboard  
✔ Maintain history of encoded items  
✔ Clear history easily  

---

## Screenshot
!App Screenshot

---

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/TariqDaCoder/barcode-encoder.git
   cd barcode-encoder
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the GUI:
      ```bash
   python src/gui.py
## Build Executable
To create a standalone .exe:
   ```bash
   pyinstaller --onefile --windowed src/gui.py
