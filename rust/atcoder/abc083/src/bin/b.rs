use std::io::stdin;
use std::str::FromStr;

fn read<T: FromStr>() -> T {
    let mut s = String::new();
    stdin().read_line(&mut s).ok();
    s.trim().parse().ok().unwrap()
}

fn read_vec<T: std::str::FromStr>() -> Vec<T> {
    read::<String>()
        .split_whitespace()
        .map(|e| e.parse().ok().unwrap())
        .collect()
}

fn main() {
    let nab = read_vec::<u32>();

    let ans = (1..=nab[0])
        .filter(|x| {
            let sum = x
                // stringに変換
                .to_string()
                // 文字列スライスの文字数を表すイテレータへ変換
                .chars()
                // ビット演算をして、それをu32へキャスト
                .map(|c| (c as u8 - b'0') as u32)
                // イテレータの要素u32を合計
                .sum::<u32>();
            nab[1] <= sum && sum <= nab[2]
        })
        .sum::<u32>();
    println!("{}", ans);
}
