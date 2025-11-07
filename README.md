# Rapid Redis

**Rapid Redis** is a lightweight, educational in-memory cache library inspired by Redis.
It is built entirely in Python for learning purposes and designed to be simple, minimal, and easy to extend.

---

## Overview

Rapid Redis provides a basic Redis-like interface for storing and managing cached data using Python dictionaries under the hood.
It currently supports five common data structures and exposes simple, intuitive methods for cache operations.

---

## Features

* In-memory key-value cache using Python dictionaries
* Basic operations: `set`, `get`, `delete`, and `clear`
* Supports multiple data structures:

  * Strings
  * Lists
  * Sets
  * Hashes
* Easy to use and lightweight — ideal for understanding Redis fundamentals

---

## Installation

You can install Rapid Redis using 

```bash
pip install rapid-redis
```

---

## Usage

```python
from rapid_redis import RapidCache
from rapid_redis.datastructures import strings, lists, sets, hash

cache = RapidCache()

# Basic cache operations
cache.set("name", "Atharsh")
print(cache.get("name"))  # Output: Atharsh
cache.delete("name")
cache.clear()  # Clear all data

# String operations
strings.set_string(cache, "username", "Atharsh")
print(strings.get_string(cache, "username"))  # Output: Atharsh

# List operations
lists.lpush(cache, "mylist", 1, 2, 3)
print(cache.get("mylist"))  # Output: [3, 2, 1]
lists.rpush(cache, "mylist", 4)
print(lists.lpop(cache, "mylist"))  # Output: 3

# Set operations
sets.sadd(cache, "myset", "a", "b", "c")
print(sets.smembers(cache, "myset"))  # Output: {'a', 'b', 'c'}

# Hash operations
hash.hset(cache, "user:1", "name", "Atharsh")
hash.hset(cache, "user:1", "age", 25)
print(hash.hget(cache, "user:1", "name"))  # Output: Atharsh
```

---

## Roadmap

Planned features for upcoming releases include:

* Sorted Sets data structure support
* TTL (Time-to-Live) support for expiring keys
* Additional cache methods (`exists`, `flush`, etc.)
* Persistent cache storage (saving data to disk)
* Thread-safe operations
* Command-line interface for quick cache access
* Optional lightweight server mode for experimentation
* Concurrency for multiple user handling

---

## Contributing

Rapid Redis is an open project — contributions are welcome.
If you’d like to improve functionality, add features, or clean up code, feel free to fork the repository and open a pull request.

---

## License

This project is released under the MIT License.


