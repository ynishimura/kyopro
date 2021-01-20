// https://atcoder.jp/contests/dp/tasks/dp_a

// https://www.youtube.com/watch?v=wspbr3zQzkg&list=PL3Hpv03CoZ24l1sf3ogcAuF1pqmgyKzqL&index=2
// https://qiita.com/drken/items/dc53c683d6de8aeacf5a

use proconio::input;

fn main() {
    input! {
        n: usize, // 足場の数
        hn: [i64; n], // 足場の高さ
    }
    let mut dp = vec![std::i64::MAX; n]; // 配列作成
    dp[0] = 0; //はじめはコスト０からスタートする、
    for i in 0..n {
        if i > 0 {
            // 一つ前から飛んでくるパターン
            // 一つ前のコスト + 一つ飛ぶコスト足した
            // はじめの処理、一つ飛ばししかしないため。-2するとき配列からはみ出るため
            dp[i] = dp[i].min(dp[i - 1] + (hn[i] - hn[i - 1]).abs());
        }
        if i > 1 {
            // ２つ前から飛んでくるパターン
            dp[i] = dp[i].min(dp[i - 2] + (hn[i] - hn[i - 2]).abs());
        }
    }
    println!("{}", dp[n - 1]);
}
