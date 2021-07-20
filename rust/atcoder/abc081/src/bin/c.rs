use proconio::input;
use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        k: usize,
        a: [usize; n],
    }
    let mut h = HashSet::new();
    for i in 0..n {
        h.insert(a[i]);
    }

    let l = h.len();
    let mut c = HashMap::new();
    for &i in &a {
        *(c.entry(i).or_insert(0)) += 1;
    }

    let mut cnt = Vec::new();
    for i in h {
        cnt.push(*c.get(&i).unwrap_or(&0));
    }

    cnt.sort();
    let mut ans = 0;
    if l > k {
        for i in 0..l - k {
            ans += cnt[i];
        }
    }

    println!("{}", ans);
}
