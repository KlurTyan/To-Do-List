const checkbox = document.getElementById('checkbox');
checkbox.addEventListener('change', (event) => {
  const form = document.getElementById('checkbox');
  const formData = new FormData(form);
  fetch(form.action, {
    method: 'POST',
    body: formData,
  })
  .then(response => {
    // Processing a successful response
    console.log('Успешный ответ от сервера');
  })
  .catch(error => {
    // Error Handling
    console.error('Ошибка отправки запроса:', error);
  });
});

// Does not work
