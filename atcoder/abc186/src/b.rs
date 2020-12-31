// https://atcoder.jp/contests/abc186/tasks/abc186_b
// Blocks on Grid

// 最小値を選び、その数に置き換えていく。
// なぜ最小値を基準とするかは取り除くことしかできないため

// 二次元配列を用意する
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        a: [[usize; w]; h],
    }

    let mut tot = 0;
    let mut min_a = 100;

    for i in 0..h {
        for j in 0..w {
            tot += a[i][j];

            min_a = if a[i][j] < min_a { a[i][j] } else { min_a };
        }
    }

    let ans = tot - h * w * min_a;

    println!("{}", ans);
}
