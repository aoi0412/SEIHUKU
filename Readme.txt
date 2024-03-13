仮想環境のアクティベート
    Windows(CommandPrompt)
        .\seihuku\Scripts\activate
    Mac,Linux
        .seihuku/bin/activate

仮想環境でのデバッグ
    ctrl+shift+Pでコマンドパレットを開く
    python: Select Interpreterを検索
    仮想環境のPythonを選択する

実行環境
    python:3.12.0
    numpy:1.26.4
    opencv-contrib-python:4.9.0.80
    opencv-python:4.9.0.80
    pip:23.2.1

説明
    createMarker.py：マーカーの画像を生成する関数
    hirano.py：担当した関数
    main.py：以前作成した関数．カメラを起動し，マーカーを検知した瞬間にマーカーの場所を検知．その後2点を選択すると実際の距離が出てくる関数（詳しくは平野まで）

    ※実行環境は上を参考にしてください