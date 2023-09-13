#!/usr/bin/node
const fs = require('fs');

const sFilePathA = process.argv[2];
const sFilePathB = process.argv[3];
const sFilePath = process.argv[4];

function isValidFile(filePath) {
  return fs.existsSync(filePath) && fs.statSync(filePath).isFile();
}

if (sFilePathA && sFilePathB && dFilePath) {
  if (isValidFile(sFilePathA) && isValidFile(sFilePathB)) {

    const sFileContentA = fs.readFileSync(sFilePathA, 'utf8');
    const sFileContentB = fs.readFileSync(sFilePathB, 'utf8');

    const concatenatedContent = sFileContentA + sFileContentB;
    fs.writeFileSync(dFilePath, concatenatedContent);

    console.log(`Successfully concatenated ${sFilePathA} and ${sFilePathB} into ${FilePath}`);
  } else {
    console.error("Error: One or both of the source files are invalid.");
  }
} else {
  console.error("Usage: node script.js <sFilePathA> <sFilePathB> <dFilePath>");
}
