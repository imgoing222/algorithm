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

let tc = 1;

while (true) {
	let cnt = 0;
	function dfs(x, y, depth, sum) {
		visited[x][y] = 1;
		if (depth === 4) {
			if (sum > maxValue) maxValue = sum;
			cnt += 1;
			return;
		}

		for (let i = 0; i < 4; i++) {
			const nx = x + dx[i];
			const ny = y + dy[i];

			if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
			if (visited[nx][ny]) continue;

			dfs(nx, ny, depth + 1, sum + board[nx][ny]);
			visited[nx][ny] = 0;
		}
	}

	function calculate2(x, y) {
		const directions = [
			[0, 1, 2],
			[0, 1, 3],
			[0, 2, 3],
			[1, 2, 3],
		];

		for (const direction of directions) {
			let total = board[x][y];
			for (let i = 0; i < 3; i++) {
				const nx = x + dx[direction[i]];
				const ny = y + dy[direction[i]];
				if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
				cnt += 1;
				total += board[nx][ny];
			}
			if (total > maxValue) maxValue = total;
		}
	}

	const N = Number(input());
	if (N === 0) break;
	const board = [...Array(N)].map(() => input().trim().split(/ +/).map(Number));

	const visited = Array.from(Array(N), () => Array(N).fill(0));

	let maxValue = 0;

	for (let i = 0; i < N; i++) {
		for (let j = 0; j < N; j++) {
			dfs(i, j, 1, board[i][j]);
			// ㅗ ㅏ ㅜ ㅓ
			calculate2(i, j);
		}
	}

	console.log(`${tc}. ${maxValue}`);
	tc += 1;
}
