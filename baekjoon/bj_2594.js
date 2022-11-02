"strict mode";
const stdin = require("fs")
	.readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
	.toString()
	.split("\n");

const input = (() => {
	let line = 0;
	return () => stdin[line++];
})();

function getTime(str, type) {
	let t = Number(str.slice(0, 2));
	let m = Number(str.slice(2, 4));
	if (type === "start") {
		if (m < 10) {
			t -= 1;
			m += 50;
		} else {
			m -= 10;
		}
	} else {
		if (m >= 50) {
			t += 1;
			m -= 50;
		} else {
			m += 10;
		}
	}
	t = String(t);
	m = String(m);

	return m.length === 1 ? [t, `0${m}`] : [t, m];
}

function visitTimeline(st, sm, et, em) {
	const from = 60 * (Number(st) - 10) + Number(sm);
	const to = 60 * (Number(et) - 10) + Number(em);

	for (let j = from; j < to; j++) {
		timeline[j] = 1;
	}
}

function countTime() {
	let cnt = 0;
	let maxCnt = 0;
	for (const x of timeline) {
		if (x) {
			maxCnt = Math.max(cnt, maxCnt);
			cnt = 0;
		} else {
			cnt += 1;
		}
	}
	maxCnt = Math.max(cnt, maxCnt);
	return maxCnt;
}

const N = Number(input());
let timeline = Array(720).fill(0);

for (let i = 0; i < N; i++) {
	const [start, end] = input().split(" ");
	const [start_t, start_m] = getTime(start, "start");
	const [end_t, end_m] = getTime(end, "end");

	visitTimeline(start_t, start_m, end_t, end_m);
}

console.log(countTime());
