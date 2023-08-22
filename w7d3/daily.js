let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = () =>{
    groceries.fruits.forEach(fruit => {
        console.log(fruit);
    })
}

displayGroceries();

const cloneGroceries = () => {
    let user = client;
    client = "Betty";
    console.log("User:", user); // User: John
    console.log("Client:", client); // Client: Betty
    // JavaScript variables store references to values rather than the values themselves. 
    // So, when you change the value of client, 
    // the reference held by both client and user is updated, 
    // leading to the observed behavior.
    // reassigning user with client after the change of client,
    // user will also be the new change value of Betty
    user = client;
    console.log("User:", user); // User: Betty

    let shopping = groceries;
    groceries.totalPrice = "35$";
    console.log("Total Price, Shopping: ", shopping.totalPrice); // Total Price, Shopping:  35$
    console.log("Total Price, Groceries: ", groceries.totalPrice); // Total Price, Groceries:  35$

    groceries.paid = false;
    console.log("Paid, Shopping: ",shopping.paid); // Paid, Shopping:  false
    console.log("Paid, Groceries: ",groceries.paid); // Paid, Groceries:  false

    // A variable named shopping is created and assigned the value of the groceries variable. 
    // shopping now refers to the same object as groceries, not a copy.
    // we see the modification in the shopping object for both totalPrice 
    // and paid properties because shopping refers to the same object as groceries. 
    // Both variables hold a reference to the same object in memory, 
    // so changes made through one variable will be reflected in the other.
}

cloneGroceries();