const csvToJson = require('convert-csv-to-json');

const input = './pred3.csv'; 
const output = './public/pred3.json';

csvToJson.fieldDelimiter(',').formatValueByType().generateJsonFileFromCsv(input, output);