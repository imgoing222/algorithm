"strict mode";

const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

const N = Number(input());

const topBottomPair = { 0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0 };

let answer = 0;

let dices = [];

for (let i = 0; i < N; i++) {
	dices.push(input().split(" ").map(Number));
}

// 옆면 중 가장 큰 수 찾기
function getLargestNumber(idx1, idx2, numbers) {
	let largestNumber = 0;
	for (let i = 0; i < 6; i++) {
		if (i === idx1 || i === idx2) continue;
		largestNumber = Math.max(largestNumber, numbers[i]);
	}

	return largestNumber;
}

// 1번 주사위의 top 모든 경우
for (let topIdx = 0; topIdx < 6; topIdx++) {
	const [firstDice, ..._] = dices;
	const bottomIdx = topBottomPair[topIdx];
	const largestNumber = getLargestNumber(topIdx, bottomIdx, firstDice);
	stackDice(firstDice[topIdx], 1, largestNumber);
}

// 2번 부터 쌓기
function stackDice(bottom, depth, total) {
	if (depth === N) {
		answer = Math.max(answer, total);
		return;
	} else {
		const nthDice = dices[depth];
		const bottomIdx = nthDice.indexOf(bottom);
		const topIdx = topBottomPair[bottomIdx];
		const largestNumber = getLargestNumber(topIdx, bottomIdx, nthDice);
		stackDice(nthDice[topIdx], depth + 1, total + largestNumber);
	}
}

console.log(answer);
