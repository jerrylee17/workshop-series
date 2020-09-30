# Regular Expressions

Regular expressions are used often in string matching. It can be used for 
validation or get certain pieces of the text.

We will be using [regexr](https://regexr.com/) to visualize regex

Topics to be covered
1. Things you can do with regular expressions
1. Basic syntax of regular expressions
1. Phone number exercise
1. Use regex with javascript

## Things you can do with regex

Here are a few things that you can do with regex
- String matching (validation)
- Find occurences
- Find and replaces
- Search through text quickly and return subsets of the string

## Basic syntax

Regular expressions are defined in the following format:
```
/{expression}/{flag}
```

First, copy this onto the text. We will be selecting class
names as a demo.
```
cmpe50
cmpe102
cmpe110
cmpe124
cmpe125
cmpe126
cmpe127
cmpe131
cmpe142
cmpe146
cmpe152
cs46
cs47
cs146
cs149
cs151
```

### Flags

Flags are placed after the second "/" and define the behavior of the 
regular expression.

The two most commonly used flags are *g* and *i*.
- Global(*g*): match anywhere in the string
- Case insensitive(*i*)

### Placeholders
This is essentially a wildcard, which matches a character
- *.* : Matches any characters not a newline
- *\w* : word
- *\d* : digit
- *\s* : whitespace
- *[abc]* : a, b, or c. You can also use boolean
operators (^abc - not a, b, or c) or define a range (a-z - a to z)

When the placeholders `\w`, `\d`, `\s` are capitalized, it selects 
the opposite of what would be selected. 

### Quantifiers
These come after a character and define how many of the preceding
characters we want to match
- *a\** : 0 or more
- *a+* : 1 or more
- *a?* : 0 or 1
- *a{5}* : Exactly 5 a's
- *a{5,}* : 5 or more a's

### Groups

Characters can be grouped with the parenthesis. For example, 
`(cmpe)` selects anything that matches `cmpe`. They can be used
in conjunction with boolean operators. For example, `(cmpe)|(cs)`
will select any `cmpe` or `cs` in the string. By default, groups
will be captured together (see exec()). To prevent the capturing
of a group, use `(?:cmpe)`. You will see why this is useful later.


### Match beginning/end
The `^` symbol matches the beginning of the line. 

The `$` symbol matches the end of the line.

### Lookaround
Lookaround allows you to select substrings based on what is around them.

#### Positive lookbehind: `(?<=cmpe)`
This means that whatever goes before the parenthesis needs to be
after `cmpe`.

For example, running `(?<=cmpe)\d+` on `cmpe126` will return `126`. This 
is because `cmpe126` starts with a `cmpe`, which satisfies the lookbehind,
so the digits after `cmpe` are selected and returned.

#### Negative lookbehind: `(?<!cmpe)`
This selects whatever goes after the parenthesis cannot come after `cmpe`

Try this out on regexr!

#### Positive lookahead: `(?=cmpe)`
This means whatever goes after the parenthesis must be `cmpe`.

For example, running `\w+(?=124)` on `cmpe124` will return `cmpe`. The
logic is similar to the positive lookbehind.

## Phone Number Exercise
Create a regular expression to test phone numbers in the following formats:
- 1234567890
- 123-456-7890
- 123 456 7890
- (123) 456-7890
- +1 123-456-7890

<details>
<summary> Answer </summary>
Regex:

```
/(\+?1[ -]?)?\(?(\d{3})\)?[ -]?(\d{3})[ -]?(\d{4})/g
```

</details> <br />

## Using regex with javascript

We have just learned how to use regular expressions, but they are only 
useful if you know how to use it. We will be using 
[RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
to test and match strings.

First, create a RegExp object with the regular expression. 
```
const regex = RegExp(/((?:CMPE)|(?:CS))(\d+)/i);
```

To test if a string has anything that matches with the regular
expression, use test().
```
regex.test("CMPE126"); // should return true
regex.test("ISE130"); // should return false
```

To capture the groups in a string, use exec():
```
regex.exec("CMPE126"); // should return ["cmpe146", "cmpe", "146"]
```
