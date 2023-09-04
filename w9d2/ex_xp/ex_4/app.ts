import { TodoList } from "./todo";

const todoList = new TodoList();

todoList.addTask("Buy SOME MILK!");
todoList.addTask("Find Dad");
todoList.addTask("Get da bag");

todoList.markTaskCompleted(0);

console.log("Todo List:");
todoList.listTasks();
