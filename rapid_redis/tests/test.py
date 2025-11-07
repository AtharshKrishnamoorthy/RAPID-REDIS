"""
Simple test script for rapid_redis
"""

import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from rapid_redis import RapidCache
from rapid_redis.datastructures import strings, lists, hash, sets


def test_cache_basic():
    
    print("Testing basic cache operations...")
    cache = RapidCache()
    
   
    cache.set("key1", "value1")
    assert cache.get("key1") == "value1", "Failed: set/get operation"
    
   
    cache.delete("key1")
    assert cache.get("key1") is None, "Failed: delete operation"
    
    
    cache.set("key2", "value2")
    cache.set("key3", "value3")
    cache.clear()
    assert cache.get("key2") is None, "Failed: clear operation"
    
    print("✓ Basic cache tests passed!")


def test_strings():
    
    print("\nTesting string operations...")
    cache = RapidCache()
    
    
    strings.set_string(cache, "str_key", "hello")
    assert strings.get_string(cache, "str_key") == "hello", "Failed: string set/get"
    
    
    strings.set_string(cache, "num_key", 123)
    assert strings.get_string(cache, "num_key") == "123", "Failed: number to string conversion"
    
    print("✓ String tests passed!")


def test_lists():
    
    print("\nTesting list operations...")
    cache = RapidCache()
    
    
    lists.lpush(cache, "mylist", "a")
    lists.lpush(cache, "mylist", "b", "c")
    assert cache.get("mylist") == ["c", "b", "a"], "Failed: lpush operation"
    
    
    cache.clear()
    lists.rpush(cache, "mylist", "x")
    lists.rpush(cache, "mylist", "y", "z")
    assert cache.get("mylist") == ["x", "y", "z"], "Failed: rpush operation"
    
   
    value = lists.lpop(cache, "mylist")
    assert value == "x", "Failed: lpop operation"
    assert cache.get("mylist") == ["y", "z"], "Failed: lpop list state"
    
    print("✓ List tests passed!")


def test_hash():
   
    print("\nTesting hash operations...")
    cache = RapidCache()
    

    hash.hset(cache, "user:1", "name", "John")
    hash.hset(cache, "user:1", "age", 30)
    
    assert hash.hget(cache, "user:1", "name") == "John", "Failed: hash set/get name"
    assert hash.hget(cache, "user:1", "age") == 30, "Failed: hash set/get age"
    
 
    assert hash.hget(cache, "user:1", "email") is None, "Failed: hash get non-existent field"
    
    print("✓ Hash tests passed!")


def test_sets():
 
    print("\nTesting set operations...")
    cache = RapidCache()
    

    sets.sadd(cache, "myset", "a", "b", "c")
    members = sets.smembers(cache, "myset")
    
    assert "a" in members, "Failed: set add 'a'"
    assert "b" in members, "Failed: set add 'b'"
    assert "c" in members, "Failed: set add 'c'"
    assert len(members) == 3, "Failed: set size"
    
   
    sets.sadd(cache, "myset", "a")
    members = sets.smembers(cache, "myset")
    assert len(members) == 3, "Failed: set duplicate handling"
    
    print("✓ Set tests passed!")


def run_all_tests():
   
  
    print("RAPID_REDIS TEST ")
   
    
    try:
        test_cache_basic()
        test_strings()
        test_lists()
        test_hash()
        test_sets()
        
   
        print("ALL TESTS PASSED! ✓")
   
        
    except AssertionError as e:
        print("TEST FAILED")
        return False
    except Exception as e:
        print("ERROR")
        return False
    
    return True


if __name__ == "__main__":
    run_all_tests()
