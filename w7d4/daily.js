const gameInfo = [
  {
    username: "john",
    team: "red",
    score: 5,
    items: ["ball", "book", "pen"],
  },
  {
    username: "becky",
    team: "blue",
    score: 10,
    items: ["tape", "backpack", "pen"],
  },
  {
    username: "susy",
    team: "red",
    score: 55,
    items: ["ball", "eraser", "pen"],
  },
  {
    username: "tyson",
    team: "green",
    score: 1,
    items: ["book", "pen"],
  },
];

const usernames = [];

gameInfo.forEach((player) => {
  usernames.push(player.username + "!");
});

console.log(usernames);

// better way ->

const usernamesBetterWay = gameInfo.map((user) => user.username + "!");
console.log(usernamesBetterWay);

const winners = [];

gameInfo.forEach((player) => {
  player.score > 5 ? winners.push(player.username) : null;
});

console.log(winners);

let scoreSum = 0;
gameInfo.forEach((player) => (scoreSum += player.score));

console.log(scoreSum);
