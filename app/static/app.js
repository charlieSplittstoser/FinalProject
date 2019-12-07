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
