// https://atcoder.jp/contests/abc185/tasks/abc185_b
// Smartphone Addiction

/**

電池が減るイベント、増えるイベントごとに区切って計算


 */
use proconio::*;
use std::cmp::min;

fn main() {
    input! {
        n: i32,
        m: i32,
        t: i32,
        arr: [(i32, i32); m],
    }
    let mut battery = n; // バッテリー最初は満タン
    let mut time = 0; // 時間がどれだけ進んだかのマーカー
    for (t_in, t_out) in arr {
        battery -= t_in - time; // バッテリーが減る
        if battery <= 0 {
            println!("No");
            return;
        }
        // battery = std::cmp::min(n, battery + t_out - t_in);
        battery += t_out - t_in; // バッテリーが増える
        battery = min(battery, n); // バッテリーが満タンのとき、nを超えないようにする
        time = t_out;
    }
    battery -= t - time; //最後の残りの区間分バッテリー減らす
    if battery <= 0 {
        println!("No");
    } else {
        println!("Yes");
    }
}
