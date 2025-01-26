const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    
    const rows = data.trim().split('\n');
    
    if (rows.length === 0) {
      throw new Error('Cannot load the database');
    }

    const headers = rows[0].split(',');
    
    const studentsByField = {};

    rows.slice(1).forEach((row) => {
      const student = row.split(',');
      
      if (student.length === headers.length) {
        headers.forEach((field, index) => {
          const value = student[index];
          if (value !== '') {
            if (!studentsByField[field]) {
              studentsByField[field] = [];
            }
            studentsByField[field].push(value);
          }
        });
      }
    });

    const totalStudents = Object.values(studentsByField).reduce((acc, list) => acc + list.length, 0);

    console.log(`Number of students: ${totalStudents}`);

    Object.entries(studentsByField).forEach(([field, students]) => {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    });

  } catch (error) {
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
