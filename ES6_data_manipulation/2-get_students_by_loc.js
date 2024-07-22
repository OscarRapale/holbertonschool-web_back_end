export default function getStudentsByLocation(students, city) {

    const studentCity = students.filter(student => student.location === city);

    return studentCity;
}
