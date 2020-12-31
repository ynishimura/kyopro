// https://atcoder.jp/contests/abc186/tasks/abc186_c
// 7を含まない数を数える、10進数、8進数

// 10進数、8進数に変換する関数を作るか、メソッドを利用する

// https://atcoder.jp/contests/abc186/submissions/19056475
// 引数にbase(進数)と数を受け取り7を含むか判定する数関数を作る

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let mut ans = 0;
    fn contains7(n: usize, base: usize) -> bool {
        let mut _n = n;
        while _n > 0 {
            if _n % base == 7 {
                return true;
            }
            _n /= base;
        }
        false
    }
    for i in 1..=n {
        if !(contains7(i, 8) || contains7(i, 10)) {
            ans += 1
        }
    }

    println!("{}", ans);
}
