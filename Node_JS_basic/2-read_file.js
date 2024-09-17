const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf8');
    
    // Split the data into lines
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    // Remove the header line
    const header = lines.shift();
    
    // Initialize a dictionary to store students by field
    const studentsByField = {};
    
    // Process each line
    lines.forEach(line => {
      const [firstname, lastname, age, field] = line.split(',');
      
      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      
      studentsByField[field].push(firstname);
    });
    
    // Log the total number of students
    console.log(`Number of students: ${lines.length}`);
    
    // Log the number of students in each field and their first names
    for (const field in studentsByField) {
      const students = studentsByField[field];
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (error) {
    // If an error occurs, throw an error with the specified message
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
