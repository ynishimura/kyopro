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

## target の持ち方

コンテスト用のプロジェクトを作成する前に、次の設定をすることをおすすめします。

プロジェクトを並べる予定のディレクトリで次のコマンドを実行してください。

`$ mkdir ./.cargo $ echo '[build]\ntarget-dir = "target"' > ./.cargo/config.toml`

これでこのディレクトリに`[build.target-dir](https://doc.rust-lang.org/cargo/reference/config.html#buildtarget-dir)`が設定され、そこから下にあるプロジェクト全体が一つの`target`ディレクトリを共有するようになります。 そうすることで外部クレートを使う場合、毎回それらのビルドが走ることがなくなります。

## 実行方法

プロジェクトフォルダに移動して

```
$ cargo run --bin a
```

```
$ cargo test --bin a
```
