use std::collections::HashMap;
use std::fs;

fn vector() {
    let mut names: Vec<String> = Vec::new();
    // add a name to the vector
    names.push("John".to_string());
    names.push("Jane".to_string());
    // get the first name
    let first_name = names.get(0);
    println!("First name: {:?}", first_name);
    // pop the last name
    let last_name = names.pop();
    println!("Last name: {:?}", last_name);
    // create a vector of numbers
    let countdowns = vec![1, 2, 3, 4, 5];
    println!("Countdown: {:?}", countdowns);
}

fn hash_map() {
    let mut scores: HashMap<String, u32> = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    // get the score for a team
    let team_score = scores.get(&String::from("Blue"));
    println!("Team score: {:?}", team_score);
    // update the score for a team
    scores.insert(String::from("Blue"), 25);
    // add a new team
    scores.entry(String::from("Green")).or_insert(50);
    // modify the score for a team
    let blue_team_score = scores.entry(String::from("Blue")).or_insert(0);
    *blue_team_score += 10;
    // remove the score for a team
    scores.remove(&String::from("Yellow"));
    println!("Scores: {:?}", scores);
}

fn most_popular_word() -> (Vec<String>, u32) {
    let content = match fs::read_to_string("earth_to_the_moon.txt") {
        Ok(content) => content.to_lowercase(),
        Err(error) => panic!("Error reading file: {}", error),
    };
    let words = content.split_whitespace().collect::<Vec<&str>>();

    let mut word_counts = HashMap::new();
    for word in words {
        let count = word_counts.entry(word).or_insert(0);
        *count += 1;
    }

    let mut most_popular_words: Vec<String> = Vec::new();
    let mut most_popular_count: u32 = 0;
    for (word, count) in word_counts {
        if count > most_popular_count {
            most_popular_words.clear();
            most_popular_words.push(word.to_string());
            most_popular_count = count;
        } else if count == most_popular_count {
            most_popular_words.push(word.to_string());
        }
    }
    (most_popular_words, most_popular_count)
}

fn main() {
    vector();
    hash_map();
    
    let (most_popular_words, most_popular_count) = most_popular_word();
    println!(
        "Most popular words: {:?} \nCount is {}.",
        most_popular_words, most_popular_count
    );
}
