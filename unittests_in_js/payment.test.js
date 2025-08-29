const { expect } = require('chai')
const sinon = require('sinon')
const Utils = require('./utils')
const sendPaymentRequestsToApi = require('./3-payment')

describe('sendPaymentRequestsToApi', function () {

    it('should call Utils.calculateNumber with SUM, 100, 20', function () {
        const spy = sinon.spy(console, 'log');
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

        sendPaymentRequestsToApi(100, 20);

        expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(spy.calledOnceWithExactly('The total is: 10')).to.be.true;
    })
})