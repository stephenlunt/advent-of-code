// https://adventofcode.com/2022/day/6

const fs = require('fs');

const parseData = () => {
    try {
        return fs.readFileSync('./day-06/input.txt', 'utf-8').split('');
    } catch (err) {
        console.error(err);
    }
}

const detectDistinct = (data, n) => {
    for (let i = 0; i < data.length; i++) {
        let marker = new Set(data.slice(i, (i + n)));

        if (marker.size === n) {
            return i + n;
        }
    }
}

const data = parseData();

console.log(`Problem One: ${detectDistinct(data, 4)}`);
console.log(`Problem One: ${detectDistinct(data, 14)}`);
