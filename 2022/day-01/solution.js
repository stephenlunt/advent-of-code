var fs = require('fs');

const data = fs.readFileSync('./day-01/input.txt', 'utf-8').split('\n\n');

const summedValues = sumValues();
console.log(`Problem 1: ${Math.max(...summedValues)}`);
sortSummedValues(summedValues);

function sumValues() {
    let values = []
    let sum = 0;

    data.forEach(elf => {
        const totals = elf.split('\n');
            
        for (let value of totals) {
            sum += parseInt(value);
        }

        values.push(sum);
        sum = 0;
    })

    return values;
}

function sortSummedValues(summedValues) {
    summedValues.sort();
    let topThree = summedValues.slice(sumValues.length - 3, sumValues.length);
    console.log(topThree);
}


