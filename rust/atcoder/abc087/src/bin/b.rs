use std::io::stdin;
use std::str::FromStr;

fn read<T: FromStr>() -> T {
    let mut s = String::new();
    stdin().read_line(&mut s).ok();
    s.trim().parse().ok().unwrap()
}

fn main() {
    let a: u32 = read::<u32>();
    let b: u32 = read::<u32>();
    let c: u32 = read::<u32>();
    let x: u32 = read::<u32>();
    let mut cnt: u32 = 0;

    for i in 0..a + 1 {
        for j in 0..b + 1 {
            for k in 0..c + 1 {
                if x == 500 * i + 100 * j + 50 * k {
                    cnt += 1;
                }
            }
        }
    }
    println!("{}", cnt);
}
