import streamlit as st
import PIL
import cv2
from PIL import Image 
from pyzbar.pyzbar import decode

# Make one method to decode the barcode
def BarcodeReader(image):
	
	# read the image in numpy array using cv2
	img = cv2.imread(image)
	
	# Decode the barcode image
	detectedBarcodes = decode(img)
	
	# If not detected then print the message
	if not detectedBarcodes:
		st.write("Barcode Not Detected or your barcode is blank/corrupted!")
	else:
	
		# Traverse through all the detected barcodes in image
		for barcode in detectedBarcodes:
		
			# Locate the barcode position in image
			(x, y, w, h) = barcode.rect
			
			# Put the rectangle in image using
			# cv2 to highlight the barcode
			cv2.rectangle(img, (x-10, y-10),
						(x + w+10, y + h+10),
						(255, 0, 0), 2)
			
			if barcode.data!="":
			
			# Print the barcode data
				st.write(barcode.data)
				st.write(barcode.type)
				
def main():
    img=st.camera_input("image")

    im1=Image.open(img)

 
    BarcodeReader(im1)
    
if __name__=='__main__':
    main()
