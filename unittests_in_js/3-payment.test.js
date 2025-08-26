const { expect } = require('chai')
const sinon = require('sinon')
const Utils = require('./utils')
const sendPaymentRequestsToApi = require('./3-payment')

describe('sendPaymentRequestsToApi', function(){
    it('should call Utils.calculateNumber with SUM, 100, 20', function(){
        const spy = sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestsToApi(100, 20);
        expect(spy.calledOnce).to.be.true;
        expect(spy.calledWith('SUM', 100, 20)).to.be.true;
        spy.restore();
    })
})