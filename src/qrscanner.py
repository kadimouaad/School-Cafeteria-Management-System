import qrcode


class Scanner:

    def Creat_qr_code(self, info_dic):
        myqr = qrcode.make(info_dic)
        myqr.save("myqr.png")
        return myqr

    def decode_qr(self):
        pass





