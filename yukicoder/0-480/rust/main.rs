use std::io::*;
use std::str::*;

fn read<T: FromStr>(sl: &mut StdinLock) -> Option<T> {
    let s = sl.by_ref().bytes().map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>();

    s.parse::<T>().ok()
}

fn main() {
    let s = stdin();
    let mut sl = s.lock();

    if let Some(n) = read::<i32>(&mut sl) {
        let sum = (1..(n+1)).sum::<i32>();
        println!("{}", sum)
    }
}