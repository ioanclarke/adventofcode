let requestURL = 'https://adventofcode.com/2020/leaderboard/private/view/1039209.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();
request.onload = function() {
  const response = request.response;
  console.log(response)
}
