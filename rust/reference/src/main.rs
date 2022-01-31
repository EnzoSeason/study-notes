fn main() {
    let message = String::from("Hello, world!");
    let first_world = get_first_world(&message);
    println!("{}", first_world);
}


fn get_first_world(message: &str) -> &str {
    let bytes = message.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &message[0..i];
        }
    }
    
    return message;
}