#!/usr/bin/perl

#Generates prime numbers from 2 to 1,000,000 using Eratosthenes’ prime number sieve. Why? Why not.

use CGI qw(:standard -nph);

#prints out NPH allowing the script to output as it generates and prevents 30 sec timeout
use CGI qw(:standard -nph);
print "Content-type: text/plain\n\n";
$| = 1;

print "<title>Prime Number Generator</title>\n";

$tt = time();

$limit = 1000000 ;
$limitSqrt = int(sqrt($limit));

print "Prime Numbers up to $limit<p>\n\n";

# $notprime{$num} = undef $num is prime
# $notprime{$num} = 1 $num is not prime

#calculate and print primes up to sqrt($limit)
#we are actually generating a list of non primes by adding each number (up to sqrt($limit) ) repeatedly until we reach $limit.
#all sums will not be prime
for($num=2; $num <= $limitSqrt; ++$num)
     {
      $sum = $num;

      if ($notprime{$num})
         { #this number is not a prime so it's factors's multiples have already been checked off
         next;
         }
      else
         { #this number has not yet been marked 'not prime' so it must be prime as we have already checked for all possible lesser factors
         print "$num\n"
         }
      while ($sum < $limit) #add $num repeatedly up to limit. all sums will not be prime. same as all multiples of $num
             {
             $sum = $sum + $num;
             $notprime{$sum} = 1; #not prime
             }
     }

#all non primes have been found up to $limit at this point.

#print already calculated primes after sqrt($limit)
for($num=$limitSqrt + 1; $num < $limit; ++$num)
     {
     if (!$notprime{$num})
         {
         print "$num\n"
         }
     }

print "<p><p>\n\nSeconds: " ;
print time() - $tt;
print "\n\n" ;



1;