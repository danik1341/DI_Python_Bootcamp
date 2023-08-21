// 1)

// part 1

setTimeout(() => {
    alert("Hello world!");
}, 2000)

// part 2

setTimeout(() => {
    const container = document.getElementById("container");
    const newParagraph = document.createElement('p');
    newParagraph.textContent = "Hello world!";
    container.appendChild(newParagraph);
}, 2000)

// part 3

const container = document.getElementById('container');
const clearButton = document.getElementById('clear');

let intervalId;

const addParagraph = () => {
    const newParagraph = document.createElement('p');
    newParagraph.textContent = "Hello world!";
    container.appendChild(newParagraph);

    if (container.querySelectorAll('p').length === 5) {
        clearInterval(intervalId);
    }
}

intervalId = setInterval(addParagraph, 2000);

clearButton.addEventListener('click', () => {
    clearInterval(intervalId);
})