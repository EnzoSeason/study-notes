struct Shuttle {
    name: String,
    crew_size: u16,
    fuel: f64,
}

impl Shuttle {
    fn new(name: &str) -> Shuttle {
        Shuttle {
            name: String::from(name),
            crew_size: 0,
            fuel: 0.0,
        }
    }
    
    fn get_name(&self) -> &str {
        &self.name
    }

    fn add_fuel(&mut self, amount: f64) {
        self.fuel += amount;
    }
}

struct Color(u8, u8, u8);

fn get_red_value(color: &Color) -> u8 {
    color.0
}

struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    fn new(width: f64, height: f64) -> Rectangle {
        Rectangle {
            width,
            height,
        }
    }

    fn get_area(&self) -> f64 {
        self.width * self.height
    }

    fn scale(&mut self, factor: f64) {
        self.width *= factor;
        self.height *= factor;
    }
}


fn main() {
    let car = Shuttle {
        name: String::from("Car"),
        crew_size: 11,
        fuel: 1.0,
    };
    println!("Car's crew size is {}.", car.crew_size);

    let mut bus = Shuttle {
        name: String::from("Bus"),
        ..car
    };
    println!("{}", bus.get_name());

    bus.add_fuel(10.0);
    println!("Bus' fuel is {}.", bus.fuel);

    let ship = Shuttle::new("Ship");
    println!("{}", ship.get_name());

    let red = Color(255, 0, 0);
    println!("{}", get_red_value(&red));


    let mut rect = Rectangle::new(10.0, 20.0);
    assert_eq!(rect.get_area(), 200.0);
    rect.scale(2.0);
    assert_eq!(rect.get_area(), 800.0);
}
