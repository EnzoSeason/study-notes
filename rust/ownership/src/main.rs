fn main() {
    let message = String::from("Ownership is cool!");
    update_message(message.clone());
    println!("{}", message);
}

fn update_message(old_message: String) {
    println!("{}", old_message);
}
