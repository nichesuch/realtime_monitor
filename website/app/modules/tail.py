# 正規表現が使えるsplitを使う
import re

def tail(fn, n=None, pointer=None):
    now = None
    # pointerを渡されたら、そこから先の行を返す
    # nを与えないときは最後の行だけ単体で返す
    if pointer is not None:
        n = 1
        is_list = True
    elif n is None:
        n = 1
        is_list = False
    # nは自然数
    elif type(n) != int or n < 1:
        raise ValueError('n has to be a positive integer')
    # nを与えたときはn行をリストにまとめて返す
    else:
        is_list = True

    # 128 * n バイトずつ読む
    chunk_size = 64 * n

    # seek()はバイナリモード以外だと予期せぬ挙動を見せるので'rb'を指定する
    with open(fn, 'rb') as f:
        if pointer is not None:
            print(pointer)
            now = f.seek(pointer)
            chunk = f.read().decode()
            chunk = chunk.strip()
            now = f.tell()
            print(chunk)
            return chunk, now
        # ヘッダーを除いた左端の位置を探すために最初の一行(ヘッダーの行)を読む
        f.readline()
        # 一番最初の改行コードを左端(ファイルの末尾から読んでいったときの終端)とする
        # -1は'\n'の1バイト分
        left_end = f.tell() - 1

        # ファイルの末尾(2)から1バイト戻る. read(1)で読むため
        f.seek(-1, 2)

        # ファイル末尾には空行や空白などがあることも多いから
        # それらを除いたファイルの最後の文字の位置(右端)を探す
        while True:
            if f.read(1).strip() != b'':
                # 右端
                right_end = f.tell()
                break
            # 1歩進んだから2歩下がる
            f.seek(-2, 1)

        # 左端までのまだ読んでいない残りのバイト数
        unread = right_end - left_end

        # 読んだ行数. これがn以上になればn行読み取れたことになる
        num_lines = 0

        # 読んだバイト列をつなげていくための変数
        line = b''
        while True:
            # 未読のバイト数がchunk_sizeより小さくなったら, 端数をchunk_sizeとする
            if unread < chunk_size:
                chunk_size = f.tell() - left_end

            # 現在地からchunk_sizeだけファイルの先頭側に移動する
            f.seek(-chunk_size, 1)

            # 移動した分だけ読む
            chunk = f.read(chunk_size)

            # つなげる
            line = chunk + line

            # readでまた進んでしまったのでまた先頭側にchunk_size移動する
            now = f.seek(-chunk_size, 1)

            # 未読バイト数を更新する
            unread -= chunk_size

            # 改行コードが含まれるなら
            if b'\n' in chunk:
                # 改行コードの数だけnum_linesをカウントアップ
                num_lines += chunk.count(b'\n')

                # 読んだ行数がn行以上, もしくは未読のバイト数が0になったら終了の合図
                if num_lines >= n or not unread:
                    # 最後に見つけた改行コード
                    leftmost_blank = re.search(rb'\r?\n', line)

                    # 最後に見つけた改行コードより前の部分は不要
                    line = line[leftmost_blank.end():]

                    # バイト列を文字列に変換
                    line = line.decode()

                    # 改行コード'\r\n' または\n'で区切って配列に変換する
                    lines = re.split(r'\r?\n', line)

                    # 最後に後ろからn個取り出し, float型に変換して返す
                    #result = [list(map(float, line.split(','))) for line in lines[-n:]]
                    
                    # 最後のポインタ位置を取得
                    now = f.seek(0, 2)

                    # nを指定しなかったときは最後の一行を単体で返す
                    if not is_list:
                        return lines[-1], now
                    else:
                        return lines, now

if __name__ == '__main__':
    print("tail module")