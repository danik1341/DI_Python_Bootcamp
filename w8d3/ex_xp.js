// EX XP

// 1)

const apiUrl =
  "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";

const fetchData = async () => {
  try {
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.error("Fetch error:", err);
  }
};

fetchData();

// 2)

const sunData = async () => {
  try {
    const response = await fetch(
      "https://api.giphy.com/v1/gifs/search?q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
    );

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.error("Fetch error:", err);
  }
};

sunData();

// 3)

const swData = async () => {
  try {
    const response = await fetch("https://www.swapi.tech/api/starships/9/");

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.error("Fetch error:", err);
  }
};

swData();

// 4)

// the console log would be:
// calling
// resolved
