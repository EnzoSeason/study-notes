fn longer_string<'a>(string_1: &'a str, string_2: &'a str) -> &'a str {
    if string_1.len() > string_2.len() {
        string_1
    } else {
        string_2
    }
}

struct Person<'a> {
    name: &'a str,
}

impl<'a> Person<'a> {
    fn greet<'b>(&self, msg: &'b str) -> &'b str {
        println!("{} says {}", self.name, msg);
        msg
    }
}

fn main() {
    let string_1 = String::from("abcd");
    let string_2 = String::from("xyz");

    let result = longer_string(&string_1, &string_2);
    println!("The longer string is {}", result);

    let person = Person { name: "John" };
    println!("{}", person.greet("Hello"));
}
