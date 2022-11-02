"strict mode";

const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "dev/stdin" : "input.txt")
  .toString()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

function rollTheDice(dir) {
  let tmpDice = [...dice];
  let rdir = dir % 2 ? dir + 1 : dir - 1;

  const [top, bottom, id, ird] = [dice[0], dice[5], dice[dir], dice[rdir]];

  tmpDice[0] = ird;
  tmpDice[5] = id;
  tmpDice[dir] = top;
  tmpDice[rdir] = bottom;

  dice = [...tmpDice];
}

function updateCurrentPosition(x, y, order) {
  const d = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
  ];

  const nx = x + d[order - 1][0];
  const ny = y + d[order - 1][1];

  if (nx < 0 || nx >= N || ny < 0 || ny >= M) return "out";

  currentX = nx;
  currentY = ny;
}

const [N, M, X, Y, _] = input().split(" ").map(Number);

let board = [];
for (let i = 0; i < N; i++) {
  board.push(input().split(" ").map(Number));
}

const movingOrders = input().split(" ").map(Number);

let [currentX, currentY] = [X, Y];
let dice = [0, 0, 0, 0, 0, 0];

for (const order of movingOrders) {
  // 1. 주사위 위치 구하기 (벗어난다면 pass)
  if (updateCurrentPosition(currentX, currentY, order) === "out") continue;
  // 2. 주사위 굴려서 dice 업데이트
  rollTheDice(order);
  // 3. 주사위의 top 출력
  console.log(dice[0]);

  // 4. 주사위 바닥과 칸 비교 후 로직 실행
  if (board[currentX][currentY]) {
    dice[5] = board[currentX][currentY];
    board[currentX][currentY] = 0;
  } else {
    board[currentX][currentY] = dice[5];
  }
}
