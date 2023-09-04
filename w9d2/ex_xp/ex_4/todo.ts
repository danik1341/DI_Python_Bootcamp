export class TodoList {
  private tasks: { text: string; completed: boolean }[] = [];

  addTask(text: string): void {
    this.tasks.push({ text, completed: false });
  }

  markTaskCompleted(index: number): void {
    if (index >= 0 && index < this.tasks.length) {
      this.tasks[index].completed = true;
    }
  }

  listTasks(): void {
    this.tasks.forEach((task, index) => {
      console.log(`${index + 1}. [${task.completed ? "x" : " "}] ${task.text}`);
    });
  }
}
