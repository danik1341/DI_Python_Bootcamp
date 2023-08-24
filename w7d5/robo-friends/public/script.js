const robots = [
  {
    id: 1,
    name: "Leanne Graham",
    username: "Bret",
    email: "Sincere@april.biz",
    image: "https://robohash.org/1?200x200",
  },
  {
    id: 2,
    name: "Ervin Howell",
    username: "Antonette",
    email: "Shanna@melissa.tv",
    image: "https://robohash.org/2?200x200",
  },
  {
    id: 3,
    name: "Clementine Bauch",
    username: "Samantha",
    email: "Nathan@yesenia.net",
    image: "https://robohash.org/3?200x200",
  },
  {
    id: 4,
    name: "Patricia Lebsack",
    username: "Karianne",
    email: "Julianne.OConner@kory.org",
    image: "https://robohash.org/4?200x200",
  },
  {
    id: 5,
    name: "Chelsey Dietrich",
    username: "Kamren",
    email: "Lucio_Hettinger@annie.ca",
    image: "https://robohash.org/5?200x200",
  },
  {
    id: 6,
    name: "Mrs. Dennis Schulist",
    username: "Leopoldo_Corkery",
    email: "Karley_Dach@jasper.info",
    image: "https://robohash.org/6?200x200",
  },
  {
    id: 7,
    name: "Kurtis Weissnat",
    username: "Elwyn.Skiles",
    email: "Telly.Hoeger@billy.biz",
    image: "https://robohash.org/7?200x200",
  },
  {
    id: 8,
    name: "Nicholas Runolfsdottir V",
    username: "Maxime_Nienow",
    email: "Sherwood@rosamond.me",
    image: "https://robohash.org/8?200x200",
  },
  {
    id: 9,
    name: "Glenna Reichert",
    username: "Delphine",
    email: "Chaim_McDermott@dana.io",
    image: "https://robohash.org/9?200x200",
  },
  {
    id: 10,
    name: "Clementina DuBuque",
    username: "Moriah.Stanton",
    email: "Rey.Padberg@karina.biz",
    image: "https://robohash.org/10?200x200",
  },
];

const donBot = {
  name: "Donbot",
  text: "There's no one here, capiche?",
  userText: "no search results found",
  image: "images/donbot.png",
};

const robotContainer = document.getElementById("robotContainer");

const createRobotCard = (robot) => {
  const card = document.createElement("div");
  card.className =
    "flex flex-col items-center justify-center max-w-sm lg:max-w-md lg:w-80 lg:w-[28rem] lg:h-[35rem] min-h-full m-2 overflow-hidden rounded shadow-lg h-[25rem] bg-teal-400 bg-fixed bg-center";
  card.style = "background-image: url('images/card-pattern.png')";

  const image = document.createElement("img");
  image.className = "w-[80%] rounded-full bg-slate-600";
  image.src = robot.image;
  image.alt = robot.name;

  const content = document.createElement("div");
  content.className = "max-w-sm px-6 mt-5 tracking-[-0.04em] lg:mt-14";

  const name = document.createElement("h1");
  name.className = "mb-2 text-xl font-bold lg:text-3xl";
  name.textContent = robot.name;

  const email = document.createElement("h2");
  email.className = "mb-2 text-lg font-semibold lg:text-xl";
  email.textContent = robot.email;

  content.appendChild(name);
  content.appendChild(email);
  card.appendChild(image);
  card.appendChild(content);

  return card;
};

const renderRobotCards = () => {
  robotContainer.innerHTML = "";

  const searchInput = document
    .getElementById("searchInput")
    .value.toLowerCase();
  const filteredRobots = robots.filter((robot) =>
    robot.name.toLowerCase().includes(searchInput)
  );

  if (filteredRobots.length === 0) {
    const noResultsMessage = document.createElement("div");
    noResultsMessage.className =
      "flex flex-col items-center justify-center max-w-sm lg:max-w-md lg:w-80 lg:w-[28rem] lg:h-[35rem] min-h-full m-2 overflow-hidden rounded shadow-lg h-[25rem] bg-teal-400 bg-fixed bg-center";
    noResultsMessage.style = "background-image: url('images/card-pattern.png')";

    const image = document.createElement("img");
    image.className = "w-[80%] rounded-full";
    image.src = donBot.image;
    image.alt = donBot.name;

    const content = document.createElement("div");
    content.className = "max-w-sm px-6 mt-5 tracking-[-0.04em] lg:mt-14";

    const text = document.createElement("h1");
    text.className = "mb-2 text-xl font-bold lg:text-3xl";
    text.textContent = donBot.text;

    const userText = document.createElement("h2");
    userText.className = "mb-2 text-lg font-semibold lg:text-xl";
    userText.textContent = donBot.userText;

    content.appendChild(text);
    content.appendChild(userText);
    noResultsMessage.appendChild(image);
    noResultsMessage.appendChild(content);

    robotContainer.appendChild(noResultsMessage);
  } else {
    filteredRobots.forEach((robot) => {
      const card = createRobotCard(robot);
      robotContainer.appendChild(card);
    });
  }
};

renderRobotCards();
const searchInput = document.getElementById("searchInput");
searchInput.addEventListener("input", renderRobotCards);
