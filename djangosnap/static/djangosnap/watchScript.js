$( document ).ready(function () {
    console.log(mediaURLS);
    for (var i = 0; i < mediaURLS.length; i++) {
      if (isVid(mediaURLS[i])) {
        $('.media-slider').append("<div><video src='" + mediaURLS[i] + "'" + "></video></div>");
      } else {
        $('.media-slider').append("<div><img src='" + mediaURLS[i] + "'" + "></img></div>");
      }
      
    }

    $('.media-slider').slick({
  centerMode: true,
  centerPadding: '60px',
  slidesToShow: 3,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 1
      }
    }
  ]
});
});


     function isVid(url)
     {
         var extension = url.substr(url.length - 3);
         if (extension === 'mp3')
         {
             return true;
         }
         return false;
     }