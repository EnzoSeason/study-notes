use rand::prelude::*;
use std::io;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..11);

    println!("Guess the number between 1 and 10: ");
    loop {
        let mut user_input = String::new();
        let guess = match io::stdin().read_line(&mut user_input) {
            Ok(_) => match user_input.trim().parse::<u32>() {
                Ok(num) => num,
                Err(_) => {
                    println!("Please enter a number!");
                    continue;
                }
            },
            Err(_) => {
                println!("Error reading input!");
                continue;
            }
        };

        if guess == secret_number {
            println!("You win!");
            break;
        } else {
            println!("Try again!");
        }
    }
}
