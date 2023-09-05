#!/usr/bin/env ruby 

input_string = ARGV[0]
matches = input_string.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
result = matches.join(',')
puts result

#ARGV[0] is the first argument passed to the script.
#scan() is a method that matches a regular expression pattern to a string.
#\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\] is a regular expression
#+ pattern that matches a log line that has three fields: the sender,
#+ the receiver, and the flags.
#.*? is a wildcard that matches any characters.
#from:, to:, and flags: are literal matches.
#(.*?) captures the contents of the field.
#join() is a method that joins a list of strings with a delimiter.
