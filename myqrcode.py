import qrcode as qr

#formatting with features;
features = qr.QRCode(version=1, box_size=40, border=3)

#add video link:
features.add_data('https://liquid.tech/')

#embedd details.
features.make(fit=True)
generate_image = features.make_image(fill_color =" ", Back_color= "white")
#enerate_image = qr.make("Aron QR") #prints this string 
generate_image.save('image7.png')
