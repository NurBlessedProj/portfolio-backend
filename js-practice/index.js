const fs = require("fs");
let result = "";

// function whenDataExist(err, data) {
//   if (err) {
//     console.log("your error " + err);
//   } else {
//     console.log("read data ok " + data);
//   }
// }
function addText(err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}

// fs.readFile("./texts.txt", "utf8", whenDataExist);
// fs.appendFile("./texts.txt", "hello this was writin asjdasojpd[", addText);
// fs.appendFile
// fs.mkdir("seven", addText);
// fs.appendFile("./seven/programming.txt", "this is the programming file", addText);
// fs.appendFile("./seven/web.json", "", addText);
fs.copyFile("./seven/programming","./seven/web.json", addText);
