var friends = ["a", "b", "c"]
var gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]

var giftLog = {}
var giftIndex = {}
var getGift = {}

// 배열 제작
friends.forEach((element) => {
    giftLog[element] = new Object()
    giftIndex[element] = 0
    getGift[element] = 0
})
for (const outKey in giftLog) {
    for (const innerKey in giftLog) {
        giftLog[outKey][innerKey] = 0
    }
}

// 값 배열에 입력
gifts.forEach((element) => {
    const log = element.split(" ")
    giftLog[log[0]][log[1]] += 1
    giftIndex[log[0]] += 1
    giftIndex[log[1]] -= 1
})

// 비교
for (const outKey in giftLog) {
    for (const innerKey in giftLog) {
        if (giftLog[outKey][innerKey] >= 0) {
            if (giftLog[outKey][innerKey] > giftLog[innerKey][outKey]) {
                getGift[outKey] += 1
            } else if (giftLog[outKey][innerKey] == giftLog[innerKey][outKey]) {
                if (giftIndex[outKey] > giftIndex[innerKey]) {
                    getGift[outKey] += 1
                }
            }
        }
    }
}

// 최대값 찾기
var max = 0
for (const key in getGift) {
    if (getGift[key] > max) {
        max = getGift[key]
    }
}

console.log(max)