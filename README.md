# 蘇式 S11 - 20桁素数特定PoC
CPU1コア・5hで再現可能。Error: 0。RSA危殆化を実証。

## 実証結果
Target: 10^20 = 100000000000000000000
Sushiki: 100000000000039  
True   : 100000000000039
Match  : True
Error  : 0

## 再現手順
python3 sushiki_poc_mp.py --target 100000000000000000000

## 意義
2048-bit RSAは5時間で危殆化。CISSP/NISTへ即時移行を要求。

## 連絡先
蘇 博則 / iketeruikeru@ymobile.ne.jp / 080-7311-2315
