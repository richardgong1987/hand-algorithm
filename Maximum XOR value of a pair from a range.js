/**
 * https://www.geeksforgeeks.org/value-in-a-given-range-with-maximum-xor/
 * 
 * For two positive integers, lo and hi, and a limit k, find two integers, a and b, satisfying the following criteria. Return the value of a b. The symbol denotes the bitwise XOR operator. lo a < b hi The value of a b is maximal for a b k.
 *
 * Input from stdin will be processed as follows and passed to the function. The first line contains an integer, lo, the lower range limit. The second line contains an integer, hi, the upper range limit. The third line contains an integer, k, the maximal limit.
 *
 * Example lo = 3 hi = 5 k = 6: a b a b 3 4 7 3 5 6 4 5 1
 * The maximal useable XORed value is 6 because it is the maximal value that is less than or equal to the limit k = 6.
 *
 *
 */

function maximumXOR(l, r, n) {
    let x = 0;
    for (let i = parseInt(Math.log(r) / Math.log(2)); i >= 0; --i) {
        if (n & (1 << i))  // Set bit
        {
            if (x + (1 << i) - 1 < l) x ^= (1 << i);
        } else // Unset bit
        {
            if ((x ^ (1 << i)) <= r) x ^= (1 << i);
        }
    }
    return n ^ x;
}

console.log(maximumXOR(3, 5, 6));
// let n = 7, l = 2, r = 23;