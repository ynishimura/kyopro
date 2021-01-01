// https://atcoder.jp/contests/abc186/tasks/abc186_d
// Sum of difference

// 差の絶対値の和を計算する

/*
計算時間を短縮する

- sortする
    - 2つ選びだけなので順番は関係ない
    - 絶対値を外すことができる

ex) 1 2 5 14

sortして「Aj-Ai」の和を求める形にする
2 - 1
5 - 1
5 - 2

Ajの和は何個候補があるかをかけた値

Aiの和をループで管理する
1 2
から
1 2 5
になるとき
+5するだけで値を管理できるので計算量が少なくなる

*/

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut a: [i64; n],
    }
    a.sort();
    let mut ans = 0;
    let mut sum = a[0];
    let mut cnt = 1;
    for i in 1..n {
        ans += a[i] * cnt - sum;
        sum += a[i];
        cnt += 1;
    }
    println!("{}", ans);
    /*
    ans = 0
    for i in range(1, n):
        ans += A[i] * i
        ans -= A[i-1] * (n-i)
    print(ans)

    */

    /*

        let mut add_cnt: isize = a[0] * (n as isize - 1);
        let mut sub_cnt: isize = 0;
        for i in 1..n {
            add_cnt += a[i as usize] * (n - i - 1);
            sub_cnt += a[i as usize] * i;
        }

        let ans = (add_cnt - sub_cnt).abs();
        println!("{}", ans);

    */

    /*
    for i in 1..n {
      culc[i] = culc[i-1] + vals[i];
    }

    let inn = n as isize;
    let mut result = culc[n-1] - vals[0] * inn;
    for i in 1..n {
      let sum = culc[n-1] - culc[i-1];
      let v = vals[i] * (inn - i as isize);
      result += sum - v;
    }
    println!("{}", result);
      */
}
