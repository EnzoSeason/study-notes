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


    let my_array = [1, 2, 3];
    println!("{}", my_array[0]);
    let my_filled_array = [1; 10];
    println!("{:?}", my_filled_array);

}
