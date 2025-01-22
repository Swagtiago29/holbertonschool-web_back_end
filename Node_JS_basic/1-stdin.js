const readline = require('readline');
const read = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
read.question('Welcome to Holberton School, what is your name?', (INPUT) => {
  console.log('Your name is: ${INPUT}');
  read.close();
})