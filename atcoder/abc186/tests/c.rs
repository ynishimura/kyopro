use cli_test_dir::*;

const BIN: &'static str = "./c";

#[test]
fn sample1() {
    let testdir = TestDir::new(BIN, "");
    let output = testdir
        .cmd()
        .output_with_stdin(
            r#"20
"#,
        )
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), "17\n");
    assert!(output.stderr_str().is_empty());
}
