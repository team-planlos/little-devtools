// Tempfile module
use std::env;

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

        match hash_date {
            Some(h) => {
                if h {
                    self.hash_date()
                } else {
                    self.hash_rand()
                }
            },
            None => {self.hash_date()},
        }

        let self = Tempfile {
            hash_name: hash_name,
            path: path,
        };
    }

    pub fn hash_date(&self) {
        todo!()
    }

    pub fn hash_rand(&self) {
        todo!()
    }
}