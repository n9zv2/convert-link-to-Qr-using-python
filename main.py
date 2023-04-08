import qrcode #this  libary using
def qr(text):# crate finction name qr and hava one parmieter name text 
    qr=qrcode.make(text) #using method qrcode and calling make 
    img=qr.save("make.png") #using mathod save and enter tha name Qr


qr(text =input("enter the link for QR pls : "))#hear calling tha finction and using text and make text input for user can enter link 
      
