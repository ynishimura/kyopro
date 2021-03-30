// https://atcoder.jp/contests/dp/tasks/dp_b

// https://www.youtube.com/watch?v=FvHII8WufWg&list=PL3Hpv03CoZ24l1sf3ogcAuF1pqmgyKzqL&index=3
// https://qiita.com/drken/items/dc53c683d6de8aeacf5a#b-%E5%95%8F%E9%A1%8C---frog-2

use proconio::input;

fn main() {
    input! {
        n: usize, // 足場の数
        k: usize, // ジャンプできる足場
        hn: [i64; n], // 足場の高さ
    }
    println!("{}", n);
}
