My first solution to 9-2 was very silly and can be found [here](https://github.com/gerrowadat/adventofcode/commit/bb425ebb1b5fe9957c339cc846415e2567293b76#diff-8035e16ddc9f60faa9daf28b0ababe8b82bc496a82a7297422dc9fe275b38dea).

My 2 mistakes were

 - Assuming the input was ordered (I eyeballed even the example input). I saw numbers getting 'longer' and assumed. Doh.
 - Trying to over-optimise - this code will never be re-used (I hope) and stepping back through the file from the target number wasn't necessary, even.
