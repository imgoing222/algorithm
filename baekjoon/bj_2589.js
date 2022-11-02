"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

function bfs(x, y, d) {
	let visited = Array.from(Array(R), () => Array(C).fill(0));

	let queue = [];
	queue.push([x, y, d]);

	while (queue.length !== 0) {
		const [x, y, d] = queue.shift();
		visited[x][y] = d;

		for (let i = 0; i < 4; i++) {
			const nx = x + dx[i];
			const ny = y + dy[i];

			if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
			if (visited[nx][ny]) continue;
			if (board[nx][ny] === "W") continue;

			visited[nx][ny] = d + 1;
			queue.push([nx, ny, d + 1]);
		}
	}

	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			if (visited[i][j] > ans) ans = visited[i][j];
		}
	}
}

const [R, C] = input().split(" ").map(Number);
const board = [...Array(R)].map(() => input().trim().split(""));
let ans = 0;

for (let i = 0; i < R; i++) {
	for (let j = 0; j < C; j++) {
		if (board[i][j] === "L") bfs(i, j, 1);
	}
}

console.log(ans - 1);
