function randomLogin() {
  $.ajax({
    type: 'POST',
    url: '/test/randomLogin',
    data: '',
    contentType: "application/json",
    dataType: 'json',
    success: function(data) {
      if(data.code == 200){
        var user_id = data.user_id;
        var token = data.token;
        localStorage.setItem("token", token);
        $('#login_id').html(user_id);
      }
    }
  });
}


function logout() {
  localStorage.removeItem("token");
  $('#login_id').html('NULL');
}


function sendFile() {
  var input_file = $("#input_file")[0].files[0];
  var formData = new FormData();
  var token = localStorage.getItem("token");

  // Verify the validity of the front-end
  if(token == null) {
      alert('Login is required');
      return false;
  }

  formData.append("token", token);
  formData.append("input_file", input_file);

  $.ajax({
    url: 'api/v1/saveFile',
    processData: false,
    contentType: false,
    data: formData,
    type: 'POST',
    success: function(data) {
      if(data.code == 403){
        alert('Login is required');
      } else {
        alert('File Transfer Completed');
      }
    }
  })
}
