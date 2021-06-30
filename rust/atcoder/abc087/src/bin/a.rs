use std::io::stdin;
use std::str::FromStr;

fn read<T: FromStr>() -> T {
    let mut s = String::new();
    stdin().read_line(&mut s).ok();
    s.trim().parse().ok().unwrap()
}

fn main() {
    let x: u32 = read::<u32>();
    let a: u32 = read::<u32>();
    let b: u32 = read::<u32>();
    let tmp: u32 = x - a;
    println!("{}", tmp % b);
}
