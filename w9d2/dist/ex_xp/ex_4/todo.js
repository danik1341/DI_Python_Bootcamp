"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.TodoList = void 0;
class TodoList {
    constructor() {
        this.tasks = [];
    }
    addTask(text) {
        this.tasks.push({ text, completed: false });
    }
    markTaskCompleted(index) {
        if (index >= 0 && index < this.tasks.length) {
            this.tasks[index].completed = true;
        }
    }
    listTasks() {
        this.tasks.forEach((task, index) => {
            console.log(`${index + 1}. [${task.completed ? "x" : " "}] ${task.text}`);
        });
    }
}
exports.TodoList = TodoList;
