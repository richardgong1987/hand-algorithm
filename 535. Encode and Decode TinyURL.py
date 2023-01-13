import random
import string
from collections import defaultdict


class Codec:
    _urlMapCode, _codeMapUrl = defaultdict(), defaultdict()
    _chars = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        # first step
        if longUrl in self._urlMapCode:
            return self._urlMapCode[longUrl]

        code = self._generateUrlWithRandomCode()

        while code in self._codeMapUrl:
            code = self._generateUrlWithRandomCode()

        self._codeMapUrl[code] = longUrl

        self._urlMapCode[longUrl] = code

        return code

    def decode(self, code: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self._codeMapUrl[code]

    def _generateUrlWithRandomCode(self):
        array_str = [random.choice(self._chars) for _ in range(6)]
        return 'http://tinyurl.com/' + ''.join(array_str)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

codec = Codec()
code = codec.encode('https://leetcode.com/problems/design-tinyurl')
decode = codec.decode(code)
print(code, decode)
