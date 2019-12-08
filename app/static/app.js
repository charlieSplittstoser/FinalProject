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
  var book = document.querySelector("#book_title").value;
	fetch(`proxy/${book}`)
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
  $('.book_content').empty();
  var book_id = document.querySelector('#book_name').value;
  if (typeof json.items === undefined) {
    $('#book_title').append('Book not found.')
  } else {
    for (var key in json.items) {

     var book = json.items[key].volumeInfo;


      $('#book_title').append(`${book.title}`);
      $('#book_pages').append(`Number of pages: ${book.pageCount}`);
      $('#book_authors').append(`Author(s): `);
      for (var author in book.authors) {
        $('#book_authors').append(`${book.authors[author]} `);
      }
      $('#book_publish').append(`Published: ${book.publishedDate}, ${book.publisher}`);
      //$('#book_availability').append(`Availability: ${book.ebooks[0].availability}`);
      $('#book_cover').append(`<img src=${book.imageLinks.thumbnail}>`);
    }
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
