// String Challenge
// Have the function
// stringChallenge (str) lead the str
// parameter being passed which will be a string of HTML DOM elements and plain text. The elements that will be used are: b. i. em.
//   div, p. For example: if str is «div>b> <p>hello world /p></b>/div»" then this string ot DOM elements is nested correctlv so vour
// program should return the string true
// (alv›(alv››b›</alv›/D>
// console. log(Stringchallenge (readfine(›»;
// If a string is not nested correctly, return the
// first element encountered where. if changed
// into a ditterent element. would result in a
// properl formatted string. It the string is not
// formatted properly, then it will only be one element that needs to be changed. For
// examble: if str is "<div>
// <i>hello‹/i>world</b>" then vour proaram
// should return the string div because if the
//   first ‹div> element were changed into a ‹b›
// the string would be properly formatted.

// Example:
// Input: "<div><b></b></div><p></p><div></div>"
// Output: div


function stringChallenge(str) {
  let stack = [];
  let elements = ["b", "i", "em", "div", "p"];
  let idx = 0;
  //"</div></p>"
  while (idx < str.length) {
    if (str[idx] === "<") {

      if (str[idx + 1] === "/") { // Closing tag
        let tagEndIdx = str.indexOf(">", idx);
        let tag = str.slice(idx + 2, tagEndIdx);
        if (!stack.length || stack.pop() !== tag) {
          return tag;
        }
        idx = tagEndIdx + 1;
      } else { // Opening tag
        let tagEndIdx = str.indexOf(">", idx);
        let tag = str.slice(idx + 1, tagEndIdx);
        if (elements.includes(tag)) {
          stack.push(tag);
        }
        idx = tagEndIdx + 1;
      }
    } else {
      idx++;
    }
  }

  if (!stack.length) {
    return "true";
  }
  return stack[0];

}

console.log(stringChallenge("<div></div><b></b></div></p>")); // Should return "div"


