use std::io::*;
use std::str::FromStr;

fn read<T: FromStr>() -> T {
    let stdin = stdin();
    let stdin = stdin.lock();
    let token: String = stdin
        .bytes()
        .map(|c| c.expect("failed to read char") as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect();
    token.parse().ok().expect("failed to pase token")
}

fn main() {
    let n: usize = read();
    let mut v = vec![0; 101];

    // collect
    for _ in 0..n {
        let t = read::<usize>();
        v[t] += 1;
    }

    // diff count
    let mut count = 0;
    for i in 0..101 {
        if v[i] != 0 {
            count += 1;
        }
    }
    println!("{}", count)
}
