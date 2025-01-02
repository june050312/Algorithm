function solution(name, yearning, photo) {
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
    return answer;
}