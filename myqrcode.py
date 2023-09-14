import qrcode as qr

#formatting with features;
features = qr.QRCode(version=1, box_size=40, border=3)

#add video link:
features.add_data('For Home Internet Call 0200000000 ')

#embedd details.
features.make(fit=True)
generate_image = features.make_image(fill_color = 'maroon', Back_color= "white")
#enerate_image = qr.make("Aron QR") #prints this string 
generate_image.save('image1.png')
