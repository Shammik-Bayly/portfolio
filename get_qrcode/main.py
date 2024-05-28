import qrcode
img = qrcode.make('https://github.com/Shammik-Bayly')
img.save("qrcode.png")