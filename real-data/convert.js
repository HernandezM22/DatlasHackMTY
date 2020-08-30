const csvToJson = require('convert-csv-to-json');

const input = './mach_learn_data.csv'; 
const output = './public/original.json';

csvToJson.fieldDelimiter(',').formatValueByType().generateJsonFileFromCsv(input, output);