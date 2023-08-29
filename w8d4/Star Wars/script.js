const name = document.getElementById("name");
const height = document.getElementById("height");
const gender = document.getElementById("gender");
const birthYear = document.getElementById("birth-year");
const homeWorld = document.getElementById("home-world");
const button = document.getElementById("button");

const loading = () => {
  name.innerHTML =
    '<i class="fa fa-spinner fa-pulse fa-3x fa-fw"></i> <p>Loading...</p>';
  height.innerText = "";
  gender.innerText = "";
  birthYear.innerText = "";
  homeWorld.innerText = "";
};

const errorFetching = () => {
  name.innerText = "Error fetching data.";
  height.innerText = String.fromCodePoint(0x1f480);
  gender.innerText = String.fromCodePoint(0x1f480);
  birthYear.innerText = String.fromCodePoint(0x1f480);
  homeWorld.innerText = String.fromCodePoint(0x1f480);
};

const fetchData = async () => {
  loading();

  const randomNumber = Math.floor(Math.random() * 88 + 1);
  const apiUrl = `https://swapi.dev/api/people/${randomNumber}/`;

  try {
    const response = await axios.get(apiUrl);
    return response.data;
  } catch (err) {
    console.error("Error fetching SW API data", err);
    errorFetching();
    throw err;
  }
};

const updateInfo = async () => {
  name.innerHTML = "";
  height.innerHTML = "";
  gender.innerHTML = "";
  birthYear.innerHTML = "";
  homeWorld.innerHTML = "";

  const data = await fetchData();

  const homePlanet = await axios.get(data.homeworld);

  name.innerHTML = data.name;
  height.innerHTML = `Height: ${data.height}`;
  gender.innerHTML = `Gender: ${data.gender}`;
  birthYear.innerHTML = `Birth Year: ${data.birth_year}`;
  homeWorld.innerHTML = `Home World: ${homePlanet.data.name}`;
};

button.addEventListener("click", updateInfo);
