# Lecture 1: 5-Sept-2018

## To do
* install Rtools
* add python to PATH (install)

## Homework:
* http://swcarpentry.github.io/shell-novice/
* Complete computer setup

# Lecture 2:10-Sept-2018

## path navigation
* relative paths are better for coding because they are portable
* the "-" operator in path navigation is back to the LAST directory
* file names should never have spaces: use underscores, camel case, or dashes instead
* in CODE, dashes are interpreted as minus signs so they can not be used as variable names!

## Wildcards:
* "\*"" matches 0+ characters
* "?" matches exactly 1 character

## More on filenames:
* NO SPACES (to reiterate)
* no dots, no slashes
* file extensions: not really needed by the computer, for humans
	+ explicit tends to be better because it helps signify what format the 	  file was written in
	+ used by computer occasionally to pick the default application to open 	  the file in `open xxx.pdf` in mac will know to use a pdf viewer.

## Homework for next week:
* "pipes and filters" from the software carpentry intro

# Homework notes from "Pipes and Filters": 10-Sept-2018
<Pipes and Filters link>[http://swcarpentry.github.io/shell-novice/04-pipefilter/index.html]

* the ">" operator redirects output from the left into the file on the right.
* the "<" operator redirects input from a file on the right into a program on the left.
* `wc [file]` outputs the number of lines, words, and characters in a file
* `sort -n` sorts according to numeric value (default behavior is alphabetical)
* `head -n` also returns the 1st values according to numeric order
* the ">>" operator appends to an existing file instead of overwriting it (new line)
* the "|" operator (pipe) uses the output of the function on the left as the input for the function on the right.
* `uniq [files]` removes adjascent lines that are the same: `sort [file] | uniq` will remove all duplicates.
* `ls *[AB].txt` matches files that end in "A.txt" or "B.txt". This is important to remember!

# Homework notes from "Loops": 10-Sept-2018
<Loops link>[http://swcarpentry.github.io/shell-novice/05-loop/index.html]

## loop notation
```bash
for [variable] in [list]
do
  [action] $[variable]
done
```

# Lecture 3: 12-Sep-2018

Exercise 1 is the only part of HW1 that is due on Monday.

* when a command is continued, ctl+d signifies that you are "done" entering input:

```
$ wc -l
"this is a string of text"

q
[ctl+d]
```
output:

```
3
```
## More on redirection:


# Shell Scripting notes

* read variable from stdin with "$1", "$2", etc.:

```bash
#Example shell script to print the head and tail of a file
head -n "$2" "$1" | tail -n "$3"
```
* The special variable "$@" which sends all cmd-line argments to the script.

```bash
# Sort filenames by their length.
# Usage: bash sorted.sh one_or_more_filenames
wc -l "$@" | sort -n
```

```bash
bash sorted.sh *.pdb ../creatures/*.dat
```

The above execution of the sorted.sh uses all .pdb files in the current directory and all all .dat files in the creatures directory. cd

**There are HOMEWORK 1 hints in the topics for 12-Sep-2018**

# Lecture 4: finding things: 2018-Sep-17

I was absent from this class period.

## Note about quotes:

* single quotes ('') will not expand anything

* double quotes ("") will expand certain things like variables, certain escapes, and backticks

`$ echo ' the shell is $SHELL'`
```
the shell is $SHELL
```

`$ echo "the shell is $SHELL"`
```
the shell is /bin/bash
```

## Regular Expressions: “regexp”

We need lots of practice on this! For help: man re_format, get an explanation of your expression (and debug it) on regexp101 or debuggex

``` 	 
.	any one character
^	beginning of line (only if placed first)
$	end of line (only if placed last)
\	turns off special meaning of next symbol
[aBc]	anything in: a or B or c. Ranges: like [0-9], [a-z], [a-zA-Z]
[^aBc]	anything but: a, B, c
\w	any word character: letter, number, or “_”. also [[:alnum:]_]. opposite: \W
\d	any single digit. also [[:digit:]] or [0-9]. opposite: \D
\s	any white space character: single space, \t (tab), \n (life feed) or \r (carriage return). also [[:space:]]. opposite: \S
\b	word boundary (null string). also \< and \> for start/end boundaries. opposite: \B
+	one or more of the previous
?	zero or one of the previous
*	zero or more of the previous
{4}	4 of the previous
{4,6}	between 4 and 6 of the previous
{4,}	4 or more of the previous
```

### Finding the non-nucleotide

in the file:  ~/Documents/Stat679/bds-files/chapter-03-remedial-unix, to remove the non-sequence lines, we use `tail -n +[NUM]` to start from line number `NUM` and then we can pipe the output through grep and locate the line(s) containing non-nucleotide characters:

```bash
cd ~/Documents/Stat679/bds-files/chapter-03-remedial-unix
tail -n +2 tb1.fasta | grep -E [^ACGT]
```

# Lecture 5 2018-Sep-19

* when in `less`, the forward slash `/` allows you to search for text within the file.

* look into `xargs` and when it needs to be used.

- [ ]  makes checkable boxes as bullets

# Lecture 6 2018-Sep-24

## Git: All about tracking versions!

**! Use DESCRIPTIVE Commit Messages!**

For homework: **[Do this](http://cecileane.github.io/computingtools/pages/notes0929.html)**

# Lecture 7 2018-Sep-26
