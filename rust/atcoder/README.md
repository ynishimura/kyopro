# コマンド

- コンテスト作成

```
$ cargo compete new abc203
```

- 問題開く

```
$ cd abc203
$ cargo compete open --bin a
```

- テストケースダウンロード(Dropbox にあれば)

```
$ cd abc203
$ cargo compete d --full --overwrite --bin a
```

※アクセストークンファイルの置き場（/Users/Alice/Library/Application Support/cargo-compete/tokens/dropbox.json）

- テスト実行

```
$ cd abc203
$ cargo compete test
```

- 提出情報取得(cargo compete retrieve submission-summaries)

```
$ cd abc203
$ cargo compete r ss
```

- 提出(cargo compete submit)

```
$ cd abc203
$ cargo compete submit a
```

https://github.com/qryxip/cargo-compete/blob/master/README-ja.md#%E8%A8%AD%E5%AE%9A
