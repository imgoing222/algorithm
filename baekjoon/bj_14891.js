"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

let gears = [];
for (let i = 0; i < 4; i++) {
	gears.push(input().trim().split("").map(Number));
}

const N = Number(input());
for (let j = 0; j < N; j++) {
	const [num, dir] = input().trim().split(" ").map(Number);
	checkDirection(num - 1, dir, 0);
}

function checkDirection(n, d, movingDir) {
	// 좌
	if (n > 0 && movingDir !== 1) {
		if (gears[n][6] !== gears[n - 1][2]) {
			checkDirection(n - 1, d * -1, -1);
		}
	}
	// 우
	if (n < 3 && movingDir !== -1) {
		if (gears[n][2] !== gears[n + 1][6]) {
			checkDirection(n + 1, d * -1, 1);
		}
	}
	rotate(n, d);
}

function rotate(n, d) {
	if (d === 1) {
		const tmp = gears[n].pop();
		gears[n].unshift(tmp);
	} else {
		const tmp = gears[n].shift();
		gears[n].push(tmp);
	}
}

let ans = 0;
for (let k = 0; k < 4; k++) {
	ans += gears[k][0] * 2 ** k;
}

console.log(ans);
