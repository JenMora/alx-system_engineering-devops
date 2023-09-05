#!/usr/bin/env ruby

#puts ARGV[0].scan(/hbt{2,5}n/).join

input_string = ARGV[0]
result = input_string.scan(/hbt{2,5}n/).join
puts result

