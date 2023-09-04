"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const fileManager_1 = require("./fileManager");
function main() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const helloContent = yield (0, fileManager_1.readFile)("ex_xp/ex_3/Hello_World.txt");
            console.log("Content of Hello_World.txt:", helloContent);
            yield (0, fileManager_1.writeFile)("ex_xp/ex_3/Bye_World.txt", "Wrting to the file");
            console.log("Successfully wrote to file");
        }
        catch (err) {
            console.error("Error:", err);
        }
    });
}
main();
