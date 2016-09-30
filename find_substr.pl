#!/usr/bin/perl
use strict;
use warnings;

print "enter sequence: ";
my $string = <STDIN>;
chomp $string;
print "enter motif: ";
my $motif = <STDIN>;
chomp $motif;

my @matches;#=  $string =~ /(?=$motif)/g;

while ($string =~ /(?=$motif)/g){
    push (@matches, pos($string)+1);
}

print join (" ", @matches), "\n";

