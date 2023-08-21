// EX XP

// 1.

// 1)

const h1Element = document.querySelector("h1");
console.log(h1Element.textContent);

// 2)

const article = document.querySelector("article");
const paragraphs = article.querySelectorAll("p");

const lastParagraph = paragraphs[paragraphs.length - 1];
article.removeChild(lastParagraph);

// 3)

const h2Element = document.querySelector("h2");

h2Element.addEventListener("click", function () {
  h2Element.style.backgroundColor = "red";
});

// 4)

const h3Element = document.querySelector("h3");

h3Element.addEventListener("click", function () {
  h3Element.style.display = "none";
});

// 5)

const btn = document.querySelector("button");
const boldParagraphs = document.querySelectorAll("p");

btn.addEventListener("click", function () {
  boldParagraphs.forEach((paragraph) => {
    paragraph.style.fontWeight = "bold";
  });
});

// 6)

h1Element.addEventListener("mouseover", function () {
  const randomSize = Math.floor(Math.random() * 101);
  h1Element.style.fontSize = randomSize + "px";
});

// 7)

const fadeParagraph = paragraphs[1];

fadeParagraph.addEventListener("mouseover", function () {
  fadeParagraph.style.transition = "opacity 0.5 ease-in-out";
  fadeParagraph.style.opacity = 0;
});

fadeParagraph.addEventListener("mouseout", function () {
  fadeParagraph.style.transition = "opacity 0.5 ease-in-out";
  fadeParagraph.style.opacity = 1;
});

// 2.

// 1)

const formElement = document.querySelector("form");
console.log(formElement);

// 2)

const inputFname = document.getElementById("fname");
const inputLname = document.getElementById("lname");
const inputSubmit = document.getElementById("submit");

console.log(inputFname);
console.log(inputLname);
console.log(inputSubmit);

// 3)

const firstNameInput = document.getElementsByName("firstname")[0];
const lastNameInput = document.getElementsByName("lastname")[0];

console.log(firstNameInput);
console.log(lastNameInput);

// 4)

const usersAnswerList = document.querySelector(".usersAnswer");

formElement.addEventListener("submit", function (e) {
  e.preventDefault();
  // e.preventDefault() is called to prevent the default form submission behavior, which would cause the page to reload.

  const firstNameValue = inputFname.value.trim();
  const lastNameValue = inputLname.value.trim();

  if (firstNameValue !== "" && lastNameValue !== "") {
    const firstNameListItem = document.createElement("li");
    firstNameListItem.textContent = firstNameValue;

    const lastNameListItem = document.createElement("li");
    lastNameListItem.textContent = lastNameValue;

    usersAnswerList.innerHTML = "";
    usersAnswerList.appendChild(firstNameListItem);
    usersAnswerList.appendChild(lastNameListItem);
  }
});


// 3.

// 1)

let allBoldItems;

const getBoldItems = () => {
  const paragraph = document.getElementById('strong');
  allBoldItems = paragraph.querySelectorAll('strong');
}
getBoldItems();

// 2)

const highlight = () => {
  allBoldItems.forEach(item => {
      item.style.color = 'blue';
  });
}
// highlight();

// 3)

const returnItemsToDefault = () =>{
  allBoldItems.forEach(item => {
    item.style.color = 'black'
  })
}
// returnItemsToDefault();

// 5)

const strongParagraph = document.getElementById('strong');
strongParagraph.addEventListener('mouseover', () =>{
  highlight();
})

strongParagraph.addEventListener('mouseout', () =>{
  returnItemsToDefault();
})