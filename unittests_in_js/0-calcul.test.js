const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function (){
    it('should round the numbers and add them', function () {
        assert.strictEqual(calculateNumber(2.2, 1.1), 3)
    });
});