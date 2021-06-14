# aviation-alphabet
Have you ever been on a phonecall and needed to spell out something but the person on the other side didn't understand you? Well, the aviation industry has had
the same problems and created a phonetic alphabet.

## How does the alphabet work?
It has 26 words, every word starts with each letter of the alphabet (Alfa, ..., Zulu). During a phonecall it may be hard to remember the words, so I made this
script that gets them for you.

## How do I use it?
It's easy, you just run it, add the desired string as an argument, quotes are optional.

Input:
```bash
$ ./aviation-alphabet "Hello world"
```
Output:
```bash
Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta
```
Or, you can input the string without quotes, the script takes care of it:

Input:
```bash
$ ./aviation-alphabet Hello world
```
Output:
```bash
Hotel Echo Lima Lima Oscar Whiskey Oscar Romeo Lima Delta
```
