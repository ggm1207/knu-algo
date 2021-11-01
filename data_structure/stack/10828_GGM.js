class Stack {
    constructor() {
        // Javascript arrays are typically implemented as hashmaps with one added feature:
        // there is an attribute `length`
        this._arr = new Array(10001);
        this._top = -1;
    }

    push(x) {
        this._top += 1;
        this._arr[this._top] = x;
    }
    pop() {
        if (this.is_empty()) {
            console.log("-1");
            return;
        }
        this.top();
        this._top -= 1;
    }
    size() {
        console.log(String(this._top + 1));
    }
    empty() {
        var temp;
        if (this._top == -1) {
            temp = "1";
        } else {
            temp = "0";
        }
        console.log(temp);
    }
    is_empty() {
        return this._top == -1;
    }
    top() {
        if (this.is_empty()) {
            console.log(" -1");
            return;
        }
        console.log(this._arr[this._top]);
    }
}

function main() {
    // 입력 받아오는 부분은 정답 코드 참고함
    let input = require("fs").readFileSync("./input").toString().split("\n");
    // let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
    let n = +input.shift();
    let s = new Stack();
    for (let i = 0; i < n; ++i) {
        command = input[i];
        switch (command) {
            case "pop":
                s.pop();
                break;
            case "size":
                s.size();
                break;
            case "empty":
                s.empty();
                break;
            case "top":
                s.top();
                break;
            default:
                s.push(+command.substring(5));
        }
    }
}

main();
