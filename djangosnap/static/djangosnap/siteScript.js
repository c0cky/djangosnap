$( document ).ready(function() {
  // Handler for .ready() called.
  var path = window.location.pathname;
  if (path == "/") {
  	path = "index";
  }
  try {
      var highlight = replaceAll(path, '/', '');
  } catch (e) {
      highlight = path;
  }
  console.log(highlight);
  $('li').removeClass();
  $('#' + highlight).addClass('active');

});

replaceAll = function(string, omit, place, prevstring) {
  if (prevstring && string === prevstring)
    return string;
  prevstring = string.replace(omit, place);
  return replaceAll(prevstring, omit, place, string)
}





