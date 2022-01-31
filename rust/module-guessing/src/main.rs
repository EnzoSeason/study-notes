use rand::prelude::*;
use std::io;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..11);

    println!("Guess the number between 1 and 10: ");
    loop {
        let mut user_input = String::new();
        io::stdin()
            .read_line(&mut user_input)
            .expect("Failed to read line");
        let guess: u32 = user_input.trim().parse().expect("Fail to parse guess");

        if guess == secret_number {
            println!("You win!");
            break;
        } else {
            println!("Try again!");
        }
    }
}
