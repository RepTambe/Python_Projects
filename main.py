import qrcode

data = "https://www.youtube.com/watch?v=iYx_aGlmyc4"


img = qrcode.make(data)



qr = qrcode.QRCode(version= 1, box_size= 10, border= 5)

qr.add_data(data)

qr.make(fit= True)

img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/atamb/OneDrive/Documents/PythonProjects/myqrcode.png')