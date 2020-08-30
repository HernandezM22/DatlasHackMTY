const csvToJson = require('convert-csv-to-json');

const input = './pred2.csv'; 
const output = './public/pred2.json';

csvToJson.fieldDelimiter(',').formatValueByType().generateJsonFileFromCsv(input, output);