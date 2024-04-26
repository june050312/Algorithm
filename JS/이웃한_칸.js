let board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
let h = 1
let w = 1

let curColor = board[h][w]
let cnt = 0

let arr = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for (let i=0;i<4;i++) {
    try {
        board[h + arr[i][0]][w + arr[i][1]] === curColor ? cnt++ : cnt;
    } catch (err) {
        continue;
    }
}

console.log(cnt);