$(document).ready(function(){ 
  $('#completed').hide()

  $.get('http://127.0.0.1:8000/api/post/', async function(data){
    len = data['results'].length
    for (let i = 0; i<len; i++){
      const card = document.createElement('div')
      card.className = 'input-group-text';

      const cb = document.createElement('input');
      cb.type = 'checkbox'
      cb.name = 'checkbox'
      cb.id = 'checkbox' + data['results'][i].id

      const text_label = document.createElement('label');
      text_label.setAttribute('for', 'checkbox' + data['results'][i].id)
      text_label.className = 'text'
      text_label.id = 'c' + data['results'][i].id
      text_label.innerText = data['results'][i].text

      card.appendChild(cb)
      card.appendChild(text_label)
      
      if (data['results'][i].done == true){
        document.getElementById('card-container-completed').appendChild(card);
        $(String('#checkbox' + data['results'][i].id)).prop('checked', true);
        $(String('#c' + data['results'][i].id)).css('text-decoration', 'line-through');
      }
      else{
        document.getElementById('card-container').appendChild(card);
        $(String('#c' + data['results'][i].id)).css('text-decoration', 'none');
      }

      $(String('#checkbox' + data['results'][i].id)).click(function(){
        $.get(`http://127.0.0.1:8000/api/post/${data['results'][i].id}/`, async function(data){
          if (data.done == false){
            $.ajax({
            url : `http://127.0.0.1:8000/api/post/${data.id}/`,
            method: 'PATCH',
            data : {text : data.text, date : data.date, done : true},
            })
            $(String('#c' + data.id)).css({'text-decoration' : 'line-through'});
            document.getElementById('card-container-completed').appendChild(card);
          }

          else {
            $.ajax({
              url : `http://127.0.0.1:8000/api/post/${data.id}/`,
              method: 'PATCH',
              data : {text : data.text, date : data.date, done : false},
            })
            $(String('#c' + data.id)).css({'text-decoration': 'none'});
            document.getElementById('card-container').appendChild(card);
          }

        })
      })
      
    }
  })
})