use cli_test_dir::*;

const BIN: &'static str = "./a";

#[test]
fn sample1() {
    let testdir = TestDir::new(BIN, "");
    let output = testdir
        .cmd()
        .output_with_stdin(
            r#"4
10 30 40 20"#,
        )
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), "30\n");
    assert!(output.stderr_str().is_empty());
}
