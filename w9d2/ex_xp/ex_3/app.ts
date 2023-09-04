import { readFile, writeFile } from "./fileManager";

async function main() {
  try {
    const helloContent = await readFile("ex_xp/ex_3/Hello_World.txt");
    console.log("Content of Hello_World.txt:", helloContent);

    await writeFile("ex_xp/ex_3/Bye_World.txt", "Wrting to the file");
    console.log("Successfully wrote to file");
  } catch (err) {
    console.error("Error:", err);
  }
}

main();
