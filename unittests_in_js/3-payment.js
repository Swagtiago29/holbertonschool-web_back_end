const Utils = require('./utils')
function sendPaymentRequestsToApi(totalAmount, totalShipping) {
    const result = Utils.calculateNumber('SUM', totalAmount, totalShipping)
    console.log(`The total is: ${result}`)
}
module.exports = sendPaymentRequestsToApi;