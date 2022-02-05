use std::fmt;

#[derive(PartialEq, PartialOrd)]
struct Satelite {
    name: String,
    velocity: f64,
}

struct SpaceStation {
    name: String,
    crew_size: u32,
}

impl fmt::Display for SpaceStation {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Space Station {} has {} crew", self.name, self.crew_size)
    }
}

trait Describable {
    fn describe(&self) -> String {
        "Hello".to_string()
    }
}

impl Describable for Satelite {
    fn describe(&self) -> String {
        format!("{} is travelling at {} km/s", self.name, self.velocity)
    }
}

impl Describable for SpaceStation {
    fn describe(&self) -> String {
        format!("{} has a crew of {}", self.name, self.crew_size)
    }
}

fn compare<T>(a: T, b: T)
where
    T: PartialEq + PartialOrd + fmt::Display,
{
    if a == b {
        println!("{} and {} are equal", a, b);
    } else if a > b {
        println!("{} is greater than {}", a, b);
    } else {
        println!("{} is less than {}", a, b);
    }
}

fn get_displayable() -> impl fmt::Display {
    "hi"
}

fn main() {
    let bad_boy = Satelite {
        name: "Bad boy".to_string(),
        velocity: 17.2,
    };

    let home_ship = SpaceStation {
        name: "Home Ship".to_string(),
        crew_size: 100,
    };

    println!("{}", bad_boy.describe());
    println!("{}", home_ship.describe());
    println!("{}", home_ship);
    
    compare(1, 2);

    println!("{}", get_displayable());
}
