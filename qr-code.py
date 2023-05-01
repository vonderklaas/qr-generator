import qrcode

def generate_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    domain = url.split("/")[2]
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{domain}.png")

url = input("Enter the URL: ")

if (url == ""):
    print("URL cannot be empty")
    exit()
else:
    generate_qrcode(url)
    print("QR Code Generated Successfully")