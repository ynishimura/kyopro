# 概要

## アルゴリズム

### 幅優先探索

最短距離を求めるアルゴリズム

## 参考資料

https://atcoder.jp/contests/abc007/tasks/abc007_3

https://www.youtube.com/watch?v=6QKW-HQV-hE

## python

deque(デック)を使うのが便利

- 右 or 左から入れて、左 or 右から出す
  - 便利

ビットシフト演算

1<<3：1 を 3 ビットずらす

```python
>>> 1<<3
8
>>> bin(1<<3)
'0b1000'
```

無限
INF = 1<<60

リストを unpack する
\*hoge
