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

function dfs(x, y, color) {
	visited[x][y] = 1;

	for (let i = 0; i < 4; i++) {
		const nx = x + dx[i];
		const ny = y + dy[i];

		if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
		if (visited[nx][ny]) continue;
		if (board[nx][ny] !== color) continue;
		dfs(nx, ny, board[nx][ny]);
	}
}

const N = Number(input());

// 일반인 그림
let board = [];
for (i = 0; i < N; i++) {
	board.push(input().trim().split(""));
}

let visited = Array.from(Array(N), () => Array(N).fill(0));
let normalCnt = 0;
for (i = 0; i < N; i++) {
	for (j = 0; j < N; j++) {
		if (!visited[i][j]) {
			dfs(i, j, board[i][j], "normal");
			normalCnt += 1;
		}
	}
}

// 적록색약 그림
board = board.map((x) => x.map((color) => color.replace("G", "R")));
visited = Array.from(Array(N), () => Array(N).fill(0));
let cnt = 0;
for (i = 0; i < N; i++) {
	for (j = 0; j < N; j++) {
		if (!visited[i][j]) {
			dfs(i, j, board[i][j]);
			cnt += 1;
		}
	}
}
console.log(normalCnt, cnt);
