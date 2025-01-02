function solution(bandage, health, attacks) {
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
}