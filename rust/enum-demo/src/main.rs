enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
}

impl Shape {
    fn area(&self) -> f64 {
        match *self {
            Shape::Circle(r) => 3.14 * (r * r),
            Shape::Rectangle(x, y) => x * y,
        }
    }
}

enum Location {
    Unknown,
    Anonymous,
    Known(f64, f64),
}

impl Location {
    fn display(&self) {
        match *self {
            Location::Unknown => println!("I don't know where I am."),
            Location::Anonymous => println!("I am nobody, nobody."),
            Location::Known(x, y) => println!("I am at ({}, {})", x, y),
        }
    }
}

fn main() {
    let rect = Shape::Rectangle(3.0, 4.0);
    println!("Area of rectangle is {}", rect.area());
    let circle = Shape::Circle(3.0);
    println!("Area of circle is {}", circle.area());

    let nums = [1, 2, 3];
    let my_num = nums.get(0);
    let res = match my_num {
        Some(n) => n,
        None => &0,
    };
    println!("{}", res);

    match my_num {
        Some(1) => println!("One"),
        _ => (), // Do nothing
    }

    if let Some(1) = my_num {
        println!("One");
    }

    let unknown = Location::Unknown;
    unknown.display();

    let anonymous = Location::Anonymous;
    anonymous.display();

    let known = Location::Known(1.0, 2.0);
    known.display();
}
