# HIST3814O Module 2 Exercise 6
## July 21 2017

Followed the instructions for module 2, exercise 6, I downloaded Tesseract, Imagemagick, and PDFtk, then produced an OCR of page 1 of the Equity issue for July 4 1957.

My OCR (output.txt) is incredibly bad - absolutely unreadable! The Provincial Archives produced a much better OCR.

    1  cd ocr-test
    2  pwd
    3  sudo apt-get install tesseract-ocr
    4  sudo apt-get install imagemagick
    5  sudo apt-get install pdftk
    6  wget -w 2 -A .pdf -limit-rate=20k http://collections.banq.qc.ca:8008/jrn03/equity/src/1957/07/04/
    7  wget -w 2 -A .pdf --limit-rate=20k http://collections.banq.qc.ca:8008/jrn03/equity/src/1957/07/04/
    8  wget -w 2 --limit-rate=20k -r --no-parent -A .pdf http://collections.banq.qc.ca:8008/jrn03/equity/src/1957/07/04/
    9  pdftk 83471_1957-07-04.pdf burst
   10  ls
   11  mv collections.banq.qc.ca:8008/jrn03/equity/src/1957/07/04/83471_1957-07-04.pdf ocr-test
   12  ls
   13  mv ocr-test 83471_1957-07-04.pdf
   14  pdftk 83471_1957-07-04.pdf burst
   15  ls
   16  convert -density 300 pg_0001.pdf -depth 8 -strip -background white -alpha off file.tiff
   17  tesseract file.tiff output.txt
   18  history > module2exercise6_commands.md
