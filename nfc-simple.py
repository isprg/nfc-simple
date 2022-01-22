import PySimpleGUI as sg
import nfc
import time
import binascii
import random
import datetime

class Gururi():
    def __init__(self):
        sg.theme('DarkBrown2')
        self.layout =[[sg.Text('ぐるりパワースポット')],
                 [sg.Text('パワースポットの色'), sg.Text(key='-spotcolor-', size=(40,1))],
                 [sg.Text('ハムスタンNFCID'), sg.Text(key='-IDm-', size=(40,1))],
                 [sg.Text('ハムスタンの色'), sg.Text(key='-color-', size=(40,1))],
                 [sg.Text(key='-msg-', size=(40,1))]]
        self.window = sg.Window('NFCタグリーダー', self.layout, size=(300, 150))
        self.spcolor = 0 # spot color
        #print(dir(self.window))
    def compare_color(self):
        # spot colorとnfccolorを比較する
                
        if self.idmcolor == 0:
            print("赤です")
            cr.window['-color-'].update("赤")
        elif self.idmcolor == 1:
            print("青です")
            cr.window['-color-'].update("青")
        elif self.idmcolor == 2:
            cr.window['-color-'].update("緑")

        if self.spcolor == self.idmcolor:
            cr.window['-msg-'].update("ぐるりパワーげっと！")
        else:
            cr.window['-msg-'].update("")
        
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
            try:
                self.idm = int(binascii.hexlify(tag._nfcid).decode(),16) # bytesをdecodeして文字列にする->10進整数に変換
                self.idmcolor = self.idm % 3
                #print("IDm : " + str(self.idm))
                self.window['-IDm-'].update(str(self.idm))
                self.compare_color()
                
            except AttributeError:# たまに AttributeError: 'NoneType' object has no attribute '_nfcid' が発生するので対策
                print("ID読み込み失敗")
                

            #print(dir(tag))
            #tagdump=tag.dump()
 
        clf.close()
if __name__ == '__main__':
    cr = Gururi()
    store_status = 0 #スポットカラーを更新するかどうかを評価する変数

    while True:
        #time.sleep(1)
        event, values = cr.window.read(timeout=10,timeout_key='-timeout-')
        if event == sg.WIN_CLOSED:
            break
        elif event in '-timeout-':
            dt = datetime.datetime.now()
            status = dt.second // 5
            if store_status != status: #5秒に1度更新されるstatusが変化したときにだけスポットカラーを変化させる
                cr.spcolor = random.randint(0,2)
                store_status = status
            if cr.spcolor == 0:
                strspcolor = "赤"
            elif cr.spcolor == 1:
                strspcolor = "青"
            elif cr.spcolor == 2:
                strspcolor = "緑"
            cr.window['-spotcolor-'].update(strspcolor)
            cr.check_ic()
            
    cr.window.close()
