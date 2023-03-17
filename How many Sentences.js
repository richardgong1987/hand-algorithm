/***
 * https://leetcode.com/discuss/interview-question/1541093/How-many-sentences-Can-someone-provide-a-python-solution-for-this-question
 *
 * How many Sentences problem:
 *
 * Given an array of words and an array of sentences, determine which words are anagrams of each other.
 * Calculate how many sentences can be created by replacing any word with one of its anagrams.
 * Example wordSet = ['listen', 'silent', 'it', 'is'] sentence = 'listen it is silent'
 * Determine that listen is an anagram of silent. Those two words can be replaced with their anagrams.
 * The four sentences that can be created are: listen it is silent listen it is listen silent it is silent silent it is listen
 *
 */

function countSentences(wordSet, sentences) {
    const anagrams = {};
    wordSet.forEach((word) => {
        const sorted = word.split('').sort().join('');
        if (!anagrams[sorted]) {
            anagrams[sorted] = [word];
        } else {
            anagrams[sorted].push(word);
        }
    });

    const results = [];
    sentences.forEach((sentence) => {
        const words = sentence.split(' ');
        let count = 1;
        words.forEach((word) => {
            const sorted = word.split('').sort().join('');
            if (anagrams[sorted]) {
                count *= anagrams[sorted].length;
            }
        });
        results.push(count);
    });

    return results;
}