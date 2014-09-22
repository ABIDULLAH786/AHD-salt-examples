◯ディレクトリ構成
command：
　scriptディレクトリ内の命令を実行するためのシェルスクリプト
script：
　個々の命令を書いたPythonスクリプト



◯シェルスクリプトの構成
common.sh：
　全シェルスクリプトで共通の変数を定義。
　「source common.sh」でインクルードする。
　HOST*に各ペッパーのIPを指定する。

その他のshファイル：
　各命令を５体のペッパーに送信する。



◯便利ツール
CommandFileMaker.sh
　Finderから直接ダブルクリックでシェルスクリプトを実行するための.commandファイルを作成する。
　ターミナルから「sh CommandFileMaker.sh ###.sh」というように
　.commandファイルにしたいシェルスクリプトを第１引数に指定して実行する。
　作成した.commandファイルはFinderからダブルクリックで実行できる。