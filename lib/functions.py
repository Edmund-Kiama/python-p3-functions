#!/usr/bin/env python3

def greet_programmer() -> None:
    print("Hello, programmer!")


def greet(name) ->None:
    print(f'Hello, {name}!')

def greet_with_default(name="programmer")->None:
    print(f"Hello, {name}!")

def add(num1, num2)->int:
    return num1 + num2

def halve(number):
    return number / 2
