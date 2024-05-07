const cards1 = ["i", "water", "drink"]
const cards2 = ["want", "to"]
const goal = ["i", "want", "to", "drink", "water"]

let flag = 1
for (let word of goal) {
    if (cards1[0] == word) {
        cards1.shift()
    } else if (cards2[0] == word) {
        cards2.shift()
    } else {
        console.log("No")
        flag = 0
        break
    }
}
if (flag) console.log("Yes")