"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

function expandWaterArea() {
	let waters = [];
	for (let i = 0; i < R; i++) {
		for (let j = 0; j < C; j++) {
			if (forest[i][j] === "*") waters.push([i, j]);
		}
	}

	// 수집한 물 좌표 순회하면서 4방향으로 확장
	// 돌이나 비버집, 영역 밖 제외
	for (const [i, j] of waters) {
		for (let k = 0; k < 4; k++) {
			nx = i + dx[k];
			ny = j + dy[k];

			if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
			if (forest[nx][ny] === "D" || forest[nx][ny] === "X") continue;

			forest[nx][ny] = "*";
		}
	}
}

function bfs(ix, iy) {
	let visited = Array.from(Array(R), () => Array(C).fill(0));
	let queue = [];
	queue.push([ix, iy, 0]);
	visited[ix][iy] = 1;
	let currentTime = -1;

	while (queue.length > 0) {
		const [x, y, time] = queue.shift();
		if (currentTime !== time) {
			currentTime = time;
			expandWaterArea();
		}

		for (let i = 0; i < 4; i++) {
			const nx = x + dx[i];
			const ny = y + dy[i];

			// 영역 밖 체크
			if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
			// visited 체크
			if (visited[nx][ny]) continue;
			// 비버 굴이면 return
			if (forest[nx][ny] === "D") return time + 1;
			// 돌이나 물 체크
			if (forest[nx][ny] === "X" || forest[nx][ny] === "*") continue;

			visited[nx][ny] = 1;
			queue.push([nx, ny, time + 1]);
		}
	}

	return "KAKTUS";
}

const [R, C] = input().split(" ").map(Number);
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];
let forest = [];
for (let i = 0; i < R; i++) {
	forest.push(input().trim().split(""));
}

// 고슴도치 찾기
for (let i = 0; i < R; i++) {
	for (let j = 0; j < C; j++) {
		if (forest[i][j] === "S") {
			const minTime = bfs(i, j);
			console.log(minTime);
		}
	}
}
