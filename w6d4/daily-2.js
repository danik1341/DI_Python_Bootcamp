// Daily Challenge: Stars

// Single Loop ->

const n = 6;

let line = '';
for (let i = 1; i <= n; i++) {
  line += '* ';
  console.log(line);
}

// Nested Loop ->

const m = 6;

for (let i = 1; i <= m; i++) {
  let line = '';
  for (let j = 1; j <= i; j++) {
    line += '* ';
  }
  console.log(line);
}
