const readline = require('readline');
const interface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
interface.question('Welcome to Holberton School, what is your name?\n', (input) => {
  console.log(`Your name is: ${input}`);
  interface.close();
})
rl.close();
console.log('This important software is now closing\n');
