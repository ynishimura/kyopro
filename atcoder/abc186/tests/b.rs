use cli_test_dir::*;

const BIN: &'static str = "./b";

#[test]
fn sample1() {
    let testdir = TestDir::new(BIN, "");
    let output = testdir
        .cmd()
        .output_with_stdin(
            r#"2 3
2 2 3
3 2 2
"#,
        )
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), "2\n");
    assert!(output.stderr_str().is_empty());
}

#[test]
fn sample2() {
    let testdir = TestDir::new(BIN, "");
    let output = testdir
        .cmd()
        .output_with_stdin(
            r#"3 3
4 3 6
4 4 6
4 4 6
"#,
        )
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), "14\n");
    assert!(output.stderr_str().is_empty());
}
