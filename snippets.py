#!/usr/bin/python2.7
from __future__ import print_function


def calc_idx_v_perturb(key, n):
    i = hash(key) % n
    yield i
    perturb = hash(key)
    while True:
        i = (5 * i + perturb + 1) % n
        print("Perturb is", perturb)
        perturb >>= 5
        yield i


def calc_idx(key, n):
    i = hash(key) % n
    yield i
    while True:
        i = (5 * i + 1) % n
        yield i


def calc_hash_mod(key, n):
    return hash(key) % n
