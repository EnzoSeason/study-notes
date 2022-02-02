use std::mem;

struct Rectangle<T, U> {
    width: T,
    height: U,
}

impl<T, U> Rectangle<T, U> {
    fn get_width(&self) -> &T {
        &self.width
    }
}

impl Rectangle<f64, f64> {
    fn area(&self) -> f64 {
        self.width * self.height
    }
}

fn get_bigger<T: PartialOrd>(first: T, second: T) -> T {
    if first > second {
        first
    } else {
        second
    }
}

fn get_sum<T: std::ops::Add<Output = T>>(first: Box<T>, second: Box<T>) -> Box<T> {
    Box::new(*first + *second)
}

fn main() {
    let rect = Rectangle {
        width: 30,
        height: 50.0,
    };
    println!("rect's height is {}, width is {}", rect.height, rect.width);
    print!("rect's width is {}", rect.get_width());

    let rect_f64 = Rectangle {
        width: 30.0,
        height: 50.0,
    };
    println!("rect2's area is {}", rect_f64.area());

    println!("The bigger one is {}", get_bigger(10, 20));

    println!(
        "The memory used on stack for a rectangle: {}",
        mem::size_of_val(&rect)
    );
    let boxed_rect = Box::new(rect);
    println!(
        "The memory used on stack for a boxed rectangle: {}",
        mem::size_of_val(&boxed_rect)
    );
    println!(
        "The memory used on heap for a boxed rectangle: {}",
        mem::size_of_val(&*boxed_rect)
    );

    println!(
        "The sum of two numbers: {}",
        get_sum(Box::new(10), Box::new(20))
    );
    println!(
        "The sum of two numbers: {}",
        get_sum(Box::new(1.1), Box::new(2.2))
    );
}
