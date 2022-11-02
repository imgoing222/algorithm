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

function bfs(x, y, sum) {
	const queue = [];
	let union = [[x, y]];

	queue.push([x, y]);
	visited[x][y] = 1;

	while (queue.length > 0) {
		const [x, y] = queue.pop();
		for (let i = 0; i < 4; i++) {
			const nx = x + dx[i];
			const ny = y + dy[i];

			if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
			if (visited[nx][ny]) continue;

			const populationDifference = Math.abs(land[nx][ny] - land[x][y]);

			if (populationDifference >= L && populationDifference <= R) {
				queue.push([nx, ny]);
				visited[nx][ny] = 1;
				union.push([nx, ny]);
				sum += land[nx][ny];
			}
		}
	}

	const population = Math.floor(sum / union.length);
	for (const [r, c] of union) {
		land[r][c] = population;
	}
}

const [N, L, R] = input().split(" ").map(Number);
let land = [];
for (let i = 0; i < N; i++) {
	let temp = input().split(" ").map(Number);
	land.push(temp);
}

let visited = Array.from(Array(N), () => Array(N).fill(0));
let day = 0;
let cnt = 0;

while (true) {
	day += 1;
	cnt = 0;
	visited = Array.from(Array(N), () => Array(N).fill(0));
	for (let i = 0; i < N; i++) {
		for (let j = 0; j < N; j++) {
			if (!visited[i][j]) {
				bfs(i, j, land[i][j]);
				cnt += 1;
			}
		}
	}
	if (cnt === N ** 2) {
		console.log(day - 1);
		break;
	}
}
