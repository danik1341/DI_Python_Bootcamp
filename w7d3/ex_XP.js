// 1)

// 1.

// The value of 'a' inside funcOne will be changed to 3 within the if block.

// What will happen if the variable is declared with const instead of let ?
// If 'a' is declared with const, the code will throw an error since you cannot reassign a const variable.

// 2.

// The value of 'a' will be changed to 5 by funcTwo, and both funcThree calls will use this updated value.

//What will happen if the variable is declared with const instead of let ?
// If 'a' is declared with const, the code will throw an error when trying to reassign 'a' in funcTwo.

// 3.

// Since 'a' is assigned to the global object window in funcFour, funcFive can access it and will display "hello".

// 4.

// The inner 'a' in funcSix shadows the outer 'a', so inside the function, 'a' is "test".

// What will happen if the variable is declared with const instead of let ?
// If 'a' is declared with const, the code will work the same way. The inner 'a' in funcSix is still a separate variable from the outer 'a'.

// 5.

// in the if block 5
// outside of the if block 2
// The if block defines a new block-scoped 'a', so within the block, 'a' is 5. Outside the block, 'a' remains 2.

// What will happen if the variable is declared with const instead of let ?
// If 'a' is declared with const, the code will work the same way. The inner 'a' in the if block is still separate from the outer 'a'.

// 2)

// function winBattle(){
//     return true;
// }

const winBattle = () => {
    return true;
}

const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints);

// 3)

const isString = value => typeof value === 'string';
console.log(isString('hello'));  // true
console.log(isString([1, 2, 4, 0])); // false

// 4)

const sum = (num1, num2) => num1 + num2;
console.log(sum(10,5));

// 5)

console.log(kgToGramsDeclaration(5)); // Output: 5000
// Function Declaration
function kgToGramsDeclaration(kg) {
    return kg * 1000;
}


// Function Expression
const kgToGramsExpression = function(kg) {
    return kg * 1000;
};

console.log(kgToGramsExpression(3)); // Output: 3000

// Difference between Function Declaration and Function Expression:
// Function declarations are hoisted, which means they can be used before they're declared in the code.
// Function expressions are not hoisted and can only be used after they're defined.

// One-line Arrow Function
const kgToGramsArrow = kg => kg * 1000;

console.log(kgToGramsArrow(2)); // Output: 2000

// 6)

(function(numberOfChildren, partnerName, geographicLocation, jobTitle) {
    const sentence = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnerName} with ${numberOfChildren} kids.`;
    document.getElementById('fortune').textContent = sentence;
})(3, 'John', 'New York', 'Web Developer');

// 7)

// if I'd a navbar it would be as so -
{/* <nav id="navbar">
        <!-- Navbar content here -->
</nav> */}

(function(username) {
    const navbar = document.getElementById('navbar');

    const welcomeDiv = document.createElement('div');
    welcomeDiv.classList.add('welcome');

    welcomeDiv.innerHTML = `
        <p>Welcome, ${username}!</p>
        <img src="profile_picture.jpg" alt="Profile Picture">
    `;

    navbar.appendChild(welcomeDiv);
})('John');

// 8)

// const makeJuice = (size) => {
//     const ingredients = [];
//     const addIngredients = (ingredient1, ingredient2, ingredient3) => {
//         const sentence = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}.`;
//         document.getElementById('juice-order').textContent = sentence;
//     }

//     addIngredients('apple', 'orange', 'carrot');
// }

// makeJuice('medium');

const makeJuice = (size) => {
    const ingredients = [];
    const addIngredients = (ingredient1, ingredient2, ingredient3) => {
        ingredients.push(ingredient1, ingredient2, ingredient3);
    }

    const displayJuice = () =>{
        const sentence = `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`;
        document.getElementById('juice-order').textContent = sentence;
    }

    addIngredients('apple', 'orange', 'carrot');
    addIngredients('banana', 'strawberry', 'pineapple');
    displayJuice();
}

makeJuice('large');