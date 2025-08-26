const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
    describe('type SUM', function () {
        it('should round the numbers and add them', function () {
            expect(calculateNumber('SUM', 2.2, 1.1)).to.equal(3);
        });
        it('should round the numbers and add them', function () {
            expect(calculateNumber('SUM', 2.7, 3.7)).to.equal(7)
        })
    })
    describe('type SUBTRACT', function () {
        it('should round the numbers and subtract them', function () {
            expect(calculateNumber('SUBTRACT', 9.7, 4.7)).to.equal(5)
        });
        it('should round the numbers and subtract them', function () {
            expect(calculateNumber('SUBTRACT', 6.2, 3.2)).to.equal(3)
        })
    })
    describe('type DIVIDE', function () {
        it('should round the numbers and divide them', function () {
            expect(calculateNumber('DIVIDE', 9.7, 4.7)).to.equal(2)
        });
        it('should round the numbers and subtract them', function () {
            expect(calculateNumber('DIVIDE', 6.2, 3.2)).to.equal(2)
        });
                it('should round the numbers and return Error', function(){
            expect(calculateNumber('DIVIDE', 3.2, 0)).to.equal('Eror')
        })
    })
});