use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();

    println!("{}", s.replace("2017", "2018"));
}
