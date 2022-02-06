use std::fs;
use std::io;

fn read_file(file_name: &str) -> Result<String, io::Error> {
    let result = fs::read_to_string(file_name)?;
    Ok(result)
}

fn main() {
    let file_string = read_file("src/test.txt");
    let contents = match file_string {
        Ok(contents) => contents,
        Err(e) => panic!("There was a problem reading the file: {:?}", e),
    };
    println!("{}", contents);
}
