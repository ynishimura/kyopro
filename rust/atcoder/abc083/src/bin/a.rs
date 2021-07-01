use std::cmp::Ordering::*;
use std::io::stdin;
use std::str::FromStr;

fn read<T: FromStr>() -> T {
    let mut s = String::new();
    stdin().read_line(&mut s).ok();
    s.trim().parse().ok().unwrap()
}

fn read_vec<T: FromStr>() -> Vec<T> {
    read::<String>()
        .split_whitespace()
        .map(|e| e.parse().ok().unwrap())
        .collect()
}

fn main() {
    let abcd: Vec<u8> = read_vec::<u8>();
    let left = abcd[0] + abcd[1];
    let right = abcd[2] + abcd[3];
    /*
    if left > right {
        println!("Left");
    } else if left < right {
        println!("Right");
    } else {
        println!("Balanced");
    }
    */

    let ans = match left.cmp(&right) {
        Equal => "Balanced",
        Greater => "Left",
        Less => "Right",
    };
    println!("{}", ans);
}
