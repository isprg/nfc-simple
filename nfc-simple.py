import PySimpleGUI as sg
import nfc
import time
import binascii

class Gururi():
    def __init__(self):
        sg.theme('DarkBrown2')
        self.layout =[[sg.Text('ぐるりパワースポット')],
                 [sg.Text('NFCID'), sg.Text(key='-IDm-', size=(40,1))],
                 [sg.Text('色'), sg.Text(key='-color-', size=(40,1))]]
        self.window = sg.Window('NFCタグリーダー', self.layout, size=(300, 120))
        #print(dir(self.window))
        
    def check_ic(self):
        #print('Waiting Now')
        # usb接続のNFCリーダを定義
        clf = nfc.ContactlessFrontend('usb')
        target = clf.sense(nfc.clf.RemoteTarget("106A"), iterations=1, interval=1)
        #target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
        #カードが見つかったら読み取りに入る
        if not target is None:
            tag = nfc.tag.activate(clf, target)
            #IDmのみ取得して表示
            # たまに AttributeError: 'NoneType' object has no attribute '_nfcid' が発生する
            try:
                self.idm = binascii.hexlify(tag._nfcid)
                #print("IDm : " + str(self.idm))
                self.window['-IDm-'].update(str(self.idm))
            except AttributeError:
                print("ID読み込み失敗")
                

            #print(dir(tag))
            #tagdump=tag.dump()
 
        clf.close()
if __name__ == '__main__':
    cr = Gururi()
    while True:
        #time.sleep(1)
        event, values = cr.window.read(timeout=10,timeout_key='-timeout-')
        if event == sg.WIN_CLOSED:
            break
        elif event in '-timeout-':
            cr.window['-color-'].update("赤")
            cr.check_ic()
            
    cr.window.close()
