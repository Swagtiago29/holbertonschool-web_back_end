const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
    describe('type SUM', function () {
        it('should round the numbers and add them', function () {
            assert.strictEqual(calculateNumber('SUM', 2.2, 1.1), 3)
        });
        it('should round the numbers and add them', function () {
            assert.strictEqual(calculateNumber('SUM', 2.7, 3.7), 7)
        })
    })
    describe('type SUBTRACT', function () {
        it('should round the numbers and subtract them', function () {
            assert.strictEqual(calculateNumber('SUBTRACT', 9.7, 4.7), 5)
        });
        it('should round the numbers and subtract them', function () {
            assert.strictEqual(calculateNumber('SUBTRACT', 6.2, 3.2), 3)
        })
    })
    describe('type DIVIDE', function () {
        it('should round the numbers and divide them', function () {
            assert.strictEqual(calculateNumber('DIVIDE', 9.7, 4.7), 2)
        });
        it('should round the numbers and subtract them', function () {
            assert.strictEqual(calculateNumber('DIVIDE', 6.2, 3.2), 2)
        })
    })
});