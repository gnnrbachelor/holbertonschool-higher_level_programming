#!/usr/bin/node

let size = Math.floor(process.argv[2]);
if (isNaN(size)) {
	console.log('Missing size');
} else {
	for (i = 0; i < size; i++) {
		for (j = 0; j < size; j++) {
			process.stdout.write('X');
		}
		if (j === size) {
			console.log();
		}
	}
}

