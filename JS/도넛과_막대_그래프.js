edges = [[2, 3], [4, 3], [1, 1], [2, 1]];

// 몇 번 가리켰는지와 몇 번 가리켜졌는지에 대한 배열 제작
var point = new Array(edges.length).fill(0);
var pointed = new Array(edges.length).fill(0);
edges.forEach(element => {
    point[element[0] - 1] += 1
    pointed[element[1] - 1] += 1
});

// 무관한 정점 구하기
var maxPoint = Math.max(...point)   // ... 전개 연산자
for (let i=0;i<edges.length;i++) {
    if (pointed[i] == 0 && point[i] == maxPoint) {
        var unrelatedPoint = i;
        break
    }
}

console.log(point);
console.log(pointed);
console.log(unrelatedPoint);