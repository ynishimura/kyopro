use cli_test_dir::*;

const BIN: &'static str = "./b";

#[test]
fn sample1() {
    let testdir = TestDir::new(BIN, "");
    let output = testdir
        .cmd()
        .output_with_stdin(
            r#"5 3
10 30 40 50 20"#,
        )
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), "30\n");
    assert!(output.stderr_str().is_empty());
}
