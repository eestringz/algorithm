const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    const strArr = [...str]    
    result = []
    
    strArr.map((it) => {
        if (it === it.toUpperCase()) {
            result.push(it.toLowerCase())
        } else {
            result.push(it.toUpperCase())
        }
    })
    
    console.log(result.join(''))
    
});