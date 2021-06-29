use std::io::*;
use std::str::FromStr;
use std::usize;

fn read<T: FromStr>() -> T {
    let stdin = stdin();
    let stdin = stdin.lock();
    let token: String = stdin
        .bytes()
        .map(|c| c.expect("failed to read char") as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect();
    token.parse().ok().expect("failed to parse token")
}

fn main() {
    let n: usize = read();
    let mut vec = vec![0; n];

    for i in 0..n {
        let a: i32 = read();
        vec[i] = a;
    }
    let mut res: i32 = 0;
    loop {
        let mut exist_odd: bool = false;
        for i in 0..n {
            if vec[i] % 2 != 0 {
                exist_odd = true;
            }
        }

        if exist_odd {
            break;
        }

        for i in 0..n {
            vec[i] /= 2;
        }

        res += 1;
    }
    println!("{}", res);
}
