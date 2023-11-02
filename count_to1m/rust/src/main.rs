fn main() {
    use std::time::Instant;

    let start_time = Instant::now();

    for i in 1..=1_000_000 {
        println!("{}", i);
    }

    let duration = start_time.elapsed();

    println!("Time elapsed in expensive_function() is: {:?}", duration);
}
