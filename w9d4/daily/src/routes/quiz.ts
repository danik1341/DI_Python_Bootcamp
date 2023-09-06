import express, { Request, Response } from "express";

export const quizRouter = express.Router();

const triviaQuestions = [
  {
    question: "What is the capital of France?",
    answer: "Paris",
  },
  {
    question: "Which planet is known as the Red Planet?",
    answer: "Mars",
  },
  {
    question: "What is the largest mammal in the world?",
    answer: "Blue whale",
  },
];

let currentQuestionIndex = 0;
let score = 0;

quizRouter.get("/", (req: Request, res: Response) => {
  if (currentQuestionIndex < triviaQuestions.length) {
    const question = triviaQuestions[currentQuestionIndex].question;
    res.render("quiz", { question });
  } else {
    res.redirect("/quiz/score");
  }
});

quizRouter.post("/", (req: Request, res: Response) => {
  const userAnswer = req.body.answer;
  const correctAnswer = triviaQuestions[currentQuestionIndex].answer;

  if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
    score++;
  }

  currentQuestionIndex++;

  res.redirect("/quiz");
});

quizRouter.get("/score", (req: Request, res: Response) => {
  res.render("score", { score, totalQuestions: triviaQuestions.length });
});
