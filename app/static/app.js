$('#book_name').change(function() {
  var book_title = document.querySelector('#book_name').value;
  console.log(book_title);
  var book_error = document.querySelector('#book_error');

  if (book_title.length == 0) {
    book_error.style.display = "block";
    return false;
  } else {
    book_error.style.display = "none";
  }

  return true;
})

$("#book_name").on('keypress', function (e) {
    if (e.keyCode === 13) {
        postBook();
    }
});

function postBook() {
  var book = document.querySelector("#book_name").value;
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
  //var book_id = document.querySelector('#book_name').value;
  $('#books_main').empty();
  if (typeof json.items === "undefined") {
    $('#books_main').append('Book not found.')
  } else {
    var cols = 0;
    //var row = $('<div>', {'class': 'row'});
    for (var key in json.items) {
      var book = json.items[key].volumeInfo;
      var sale = json.items[key].saleInfo;
      var card = $('<div>', {'class': 'card mb-3'});
      var card_row = $('<div>', {'class': 'row no-gutters'});
      var img_col = $('<div>', {'class': 'book_img book_content col-md-4'});
      $(img_col).append(`<img src=${book.imageLinks.thumbnail} class="card-img">`);
      var card_col = $('<div>', {'class': 'col-md-8'});
      var card_body = $('<div>', {'class': 'card-body'});
      var card_title = $('<h5>', {'class': 'card-title'});
      $(card_title).append(`${book.title}`);
      var pages = $('<div>', { 'id': 'book_pages', 'class': 'card-text' });
      var authors = $('<div>', { 'id': 'book_authors', 'class': 'card-text' });
      var publish = $('<div>', { 'id': 'book_publish', 'class': 'card-text' });
      var availability = $('<div>', { 'id': 'book_availability', 'class': 'card-text for_sale' });

      $(pages).append(`Number of pages: ${book.pageCount}`);
      $(authors).append(`Author(s): `);
      for (var author in book.authors) {
        $(authors).append(`${book.authors[author]} `);
      }
      $(publish).append(`Published: ${book.publishedDate}, ${book.publisher}`);
      if (sale.saleability == "FOR_SALE" || sale.saleability == "FOR_SALE_AND_RENTAL") {
        $(availability).append('Available');
      } else {
        availability = $('<div>', { 'id': 'book_availability', 'class': 'card-text not_for_sale' });
        $(availability).append('Unavailable');
      }

      $(card_body).append(card_title);
      $(card_body).append(pages);
      $(card_body).append(authors);
      $(card_body).append(publish);
      $(card_body).append(availability);
      $(card_col).append(card_body);
      $(card_row).append(img_col);
      $(card_row).append(card_col);
      $(card).append(card_row);
      $('#books_main').append(card);

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

$('#selectTerm').change(function() {
  var term = $('#selectTerm').children("option:selected").val();
  handleScheduleTermChange(term);
})

function handleScheduleTermChange(term) {
  document.location.href="/schedule/" + term;
}
