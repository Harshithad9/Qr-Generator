import qrcode

# Generate QR code
qr = qrcode.make("Follow @harshitha.gmail!") #add text you want to encode in the QR code

# Show the QR code
qr.show()

# Ask user if they want to save the QR code
choice = input("Do you want to save the QR code? (yes/no): ").strip().lower()

if choice == "yes":
    qr.save("qrcode.png")
    print("QR code saved as 'qrcode.png'.")
else:
    print("QR code was not saved.")
