const stdin = require('fs').readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt').toString().split('\n');
const input = (() => {
    let line = 0
    return () => stdin[line++]
})();

N = Number(input())

const candidates = [...Array(3)].map((v, i) => new Map([['1', 0], ['2', 0], ['3', 0], ['total', 0], ['num', i + 1]]))

for (let i = 0; i < N; i++) {
    const [a, b, c] = input().trimRight().split(' ')
    candidates[0].set(a, candidates[0].get(a) + 1)
    candidates[0].set('total', candidates[0].get('total') + Number(a))
    candidates[1].set(b, candidates[1].get(b) + 1)
    candidates[1].set('total', candidates[1].get('total') + Number(b))
    candidates[2].set(c, candidates[2].get(c) + 1)
    candidates[2].set('total', candidates[2].get('total') + Number(c))
}

candidates.sort((a, b) => {
    if (a.get('total') == b.get('total')) {
        if (a.get('3') == b.get('3')) {
            return a.get('2') - b.get('2')
        }
        return a.get('3') - b.get('3')
    }
    return a.get('total') - b.get('total')
})

const [a, b] = [candidates[2], candidates[1]]
if (a.get('total') != b.get('total')) {
    console.log(a.get('num'), a.get('total'))
}
else if (a.get('1') != b.get('1')) {
    console.log(a.get('num'), a.get('total'))
}
else {
    console.log(0, a.get('total'))
}
