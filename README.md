# nfc-simple
NFCリーダーとPySimpleGUIのサンプル

起動すると赤青緑の丸が表示される（5秒に1回ランダムに更新）
NFCリーダーにタグを近づけると，赤・青・緑に分類され（IDを3で割った余りで判定），表示されている〇の色と同じ色のタグかそうじゃないかで鳴る音が変わる

## NFCリーダーのセットアップ（Windows）
- Windows環境では下記のとおり（libusbのセットアップは不要だった）
- https://obenkyolab.com/?p=741

## NFCリーダーのセットアップ（raspberry pi)
- 下記のとおり
- https://monomonotech.jp/kurage/raspberrypi/nfc.html
- git環境のみapt-get install git で追加
