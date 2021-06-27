use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: usize,
        b:usize,
        c:usize,
    }
    let ans = {
        if a == b {
            c
        } else if a == c {
            b
        } else if b == c {
            a
        } else {
            0
        }
    };
    print!("{}", ans)
}
