"strict mode";
const fs = require("fs");
// const stdin = fs.readFileSync("/dev/stdin").toString().split("\n");
const stdin = `3 3
1000000000
1000000000
1000000000`.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

// 입력값 10억번 & 2초 => binary search

const [S, C] = input().split(" ").map(Number);
pas = [];
for (i = 0; i < S; i++) {
	pas.push(Number(input()));
}

let start = 1;
let end = 1000000000;

while (true) {
	let mid = Math.floor((start + end) / 2);

	if (end < start) {
		const totalPa = pas.reduce((a, b) => a + b, 0);
		const ans = totalPa - mid * C;
		console.log(ans);
		break;
	}

	let padak = 0;
	// 현재 중간값으로 파 나눴을 때 파닭 개수 구하기
	pas.forEach((pa) => (padak += Math.floor(pa / mid)));

	// 모자라다면 파 길이 감소, 많거나 같다면 파 길이 증가
	if (padak < C) end = mid - 1;
	else if (padak >= C) {
		start = mid + 1;
	}
}
