#!/usr/bin/env ruby
puts ARGV[0].scan(/hb?tn/).join

#The regular expression /hb?tn/ matches the string "htn" or "hbtn".
#+ The ? character is called the optional quantifier. It tells the regular
#+ expression engine that the preceding character can be present or absent.
