// https://adventofcode.com/2022/day/3


const fs = require('fs');

function parseData() {
    try {
        return fs.readFileSync('./day-03/input.txt', 'utf-8').split('\n');
    } catch (err) {
        console.error(err);
    }
}


function problemOne(rucksacks) {
    let total = 0;

    for (let rucksack of rucksacks) {
        let mid = Math.floor(rucksack.length / 2);
        let left = [...rucksack.substring(0, mid)];
        let right = [...rucksack.substring(mid)];
        
        let similarItem = left.filter(value => right.includes(value))[0];
        let priority = similarItem.charCodeAt(0);

        if (priority > 96) {
            total += priority - 96;
        } else {
            total += priority - 38;
        }
    }

    return total;
}


function problemTwo(rucksacks) {
    const N = rucksacks.length / 3;
    let total = 0;

    for (let i = 0; i < rucksacks.length; i += 3) {
        let sack1 = [...rucksacks[i]]
        let sack2 = [...rucksacks[i + 1]]
        let sack3 = [...rucksacks[i + 2]]
        
        let similarItem = sack1.filter(value => {
            if (sack2.includes(value) && sack3.includes(value)) {
                return true;
            }
            return false;
        });

        let priority = similarItem[0].charCodeAt(0);

        if (priority > 96) {
            total += priority - 96;
        } else {
            total += priority - 38;
        }
    }

    return total;
}


const rucksacks = parseData();
console.log(`Problem One: ${problemOne(rucksacks)}`)
console.log(`Problem Two: ${problemTwo(rucksacks)}`)
