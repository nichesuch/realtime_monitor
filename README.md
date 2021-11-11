# RealTime Monitor of Django+Plotly Streaming

DjangoとPlotlyで加速度情報のリアルタイムモニターを作成
加速度情報は以下の項目のCSV
- Unixtime(秒数,ミリ秒は小数点で指定)
- 加速度x
- 加速度y
- 加速度z

CSVに追記していくと、最終行を取得してグラフに追加表示される。

### Reference
https://docs.djangoproject.com/ja/3.2/
https://plotly.com/javascript/streaming/

### Need
- python 3.7.1
- pip 21.3.1

### Install
```
$ cd realtime_monitor
$ python -m venv .env
$ . .env/bin/activate
$ pip install -r requirements.txt
```

### Config
`website/website/settings.py`

```
LOG_FILE_PATH = '/tmp/sample.log' #ログファイルのパス
SAMPLE_DATA = True #ログではなくダミーデータを表示
MONITOR_RANGE_MSEC = 12000 #モニタに表示する範囲(ミリ秒数) 初期値
MONITOR_INTERVAL_MSEC = 1000 #モニタの更新頻度(ミリ秒数)　初期値
```

### run
```
$ cd realtime_monitor
$ cd website
$ python manage.py runserver 0.0.0.0:8000
```

終了する時はCtrl+C

### Usage
ブラウザで以下にアクセス
http://127.0.0.1:8000/

- 表示開始
  - Startボタンを押下
- 表示停止
  - Stopボタンを押下

### Tips
ログファイル(/tmp/sample.log)にダミーデータをひたすら追加するコマンド
- for Linux
`for ((i=0; i<1000; i++)); do echo $(date +%s.%3N),$RANDOM,$RANDOM,$RANDOM >> /tmp/sample.log; done`
- for Mac(need gdate)
`for ((i=0; i<1000; i++)); do echo $(gdate +%s.%3N),$RANDOM,$RANDOM,$RANDOM >> /tmp/sample.log; done`

