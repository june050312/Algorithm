// 조건
// 1. 체력이 최대일 때 더 이상 체력 안참
// 2. 붕대 감기 시전시간 동안 취소를 안 당하면 추가체력 회복이 있음(시전시간 마지막에 초 당 체력회복이랑 같이 들어감)
// 3. 공격을 당하면 붕대 감기가 취소됨
// 4. 공격을 당할 때는 체력 회복이 없음
// 5. 추가 회복이 있더라도 최대 체력 이상으로 회복 안됨

var bandage = [1, 1, 1];
var health = 5;
var attacks = [[1, 2], [3, 2]];

var maxHealth = health;
var attackCnt = 0;
var skillTick = 0;
for (let t = 1; t <= attacks[attacks.length - 1][0]; t++) {
    if (attacks[attackCnt][0] == t) {
        health -= attacks[attackCnt][1];
        attackCnt += 1;
        skillTick = 0;
    } else {
        if (skillTick == bandage[0]) {
            health += bandage[1];
            health += bandage[2];

            health >= maxHealth ? health = maxHealth : health
            skillTick = 0;
        } else if (health >= maxHealth) {
            health = maxHealth;
        } else {
            health += bandage[1];
        }
    }
    skillTick += 1;

    if (health <= 0) {
        return -1;
    }
}
return health
