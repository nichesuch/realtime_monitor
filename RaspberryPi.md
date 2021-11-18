# リアルタイムモニタをラズパイで動かす。

## 必要なものをインストール
```
$ python3 --version
Python 3.7.3

$ sudo apt install python3-pip

$ pip --version
pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)

$ sudo apt install python3-venv

$ sudo apt install git
```

### プログラムを落としてくる。
```
$ git clone https://github.com/nichesuch/realtime_monitor.git
```

### 仮想環境を作って必要なpythonライブラリをインストール
```
$ cd realtime_monitor
$ python3 -m venv .env
$ . .env/bin/activate
(.env) $ pip install -r requirements.txt
```
**以降、.envの環境で行う。**

### Djangoのマイグレート
```
$ python3 manage.py migrate
```

### 環境に合わせた設定
```
$ vi website/website/settings.py

ALLOWED_HOSTS = ['999.999.999.999'] #ラズベリーパイのIPアドレス

LOG_FILE_PATH = '/tmp/sample.log' #ログファイルのパス
SAMPLE_DATA = False #ログではなくダミーデータを表示
MONITOR_RANGE_MSEC = 12000 #モニタに表示する範囲(ミリ秒数) 初期値
MONITOR_INTERVAL_MSEC = 1000 #モニタの更新頻度(ミリ秒数)　初期値
```

### 実行
```
$ cd website
$python3 manage.py runserver 0.0.0.0:8000
```
