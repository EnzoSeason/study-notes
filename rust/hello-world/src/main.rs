fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn main() {
    let integer = 3;
    print_type_of(&integer);

    let float = 3.14;
    print_type_of(&float);

    let a_str = "hello";
    println!("{}", a_str);

    let is_true = true;
    println!("{}", is_true);

    let my_tuple = (1, "cool", true);
    println!("{}", my_tuple.0);
    let (a, b, c) = my_tuple;
    println!("{} {} {}", a, b, c);

    let my_filled_array = [1; 10];
    println!("{:?}", my_filled_array);

    if integer == 3 {
        println!("{}, condition", integer);
    } else if integer == 4 {
        println!("{}", integer);
    } else {
        println!("{}", integer);
    }

    let mut counter = 0;
    while counter < 10 {
        // println!("{}", counter);
        counter += 1;
    }

    let mut counter = 0;
    loop {
        // println!("{}", counter);
        counter += 1;
        if counter == 10 {
            break;
        }
    }

    let my_array = [1, 2, 3, 4, 5];
    for i in my_array {
        println!("{}", i);
    }

}
