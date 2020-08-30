const csvToJson = require('convert-csv-to-json');

const input = './pred1.csv'; 
const output = './public/pred1.json';

csvToJson.fieldDelimiter(',').formatValueByType().generateJsonFileFromCsv(input, output);