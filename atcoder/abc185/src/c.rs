// https://atcoder.jp/contests/abc185/tasks/abc185_c
// Duodecim Ferra

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        l: u128,
    }

    let mut ans = 1;
    // ans:  combination(l-12+11, 11)
    for i in 1..=11 {
        // 分子の計算
        ans *= l - i;
        // 分母の計算
        ans /= i;
    }

    println!("{}", ans);
}
