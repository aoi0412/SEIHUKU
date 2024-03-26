# 飯田くんと長井くん用

1. ターミナルを見る
2. Running on http://127.0.0.1 というのがあるか確認（上にスクロールしたらあるかもなのでそれも確認。それでも無ければ平野まで）
3. ブラウザにて http://127.0.0.1 にアクセス
4. html は iida.html nagai.html ファイルを編集，css は app/static/にファイルを作って編集

ファイルを編集してブラウザに反映させたいときはブラウザをリロードしましょう〜

何か困ったら平野まで相談（Slack でも可）

# はじめに

## 仮想環境に入ります

### Linux，Mac の人

. ./seihuku/bin/activate

### Windows の人

.\seihuku\Scripts\activate

# アプリの開始の仕方

## Web サーバーを立てる

Web ブラウザで見れるように立ち上げ得る URL を生成する

    python3 run.py

#　ファイル構成について

## app/templates

ここに HTML を書いていく

## app/static

ここに css とか画像とかを入れる

## app/app.py

これはアプリの全体を管理するファイル
どういう時にどの HTML に飛ぶのかを指定したりする

## run.py

アプリを立ち上げる時に実行するもの
