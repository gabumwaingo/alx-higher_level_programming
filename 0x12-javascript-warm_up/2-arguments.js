#!/usr/bin/node
const myVar = process.argv.length;
if (myVar === 2){
	console.log('No argument');
} else {
	console.log('Arguments found');
}
