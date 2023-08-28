// EX XP

// 1)

const compareToTen = (num) => {
  return new Promise((resolve, reject) => {
    if (num <= 10) {
      resolve(`${num} is less than or equal to 10`);
    } else {
      reject(`${num} is greater than 10`);
    }
  });
};

//In the example, the promise should reject
compareToTen(15)
  .then((result) => console.log(result))
  .catch((error) => console.log(error));

//In the example, the promise should resolve
compareToTen(8)
  .then((result) => console.log(result))
  .catch((error) => console.log(error));

// 2)

const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("success");
  }, 4000);
});

myPromise.then((result) => {
  console.log(result); // Output: "success"
});

// 3)

const promiseResolved = Promise.resolve(3);

promiseResolved.then((result) => {
  console.log(result); // Output: 3
});

const promiseRejected = Promise.reject("Boo!");

promiseRejected.catch((error) => {
  console.error(error); // Output: "Boo!"
});
