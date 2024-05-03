const express = require('express');
const app = express();

// Обробник GET-запитів
app.get('/', (req, res) => {
    // Отримання особистих даних
    const name = 'Datsenko Anastasiia';
    const course = 'Computer Science';
    const group = 'IS-21';

    // Формування відповіді з особистими даними
    const response = {
        surname: name.split(' ')[0],
        firstName: name.split(' ')[1],
        course: course,
        group: group
    };

    // Відправлення відповіді у форматі JSON
    res.json(response);
});

// Запуск HTTP-серверу на порту 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`HTTP server running on port ${PORT}...`);
});


