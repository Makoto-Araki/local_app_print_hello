# local_app_print_hello 

Windows アプリの CI/CD 導入サンプル

このリポジトリは、Python で作成されたシンプルなコンソールアプリケーション（`Hello World`）を  PyInstaller を使って Windows 実行ファイル（.exe）化し、CI/CD パイプラインでビルド・配布するためのサンプルです。

---

## 📦 プロジェクト概要

- **main.py**  
  コンソールアプリで標準出力に `Hello World` をプリントします。

- **main.spec**  
  PyInstaller 用のビルド定義ファイル。

- **requirements.txt**  
  PyInstaller 等の依存ライブラリを固定版で管理します。

- **.github/workflows/**  
  GitHub Actions を使った CI/CD ワークフロー定義。

---

## 🚀 セットアップ

### 1. リポジトリのクローン

```bash
## リポジトリのクローン
$ git clone https://github.com/Makoto-Araki/local_app_print_hello.git

## ディレクトリ移動
$ cd local_app_print_hello
```

### 2. 仮想環境の構築(推奨)

```bash
## 仮想環境を作成
$ python -m venv venv

## 仮想環境を起動
$ venv\Scripts\activate
```

### 3. 依存関係のインストール
```bash
$ pip install -r requirements.txt
```

### 4. アプリ実行
```bash
$ python main.py
```

### 5. ビルド(Pyinstaller)
```bash
$ pyinstaller main.spec
```

### 6. 仮想環境の停止(推奨)
```bash
$ venv\Scripts\deactivate.bat
```
