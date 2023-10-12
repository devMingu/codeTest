function solution(a, b, n) {
  var answer = 0;
  let new_coke = 0;
  let available_coke = parseInt(n / a);

  while (available_coke) {
    new_coke = available_coke * b;
    answer += new_coke;
    n = new_coke + (n % a);

    available_coke = parseInt(n / a);
  }

  return answer;
}
