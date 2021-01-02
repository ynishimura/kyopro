// https://atcoder.jp/contests/abc185/tasks/abc185_a
// Preparetion

use proconio::*;

fn main() {
    input! {
        a: [usize; 4]
    }
    println!("{}", a.iter().min().unwrap());
}
