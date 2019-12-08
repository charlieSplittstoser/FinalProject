function checkLibraryFields() {
  var book_id = document.querySelector('#id_type').value;
  var book_value = document.querySelector('#id_value').value;

  if (book_id.value == 'Select') {
    document.querySelector('#id_error').innerHTML = "Please select an ID.";
    return false;
  }

  if (book_value.length == 0) {
    document.querySelector('#value_error').innerHTML = "Please enter book value.";
    return false;
  }

  return true;

}

function postBook() {
  var id_type = document.querySelector("#id_type").value;
  var id_value = document.querySelector("#id_value").value;
	fetch(`proxy/${id_type}/${id_value}`)
	.then(function(response) {
     	return response.json();
  })
  	.then(function(json) {
  		console.log('Request successful', json);
  		callbackFunc(json);
  })
  	.catch(function(error) {
    	console.log('Request failed', error)
  });
}

function callbackFunc(json) {
  console.log("IN CALLBACK");
  var book_id = document.querySelector('#id_type').value;
  if (typeof json.records === undefined) {
    $('#book_title').append('Book not found.')
  } else {
    for (var key in json.records[0])
    $('#book-title').append(`${key.details.details.title}`);
  }
}

function enrollUser(userId, courseId) {
  fetch(`../enrollUser/${userId}/${courseId}`, { mode: 'cors' })
  .then(function(response) {
    return response.text();
  })
  .then(function(resp) {
    if(resp == "Success") {
      $('#enrollMessage').text("Successfully enrolled!");
      $('#enrollMessage').removeClass('error');
      $('#enrollMessage').addClass('success');
      console.log('Request successful', resp);
    } else {
      $('#enrollMessage').text("Failure to enroll. Perhaps you are already enrolled in this course.");
      $('#enrollMessage').removeClass('success');
      $('#enrollMessage').addClass('error');
      console.log('Request failure', resp);
    }

    var backBtn = $('<a>', { 'href':'../catalog', 'class': 'btn btn-outline-primary', 'role': 'button' });
    backBtn.text('Return to Catalog');
    $('#enrollBtnGroup').empty();
    $('#enrollBtnGroup').append(backBtn);
  })
  .catch(function(error) {
    console.log('Request failed', error);
  });
}
