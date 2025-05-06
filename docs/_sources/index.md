# powパッケージ集

```{toctree}
---
hidden:
---
package_summary/index
apiref
genindex
modindex
```

PythonからWindowsのCOMを使わない機能を使いやすくするパッケージ集です。各パッケージはリポジトリとドキュメントを共有しますが、インストールは別々に可能です。

## パッケージ

|パッケージ|概要|依存関係|
|:--|:--|:--|
|powsid|SID（セキュリティID）。|標準ライブラリ|
|powguid|GUID。comtypesパッケージを使わない場合にGUID型を定義します。|標準ライブラリ|
|powpowerman|電力管理。|powguid|
|powdeviceinfo|デバイス情報。|powguid|

```{mermaid}
flowchart TB
    powsid
    powguid --> powpowerman
    powguid --> powdeviceinfo
```

## インストール

ローカルパッケージとしての利用を想定しています。ダウンロードして次のいずれかの方法でインストールしてください。

1. `powc\pip install e.ps1`実行→パッケージがまとめてインストールされます。
2. 各フォルダの`pip install e.ps1`実行→パッケージをそれぞれインストールできます。
