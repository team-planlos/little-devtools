// Tempfile module
use std::env;
use std::fs::File;

pub struct Tempfile {
    hash_name: String,
    path: String,
}

impl Tempfile {
    pub fn new(path: Option<String>, hash_date: Option<bool>) -> Tempfile {
        let hash_name: String;
        let path: String;

        match path {
            Some(p) => {path=p.clone()},
            None => {path=env.current_dir()},
        }

        let self = Tempfile {
            hash_name: hash_name,
            path: path,
        };

        match hash_date {
            Some(h) => {
                if h {
                    hash_name = self.hash_date();
                } else {
                    hash_name = self.hash_rand();
                }
            },
            None => {hash_name = self.hash_date()},
        }
        File::create(format!("{}", self.hash_name))?;
    }

    pub fn hash_date(&self) -> str {
        use chrono::offset::Local;

        format!(chrono::offset::Local::now())
    }

    pub fn hash_rand(&self) -> str {
        use random::Source;
        let mut source = random::default(42);
    }
}