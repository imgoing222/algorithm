"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const [H, W] = input().split(" ").map(Number);
const walls = input().split(" ").map(Number);

const board = Array.from(Array(H), () => Array(W).fill(0));

for (let i = 0; i < W; i++) {
	for (let j = 0; j < walls[i]; j++) {
		board[j][i] = 1;
	}
}
let answer = 0;
for (let i = 0; i < H; i++) {
	let [flag, tmp] = [0, 0];
	for (let j = 0; j < W; j++) {
		if (board[i][j] === 1) {
			if (flag) {
				answer += tmp;
				tmp = 0;
			}
			flag = 1;
		} else {
			if (flag) tmp += 1;
		}
	}
}

console.log(answer);
