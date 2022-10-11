"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

function countCheese() {
	let tmpCheese = 0;

	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			if (board[i][j]) tmpCheese += 1;
		}
	}
	return tmpCheese;
}

function meltCheese(melting) {
	for (const [x, y] of melting) {
		board[x][y] = 0;
	}
}

function bfs(x, y) {
	let visited = Array.from(Array(R), () => Array(C).fill(0));

	let queue = [];
	queue.push([x, y]);
	visited[x][y] = 1;

	while (queue.length > 0) {
		const [x, y] = queue.shift();

		for (let i = 0; i < 4; i++) {
			nx = x + dx[i];
			ny = y + dy[i];

			if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
			if (visited[nx][ny]) continue;
			if (board[nx][ny]) melting.push([nx, ny]);
			else queue.push([nx, ny]);
			visited[nx][ny] = 1;
		}
	}
}

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];
const [R, C] = input().split(" ").map(Number);

let board = [];
for (let i = 0; i < R; i++) {
	board.push(input().split(" ").map(Number));
}

let cheesePiece;
let time = 0;
let melting = [];

while (true) {
	if (countCheese()) cheesePiece = countCheese();
	else break;
	bfs(0, 0);
	meltCheese(melting);
	time += 1;
}

console.log(time);
console.log(cheesePiece);
