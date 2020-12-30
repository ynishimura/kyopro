// https://atcoder.jp/contests/abc186/tasks/abc186_a
// Brick

#![allow(unused_imports)]
use num::{
    abs,
    integer::{gcd, ExtendedGcd},
};
use permutohedron::LexicalPermutation;
use proconio::{fastout, input, marker::*};
use std::collections::{BTreeMap, BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};
use text_io::read;

#[fastout]
fn main() {
    input! {
        n: i32,
        w: i32,
    }

    println!("{}", n / w); //切り捨てになる
}
