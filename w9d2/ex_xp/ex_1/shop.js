const { products } = require("./products");

const findProducts = (productName) => {
  const product = products.find((item) => item.name === productName);
  return product;
};

const product1 = findProducts("Product 1");
const product2 = findProducts("Product 4");

if (product1) {
  console.log("Product 1 Details:", product1);
} else {
  console.log("Product 1 not found.");
}

if (product2) {
  console.log("Product 2 Details:", product2);
} else {
  console.log("Product 2 not found.");
}
