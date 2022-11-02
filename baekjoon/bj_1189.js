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

function dfs(x, y, depth) {
	if (x === 0 && y === C - 1) {
		if (depth === K) ans += 1;
	}

	for (let i = 0; i < 4; i++) {
		const nx = x + dx[i];
		const ny = y + dy[i];

		if (nx < 0 || ny < 0 || nx >= R || ny >= C) continue;
		if (board[nx][ny]) continue;

		board[nx][ny] = depth;
		dfs(nx, ny, depth + 1);
		board[nx][ny] = 0;
	}
}

const [R, C, K] = input().split(" ").map(Number);
const board = [];

let ans = 0;

for (let i = 0; i < R; i++) {
	board.push(
		input()
			.trim()
			.split("")
			.map((x) => {
				if (x === ".") return 0;
				else return x;
			})
	);
}

board[R - 1][0] = 1;
dfs(R - 1, 0, 1);

console.log(ans);
