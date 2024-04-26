let name = ["may", "kein", "kain", "radi"]
let yearning = [5, 10, 1, 3]
let photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

let missVal = new Object()
let answer = new Array(photo.length).fill(0)

for (let i=0;i<name.length;i++) {
    missVal[name[i]] = yearning[i]
}

for (let i=0;i<photo.length;i++) {
    photo[i].forEach(person => {
        missVal[person] != undefined ? answer[i] += missVal[person] : answer[i]
    });
}

console.log(answer);