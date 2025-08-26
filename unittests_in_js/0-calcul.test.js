const assert = require('assert');

describe('calculateNumber', function (){
    it('should round the numbers and add them', function () {
        assert.strictEqual(calculateNumber(2.2, 1.1), 3)
    });
});