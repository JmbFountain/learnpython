#!/usr/bin/env python3
i = 0
words = {3: "fizz", 5: "buzz"}
while i <= 100:
    output = ''
    for word in words:
        if i % word == 1:
            output = output + words.get(word)
    if output == '':
        output = i
    print(output)
    i = i + 1
