import express, { Request, Response } from "express";
import dotenv from "dotenv";

dotenv.config();
const port = process.env.PORT;
const app = express();

const emojis = [
  { emoji: "😀", name: "Smile" },
  { emoji: "🐶", name: "Dog" },
  { emoji: "🌮", name: "Taco" },
  { emoji: "😀", name: "Grinning Face" },
  { emoji: "🙃", name: "Upside Down Face" },
];

const getRandomEmojis = (count: number) => {
  const shuffled = emojis.sort(() => 0.5 - Math.random());
  return shuffled.slice(0, count);
};

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

app.get("/api/guess/", (req: Request, res: Response) => {
  const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
  const distractors = getRandomEmojis(3);

  const options = [...distractors, randomEmoji];

  const shuffledOptions = options.sort(() => 0.5 - Math.random());

  res.json({ options: shuffledOptions });
});
