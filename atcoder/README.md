## プロジェクトの作り方

Cargo の workspace セクションを使います。このセクションに members というキーを追加し、その値にはパッケージ名を文字列にした配列を置きます。例えばそれは以下のようになります。

所謂、モノレポ構成

```
[workspace]
members = [
  "plus-one",
  "there-is-plus-one-as-dependency"
]
```

複数の main を管理する方法
https://qiita.com/tatsuya6502/items/7c41dd981ffa56bcab99

## 実行方法

プロジェクトフォルダに移動して

```
$ cargo run --bin main2
```
