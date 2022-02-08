function madlib(name, subject) {
  let nameUpper = name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
  let subjectLower = subject.toLowerCase();
  console.log(`${nameUpper}'s favorite subject in school is ${subjectLower}.`);
}
