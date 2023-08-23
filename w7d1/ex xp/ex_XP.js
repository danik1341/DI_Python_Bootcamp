const prompt = require("prompt-sync")(); // here for Node testing purposes

//  EX XP

// 1)

// const displayNumbersDivisible = () => {
//     let sum = 0;
//     for (let i = 0; i <= 500; i++) {
//         if ( i % 23 === 0){
//             console.log(i)
//             sum+=i;
//         }
//     }
//     console.log(`Sum: ${sum}`)
// }
// displayNumbersDivisible();

const displayNumbersDivisible = (divisor) => {
  let sum = 0;
  for (let i = 0; i <= 500; i++) {
    if (i % divisor === 0) {
      console.log(i);
      sum += i;
    }
  }
  console.log(`Sum: ${sum}`);
};
displayNumbersDivisible(3);
console.log("---");
displayNumbersDivisible(45);
console.log("/////////////////////////////////////////");

// 2)

const stock = {
  banana: 6,
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1,
};

const prices = {
  banana: 4,
  apple: 2,
  pear: 1,
  orange: 1.5,
  blueberry: 10,
};

const shoppingList = ["banana", "orange", "apple"];

const myBill = () => {
  totalBill = 0;

  for (const item of shoppingList) {
    if (item in stock && stock[item] > 0) {
      totalBill += prices[item];
      stock[item]--;
    }
  }

  return totalBill;
};

const billAmount = myBill();
console.log("Total Bill:", billAmount);
console.log("Updated Stock:", stock);
console.log("/////////////////////////////////////////");

// 3)

const changeEnough = (itemPrice, amountOfChange) => {
  const [quarters, dimes, nickels, pennies] = amountOfChange;
  const totalChange =
    quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01;

  return totalChange >= itemPrice;
};

console.log(changeEnough(4.25, [25, 20, 5, 0])); // outcome -> true
console.log(changeEnough(14.11, [2, 100, 0, 0])); // outcome ->  false
console.log(changeEnough(0.75, [0, 0, 20, 5])); // outcome -> true
console.log("/////////////////////////////////////////");

// 4)

const hotelCost = () => {
  let totalCost = 0;
  let validInput = false;

  while (!validInput) {
    const numOfNights = prompt(
      "How many nights would you like to stay in the hotel?"
    );

    if (numOfNights === null) {
      return null;
    }

    const parsedNumber = parseInt(numOfNights);

    if (!isNaN(numOfNights) && numOfNights > 0) {
      totalCost = parsedNumber * 140;
      validInput = true;
    } else {
      // alert("Please enter a valid number of nights."); In browsers
      console.log("Please enter a valid number of nights."); //Outside browsers
    }
  }
  return totalCost;
};

const totalPrice = hotelCost();

if (totalPrice !== null) {
  console.log("Total Price:", totalPrice);
} else {
  console.log("Input canceled by user.");
}
console.log("/////////////////////////////////////////");

const planeRideCost = () => {
  let destinationPrice = 0;
  let validInput = false;

  while (!validInput) {
    const destination = prompt("Where is your destination?");

    if (typeof destination === "string" && destination.trim() !== "") {
      const trimmedDestination = destination.trim().toLowerCase();

      switch (trimmedDestination) {
        case "london":
          destinationPrice = 183;
          validInput = true;
          break;
        case "paris":
          destinationPrice = 220;
          validInput = true;
          break;
        default:
          destinationPrice = 300;
          validInput = true;
          break;
      }
    } else {
      // alert("Please enter a valid destination."); In browsers
      console.log("Please enter a valid destination.");
    }
  }

  return destinationPrice;
};

const totalCost = planeRideCost();

if (totalCost !== null) {
  console.log("Total Cost:", totalCost);
} else {
  console.log("Input canceled by user.");
}
console.log("/////////////////////////////////////////");

const rentalCarCost = () => {
  let rentPrice = 0;
  let validInput = false;

  while (!validInput) {
    const numOfDays = prompt("How many days would you rent the car?");

    if (numOfDays === null) {
      return null;
    }

    const parsedNumber = parseInt(numOfDays);

    if (!isNaN(numOfDays) && numOfDays > 0) {
      rentPrice = parsedNumber * 40;
      if (parsedNumber > 10) {
        rentPrice *= 0.95;
      }
      validInput = true;
    } else {
      // alert("Please enter a valid number of days."); In browsers
      console.log("Please enter a valid number of days."); //Outside browsers
    }
  }
  return rentPrice;
};

const rentPrice = rentalCarCost();

if (rentPrice !== null) {
  console.log("Total Price:", rentPrice);
} else {
  console.log("Input canceled by user.");
}
console.log("/////////////////////////////////////////");

const totalVacationCost = () => {
  const hotelCostValue = hotelCost();
  const planeRideCostValue = planeRideCost();
  const rentalCarCostValue = rentalCarCost();

  if (
    hotelCostValue === null ||
    planeRideCostValue === null ||
    rentalCarCostValue === null
  ) {
    return null;
  }

  const totalCost = hotelCostValue + planeRideCostValue + rentalCarCostValue;
  return totalCost;
};

const totalVacationPrice = totalVacationCost();

if (totalVacationPrice !== null) {
  console.log("Total Vacation Cost:", totalVacationPrice);
} else {
  console.log("Input canceled by user in one of the functions.");
}

// 5)

const containerDiv = document.getElementById("container");
console.log(containerDiv);

const peteElement = document.querySelector(
  ".list:nth-child(1) li:nth-child(2)"
);
peteElement.textContent = "Richard";

const secondUl = document.querySelector(".list:nth-child(2)");
const secondLi = secondUl.querySelector("li:nth-child(2)");
secondUl.removeChild(secondLi);

const listElements = document.querySelectorAll(".list li:first-child");
listElements.forEach((element) => {
  element.textContent = "Daniel";
});

const ulElements = document.querySelectorAll("ul");
ulElements.forEach((ul) => ul.classList.add("student_list"));

const firstUl = document.querySelector(".student_list:nth-child(1)");
firstUl.classList.add("university", "attendance");

containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";

const danLi = firstUl.querySelector("li:last-child");
danLi.style.display = "none";

const richardLi = firstUl.querySelector("li:nth-child(2)");
richardLi.style.border = "1px solid black";

document.body.style.fontSize = "16px";

const usersInDiv = firstUl.textContent
  .split("\n")
  .filter((user) => user.trim() !== "");
if (containerDiv.style.backgroundColor === "lightblue") {
  alert(`Hello ${usersInDiv.join(" and ")}`);
}

// 6)

const navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const newListItem = document.createElement("li");

const textNode = document.createTextNode("Logout");

newListItem.appendChild(textNode);

const ulElement = document.querySelector("#socialNetworkNavigation ul");
ulElement.appendChild(newListItem);

const firstListItem = ulElement.firstElementChild;
const lastListItem = ulElement.lastElementChild;

console.log("First Link:", firstListItem.textContent);
console.log("Last Link:", lastListItem.textContent);

// 7)

const allBooks = [
  {
    title: "Harry Potter",
    author: "J.K. Rowling",
    image: "https://example.com/harry_potter.jpg",
    alreadyRead: true,
  },
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image: "https://example.com/the_hobbit.jpg",
    alreadyRead: false,
  },
];

const listBooksSection = document.querySelector(".listBooks");

allBooks.forEach((book) => {
  const bookDiv = document.createElement("div");
  bookDiv.classList.add("book");

  const titlePara = document.createElement("p");
  titlePara.textContent = `Title: ${book.title}`;

  const authorPara = document.createElement("p");
  authorPara.textContent = `Author: ${book.author}`;

  const image = document.createElement("img");
  image.src = book.image;
  image.style.width = "100px";

  if (book.alreadyRead) {
    titlePara.style.color = "red";
    authorPara.style.color = "red";
  }

  bookDiv.appendChild(titlePara);
  bookDiv.appendChild(authorPara);
  bookDiv.appendChild(image);

  listBooksSection.appendChild(bookDiv);
});
