

// 1 loop
for (let i = 0; i < 6; i++) {
    let asterisk = "*"
    let triangle = asterisk.repeat(i) + "\n"
    console.log(triangle)
}

//2 loops

for (let i = 0; i < 6; i++) {
    let asterisk = ""
    for (j = 0; j < i; j++) {
        asterisk += "*"
        console.log(asterisk)
    }
}
