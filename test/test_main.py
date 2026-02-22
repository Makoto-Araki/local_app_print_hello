import pytest
import sys
import pathlib

# プロジェクトルートをsys.pathに追加
ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

# テスト対象のモジュール
from main import main

def test_main_outputs_hello_world(capsys):
    """ main()が 'Hello World' を出力することを検証する
    """

    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"
