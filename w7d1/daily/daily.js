const planets = [
  { name: "Mercury", color: "gray", moons: 0 },
  { name: "Venus", color: "yellow", moons: 0 },
  { name: "Earth", color: "blue", moons: 1 },
  { name: "Mars", color: "red", moons: 2 },
  { name: "Jupiter", color: "orange", moons: 79 },
  { name: "Saturn", color: "gold", moons: 83 },
  { name: "Uranus", color: "lightblue", moons: 27 },
  { name: "Neptune", color: "blue", moons: 14 },
];

const listPlanetsSection = document.querySelector(".listPlanets");

planets.forEach((planet) => {
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet", planet.name.toLowerCase());
  planetDiv.style.backgroundColor = planet.color;

  const planetName = document.createElement("p");
  planetName.textContent = planet.name;

  planetDiv.appendChild(planetName);

  if (planet.moons > 0) {
    for (let i = 0; i < planet.moons; i++) {
      const moonDiv = document.createElement("div");
      moonDiv.classList.add("moon");
      moonDiv.style.left = `${Math.random() * 80 + 10}%`;
      moonDiv.style.top = `${Math.random() * 80 + 10}%`;
      planetDiv.appendChild(moonDiv);
    }
  }

  listPlanetsSection.appendChild(planetDiv);
});
