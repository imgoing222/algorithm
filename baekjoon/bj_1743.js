"strict mode";
const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

dx = [-1, 0, 1, 0];
dy = [0, 1, 0, -1];

function dfs(x, y) {
	visited[x][y] = 1;
	temp += 1;

	for (let i = 0; i < 4; i++) {
		const nx = x + dx[i];
		const ny = y + dy[i];

		if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
		if (visited[nx][ny]) continue;

		if (board[nx][ny]) {
			dfs(nx, ny);
		}
	}
}

let [N, M, K] = input().split(" ").map(Number);
let board = Array.from(Array(N), () => Array(M).fill(0));
let visited = Array.from(Array(N), () => Array(M).fill(0));
let ans = 0;

for (let i = 0; i < K; i++) {
	let [r, c] = input().split(" ").map(Number);
	board[r - 1][c - 1] = 1;
}

let temp;
for (let i = 0; i < N; i++) {
	for (let j = 0; j < M; j++) {
		if (board[i][j] === 1 && !visited[i][j]) {
			temp = 0;
			dfs(i, j);
			if (temp > ans) ans = temp;
		}
	}
}

console.log(ans);
