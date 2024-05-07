const keymap = ["ABACD", "BCEFD"]
const targets = ["DG"]

// 모든 알파벳에 대한 최적의 keymap 파악
let bestKeymap = {}
for (let i of "ABCDEFGHIJKLMNOPQRSTUVWXYZ") {
    bestKeymap[i] = -1
}

for (let i of "ABCDEFGHIJKLMNOPQRSTUVWXYZ") {
    for (let j of keymap) {
        if (j.indexOf(i) != -1) {
            bestKeymap[i] == -1 ? bestKeymap[i] = j.indexOf(i) : bestKeymap[i] > j.indexOf(i) ? bestKeymap[i] = j.indexOf(i) : bestKeymap[i]
        }
    }
}

// 목표 문자열 제작
let answer = new Array(targets.length).fill(0)
targets.forEach((target, i) => {
    for (let word of target) {
        if (bestKeymap[word] != -1) {
            answer[i] += bestKeymap[word] + 1
        } else {
            answer[i] = -1
            break
        }
    }
});


console.log(answer)